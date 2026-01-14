"""Database management for offline-first kitten-care content."""
import sqlite3
import json
from datetime import datetime
from typing import List, Optional
from models import Guide, StepFlow, Step, ChecklistItem, Diagram, Bookmark


class KittenGuideDB:
    """SQLite database for offline guide content."""
    
    def __init__(self, db_path: str = "kitten_guide.db"):
        self.db_path = db_path
        self.conn = None
        self._init_db()
    
    def _init_db(self):
        """Initialize database schema."""
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        cursor = self.conn.cursor()
        
        # Guides table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS guides (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                summary TEXT,
                markdown_body TEXT,
                topics TEXT,
                age_min_weeks INTEGER,
                age_max_weeks INTEGER,
                urgency TEXT,
                analogy_cards TEXT,
                do_list TEXT,
                dont_list TEXT,
                updated_at TEXT
            )
        """)
        
        # Search index table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS search_index (
                doc_id TEXT PRIMARY KEY,
                title TEXT,
                plain_body TEXT,
                tags TEXT,
                age_range TEXT,
                topic TEXT,
                urgency_boost INTEGER,
                FOREIGN KEY (doc_id) REFERENCES guides(id)
            )
        """)
        
        # Diagrams table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS diagrams (
                id TEXT PRIMARY KEY,
                guide_id TEXT,
                asset_ref TEXT,
                alt TEXT,
                caption TEXT,
                hotspots TEXT,
                FOREIGN KEY (guide_id) REFERENCES guides(id)
            )
        """)
        
        # Step flows table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS step_flows (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                progress INTEGER DEFAULT 0
            )
        """)
        
        # Steps table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS steps (
                id TEXT PRIMARY KEY,
                flow_id TEXT,
                title TEXT NOT NULL,
                instructions TEXT,
                examples TEXT,
                time_estimate TEXT,
                red_flags TEXT,
                analogy TEXT,
                step_order INTEGER,
                FOREIGN KEY (flow_id) REFERENCES step_flows(id)
            )
        """)
        
        # Checklist items table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS checklist_items (
                id TEXT PRIMARY KEY,
                step_id TEXT,
                text TEXT,
                completed INTEGER DEFAULT 0,
                FOREIGN KEY (step_id) REFERENCES steps(id)
            )
        """)
        
        # Bookmarks table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookmarks (
                guide_id TEXT PRIMARY KEY,
                created_at TEXT,
                FOREIGN KEY (guide_id) REFERENCES guides(id)
            )
        """)
        
        self.conn.commit()
    
    def add_guide(self, guide: Guide):
        """Add a guide to the database."""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO guides 
            (id, title, summary, markdown_body, topics, age_min_weeks, age_max_weeks, 
             urgency, analogy_cards, do_list, dont_list, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            guide.id,
            guide.title,
            guide.summary,
            guide.markdown_body,
            json.dumps(guide.topics),
            guide.age_min_weeks,
            guide.age_max_weeks,
            guide.urgency,
            json.dumps(guide.analogy_cards),
            json.dumps(guide.do_list),
            json.dumps(guide.dont_list),
            guide.updated_at.isoformat()
        ))
        
        # Add to search index
        urgency_boost = 3 if guide.urgency == "Now" else (2 if guide.urgency == "Today" else 0)
        cursor.execute("""
            INSERT OR REPLACE INTO search_index
            (doc_id, title, plain_body, tags, age_range, topic, urgency_boost)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            guide.id,
            guide.title,
            guide.markdown_body,
            " ".join(guide.topics),
            f"{guide.age_min_weeks or 0}-{guide.age_max_weeks or 999}",
            guide.topics[0] if guide.topics else "",
            urgency_boost
        ))
        
        # Add diagrams
        for diagram in guide.diagrams:
            cursor.execute("""
                INSERT OR REPLACE INTO diagrams
                (id, guide_id, asset_ref, alt, caption, hotspots)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                diagram.id,
                guide.id,
                diagram.asset_ref,
                diagram.alt,
                diagram.caption,
                json.dumps(diagram.hotspots)
            ))
        
        self.conn.commit()
    
    def search_guides(self, query: str, topic: Optional[str] = None, 
                     urgency: Optional[str] = None) -> List[Guide]:
        """Search guides with filters."""
        cursor = self.conn.cursor()
        
        sql = """
            SELECT g.*, s.urgency_boost
            FROM guides g
            JOIN search_index s ON g.id = s.doc_id
            WHERE (s.title LIKE ? OR s.plain_body LIKE ? OR s.tags LIKE ?)
        """
        params = [f"%{query}%", f"%{query}%", f"%{query}%"]
        
        if topic:
            sql += " AND s.topic = ?"
            params.append(topic)
        
        if urgency:
            sql += " AND g.urgency = ?"
            params.append(urgency)
        
        sql += " ORDER BY s.urgency_boost DESC, g.title"
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
        guides = []
        for row in rows:
            guides.append(Guide(
                id=row[0],
                title=row[1],
                summary=row[2],
                markdown_body=row[3],
                topics=json.loads(row[4]) if row[4] else [],
                age_min_weeks=row[5],
                age_max_weeks=row[6],
                urgency=row[7],
                analogy_cards=json.loads(row[8]) if row[8] else [],
                do_list=json.loads(row[9]) if row[9] else [],
                dont_list=json.loads(row[10]) if row[10] else [],
                diagrams=[],
                updated_at=datetime.fromisoformat(row[11])
            ))
        
        return guides
    
    def get_guide(self, guide_id: str) -> Optional[Guide]:
        """Get a specific guide by ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM guides WHERE id = ?", (guide_id,))
        row = cursor.fetchone()
        
        if not row:
            return None
        
        return Guide(
            id=row[0],
            title=row[1],
            summary=row[2],
            markdown_body=row[3],
            topics=json.loads(row[4]) if row[4] else [],
            age_min_weeks=row[5],
            age_max_weeks=row[6],
            urgency=row[7],
            analogy_cards=json.loads(row[8]) if row[8] else [],
            do_list=json.loads(row[9]) if row[9] else [],
            dont_list=json.loads(row[10]) if row[10] else [],
            diagrams=[],
            updated_at=datetime.fromisoformat(row[11])
        )
    
    def get_all_guides(self) -> List[Guide]:
        """Get all guides."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM guides ORDER BY title")
        rows = cursor.fetchall()
        
        guides = []
        for row in rows:
            guides.append(Guide(
                id=row[0],
                title=row[1],
                summary=row[2],
                markdown_body=row[3],
                topics=json.loads(row[4]) if row[4] else [],
                age_min_weeks=row[5],
                age_max_weeks=row[6],
                urgency=row[7],
                analogy_cards=json.loads(row[8]) if row[8] else [],
                do_list=json.loads(row[9]) if row[9] else [],
                dont_list=json.loads(row[10]) if row[10] else [],
                diagrams=[],
                updated_at=datetime.fromisoformat(row[11])
            ))
        
        return guides
    
    def add_bookmark(self, guide_id: str):
        """Bookmark a guide."""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO bookmarks (guide_id, created_at)
            VALUES (?, ?)
        """, (guide_id, datetime.now().isoformat()))
        self.conn.commit()
    
    def remove_bookmark(self, guide_id: str):
        """Remove a bookmark."""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM bookmarks WHERE guide_id = ?", (guide_id,))
        self.conn.commit()
    
    def get_bookmarked_guides(self) -> List[Guide]:
        """Get all bookmarked guides."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT g.* FROM guides g
            JOIN bookmarks b ON g.id = b.guide_id
            ORDER BY b.created_at DESC
        """)
        rows = cursor.fetchall()
        
        guides = []
        for row in rows:
            guides.append(Guide(
                id=row[0],
                title=row[1],
                summary=row[2],
                markdown_body=row[3],
                topics=json.loads(row[4]) if row[4] else [],
                age_min_weeks=row[5],
                age_max_weeks=row[6],
                urgency=row[7],
                analogy_cards=json.loads(row[8]) if row[8] else [],
                do_list=json.loads(row[9]) if row[9] else [],
                dont_list=json.loads(row[10]) if row[10] else [],
                diagrams=[],
                updated_at=datetime.fromisoformat(row[11])
            ))
        
        return guides
    
    def is_bookmarked(self, guide_id: str) -> bool:
        """Check if a guide is bookmarked."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM bookmarks WHERE guide_id = ?", (guide_id,))
        return cursor.fetchone() is not None
    
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
