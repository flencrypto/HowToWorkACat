"""Data models for How To Work A Cat kitten-care guide."""
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Diagram:
    """Visual guide diagram."""
    id: str
    asset_ref: str
    alt: str
    caption: str
    hotspots: List[str]


@dataclass
class ChecklistItem:
    """Individual checklist item within a step."""
    id: str
    text: str
    completed: bool = False


@dataclass
class Step:
    """Individual step within a guide flow."""
    id: str
    title: str
    instructions: List[str]
    checklist_items: List[ChecklistItem]
    examples: List[str]
    diagrams: List[Diagram]
    time_estimate: str
    red_flags: List[str]
    analogy: Optional[str] = None


@dataclass
class Guide:
    """Main content guide."""
    id: str
    title: str
    summary: str
    markdown_body: str
    topics: List[str]
    age_min_weeks: Optional[int]
    age_max_weeks: Optional[int]
    urgency: str  # "Now", "Today", "Monitor", or ""
    analogy_cards: List[str]
    diagrams: List[Diagram]
    updated_at: datetime
    do_list: List[str]
    dont_list: List[str]


@dataclass
class StepFlow:
    """Ordered sequence of steps for onboarding."""
    id: str
    title: str
    description: str
    steps: List[Step]
    progress: int = 0  # Number of completed steps


@dataclass
class Bookmark:
    """User bookmark for a guide."""
    guide_id: str
    created_at: datetime


@dataclass
class SearchResult:
    """Search result with scoring."""
    guide: Guide
    score: float
    match_type: str  # "title", "tags", "body"
