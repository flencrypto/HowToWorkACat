"""Sample kitten-care content with UK tone and terminology."""
from datetime import datetime
from models import Guide, Diagram
from database import KittenGuideDB


def load_sample_content(db: KittenGuideDB):
    """Load sample kitten-care guides into the database."""
    
    guides = [
        Guide(
            id="first-24-hours",
            title="First 24 hours: the 'tiny flatmate' protocol",
            summary="Your kitten's first day home - what to expect and how to help them settle without panicking",
            markdown_body="""# First 24 Hours: The Tiny Flatmate Protocol

## Why this matters
The first day sets the tone for your kitten's confidence. Think of it like you've just moved into a shared flat where everything smells wrong, you don't know where the loo is, and your new flatmate keeps trying to cuddle you.

## Safe Room Setup Diagram
```
    ┌─────────────────────────────────────────┐
    │         SAFE ROOM LAYOUT                │
    │                                         │
    │  [Door]                                 │
    │                                         │
    │   🛏️ Hiding Spot         💧 Water      │
    │   (under bed/box)         Bowl          │
    │                                         │
    │                                         │
    │   👕 Your t-shirt                       │
    │   in cozy bed            🍽️ Food       │
    │                           Bowl          │
    │                                         │
    │                    Keep 1+ meter apart  │
    │                    ↕                    │
    │                                         │
    │   🚽 Litter Tray                       │
    │   (far from food!)                     │
    │                                         │
    │              [Window - close curtains]  │
    └─────────────────────────────────────────┘

    KEY:
    ✅ Food & water together (but separate bowls)
    ✅ Litter tray in opposite corner
    ✅ Multiple hiding spots = security
    ✅ Your scent (t-shirt) = comfort
    ❌ Don't put food next to litter
    ❌ Don't block hiding spots
```

## Do this now (if you're panicking)
1. **Put them in one room** - bedroom or bathroom, not the whole house
2. **Show them the litter tray** - place them in it gently, don't make a fuss
3. **Leave food and water nearby** (but not next to the litter - would you eat dinner in your bathroom?)
4. **Sit on the floor and ignore them** - read a book, scroll your phone, be boring
5. **No visitors for 48 hours** - seriously

## What to expect
- **Hiding**: Completely normal. They might live under the bed for a day. That's fine.
- **Not eating**: Common for 12-24 hours. After that, ring the vet.
- **Tiny miaows**: They're calling for mum. Heartbreaking but normal.
- **Litter tray confusion**: Might wee on your duvet. Don't shout. Show them the tray.

## Do
- ✅ Let them approach you
- ✅ Speak softly (they're not deaf, just terrified)
- ✅ Keep one room as their "base camp"
- ✅ Put a worn t-shirt in their bed (your smell = comfort)

## Don't
- ❌ Chase them to cuddle
- ❌ Let other pets investigate yet
- ❌ Have mates round to "meet the kitten"
- ❌ Move their litter tray around like furniture
- ❌ Panic if they're quiet - quiet is good

## If you're stuck
**Kitten hasn't eaten in 24 hours**: Ring your vet. Dehydration happens fast.
**Kitten won't stop crying**: Warm (not hot) water bottle wrapped in a towel, ticking clock nearby, your old t-shirt. Radio on low.
**Can't find kitten**: Check inside washing machine, under sofas, inside box springs. They're ninjas.

## Human analogy
Imagine you've been dropped in a foreign country where you don't speak the language, everything smells weird, and giants keep trying to pick you up. You'd hide in the hotel bathroom too.

## Red flags - ring vet NOW
- 🔴 No drinking for 12+ hours
- 🔴 Laboured breathing or panting
- 🔴 Completely limp or unresponsive
- 🔴 Pale gums
- 🔴 Blood anywhere
""",
            topics=["Onboarding", "Behaviour", "Health"],
            age_min_weeks=0,
            age_max_weeks=16,
            urgency="",
            analogy_cards=["Like moving into a shared flat where everything smells wrong"],
            diagrams=[
                Diagram(
                    id="safe-room-setup",
                    asset_ref="safe_room_layout",
                    alt="Safe room layout showing optimal placement of litter tray, food, water, and hiding spots",
                    caption="Ideal safe room setup for first 24 hours - keep food away from litter tray",
                    hotspots=["litter-far-from-food", "hiding-spots", "water-and-food-together"]
                )
            ],
            do_list=["Let them approach you", "Speak softly", "Keep one room as base camp", "Put worn t-shirt in their bed"],
            dont_list=["Chase them to cuddle", "Let other pets investigate yet", "Have mates round to meet kitten", "Move litter tray around"],
            updated_at=datetime.now()
        ),
        
        Guide(
            id="litter-tray-basics",
            title="Litter tray: treat it like the bathroom you share with a flatmate",
            summary="How to set up and maintain a litter tray that you'd happily eat toast in (well, almost)",
            markdown_body="""# Litter Tray: The Shared Bathroom Protocol

## Why this matters
A grim litter tray = wees on your bed. It's that simple. Cats are cleaner than you. If the tray smells like a festival toilet, they'll find somewhere better (your laundry basket, probably).

## Litter Tray Placement Guide
```
    GOOD LOCATIONS ✅               BAD LOCATIONS ❌
    
    🚽 Utility room corner          ❌ Next to food bowls
    (quiet, private)                (Would you eat in a loo?)
    
    🚽 Bathroom corner              ❌ Busy hallway
    (makes sense, right?)           (Like using a toilet on stage)
    
    🚽 Spare bedroom corner         ❌ Next to washing machine
    (peaceful, accessible)          (Noise = terror)
    
    🚽 Under stairs                 ❌ In garage
    (private, easy to reach)        (Too isolated, too cold)

    DEPTH & SIZE GUIDE:
    ┌─────────────────────┐
    │    3-5cm deep       │ ← Perfect depth
    │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │
    │                     │
    └─────────────────────┘
     ↑                   ↑
     1.5x kitten length (min)
     
    RULE: Number of trays = Number of cats + 1
    Example: 1 cat = 2 trays | 2 cats = 3 trays
```

## Do this now (if you're panicking)
1. **Scoop the poo twice a day** - morning and evening, like brushing your teeth
2. **Change the litter completely once a week**
3. **Clean the tray with hot water** (not bleach - cats hate chemical smells)
4. **Put it somewhere private but accessible** - not next to food, not in a busy hallway

## The golden rules
- **One tray per cat, plus one extra** - if you have one kitten, you need two trays
- **Size matters** - tray should be 1.5x the length of your kitten (they grow fast)
- **Depth** - 3-5cm of litter, not a thin scatter, not a sandpit
- **Location** - quiet corner, easy access, away from food/water

## Do
- ✅ Use unscented, clumping litter (they hate perfume)
- ✅ Scoop daily minimum (preferably twice)
- ✅ Wash your hands after (obvious, but still)
- ✅ Praise them when they use it (softly, don't make it weird)

## Don't
- ❌ Use scented litter or air fresheners nearby
- ❌ Move the tray randomly
- ❌ Put it next to washing machine (noise = scary)
- ❌ Let it smell like a bin
- ❌ Punish accidents (they're not being spiteful, they're confused)

## If you're stuck
**Kitten weeing outside tray**: Check if tray is clean, check if tray is too small, check if something scared them (loud noise?), ring vet if it continues (could be infection).
**Kitten eating litter**: Common in tiny kittens. Switch to non-clumping briefly. If it continues, vet check.
**Poo everywhere but tray**: Might be too dirty, might be scared of the location, might be medical. Try second tray in different spot.

## Human analogy
Would you use a public toilet with no door, next to the kitchen, that hasn't been cleaned in a week and smells like artificial flowers? Neither would your kitten.

## Red flags - ring vet NOW
- 🔴 Blood in urine or poo
- 🔴 Straining to wee with nothing coming out (URGENT - can be fatal)
- 🔴 Diarrhoea for 24+ hours
- 🔴 Crying while using tray
""",
            topics=["Litter", "Health", "Behaviour"],
            age_min_weeks=0,
            age_max_weeks=52,
            urgency="",
            analogy_cards=["Like the bathroom you share with a flatmate - keep it clean enough to eat toast in"],
            diagrams=[
                Diagram(
                    id="litter-tray-placement",
                    asset_ref="litter_placement_guide",
                    alt="Guide showing good and bad locations for litter tray placement",
                    caption="Good vs bad litter tray locations - privacy matters!",
                    hotspots=["quiet-corner", "away-from-food", "avoid-busy-areas"]
                ),
                Diagram(
                    id="litter-depth-size",
                    asset_ref="litter_tray_sizing",
                    alt="Diagram showing correct litter depth and tray size relative to kitten",
                    caption="Correct litter depth (3-5cm) and tray size (1.5x kitten length)",
                    hotspots=["litter-depth", "tray-size-ratio", "number-of-trays"]
                )
            ],
            do_list=["Scoop twice daily", "Use unscented clumping litter", "Wash hands after", "Praise when they use it"],
            dont_list=["Use scented litter", "Move tray randomly", "Put next to washing machine", "Let it smell bad"],
            updated_at=datetime.now()
        ),
        
        Guide(
            id="biting-hands",
            title="Biting hands: you are not on a chew-toy subscription",
            summary="How to teach your kitten that human fingers are not prey or teething rings",
            markdown_body="""# Biting Hands: Unsubscribe from the Chew-Toy Service

## Why this matters
"It's cute when they're tiny" becomes "I'm bleeding through my jeans" very quickly. Kittens have needle teeth and no concept of gentle. Teach them now or regret it when they're 5kg of muscle with sabres.

## Cat Body Language Decoder (branded palette)

### ✅ Happy to play (sage green)
- Relaxed tail
- Forward ears
- Soft eyes
- What to do: “Let’s play!” — initiate play, offer toys, engage

### 🟠 Overstimulated (amber)
- Tail flicking
- Ears sideways
- Dilated pupils
- What to do: Slow down — reduce intensity, watch closely

### 🛑 Stop now (brick red)
- Tail lashing
- Ears flat back
- Tense body
- What to do: STOP OR I BITE — walk away, give space, end interaction

## Bite Prevention Flowchart
```
    Kitten approaches hands
            ↓
    Are you actively playing?
       ↙         ↘
     YES          NO
      ↓            ↓
    Use toy,    Let them sniff
    not hands   Stay still
      ↓            ↓
    They bite? → HIGH "OW!"
                    ↓
              Walk away immediately
                    ↓
              Wait 5 minutes
                    ↓
              Offer proper toy
                    ↓
              Redirect energy
```

## Do this now (if you're panicking)
1. **Never use hands as toys** - not even once, not even "just this time"
2. **When they bite, make a high "OW!" sound** - mimics kitten pain sound
3. **Immediately stop playing and walk away** - game over, you've gone boring
4. **Give them a proper toy instead** - redirect the energy

## Why they're doing it
- **Play aggression**: You're a fun toy that makes noises
- **Teething** (3-6 months): Their gums hurt, you're soft
- **Overstimulation**: They're excited and don't know how to stop
- **Learned behaviour**: You've accidentally taught them it's OK

## Do
- ✅ Play with wand toys (keeps hands far from teeth)
- ✅ Stop all interaction when they bite (even if it's "gentle")
- ✅ Give them teething toys (frozen wet flannel is brilliant)
- ✅ Tire them out with proper play sessions (15 min twice daily minimum)

## Don't
- ❌ Pull hand away fast (triggers prey drive)
- ❌ Shout or tap their nose (teaches fear, not manners)
- ❌ Let them "play bite" (there's no such thing)
- ❌ Use fingers to play "chase the finger" (YOU ARE TEACHING THEM TO BITE)

## If you're stuck
**Kitten bites during petting**: They're overstimulated. Learn their "I'm done" signals (tail flicking, ears back, skin twitching). Stop before they bite.
**Kitten attacks feet**: Morning zoomies. Play with them properly before breakfast to burn energy.
**Kitten won't let go**: Don't pull. Push gently towards their mouth (triggers release reflex), then walk away.

## Human analogy
Imagine your mate kept poking you for fun. First time, you laugh. Tenth time, you're annoyed. Hundredth time, you'd snap. Your kitten doesn't know the difference between "play bite" and "bite" - they're all the same word in Cat.

## Red flags - ring vet NOW
- 🔴 Bite breaks skin and looks infected (red, hot, swollen)
- 🔴 Sudden aggression from a previously calm kitten (could be pain/illness)
- 🔴 Biting themselves raw (could be fleas, allergies, stress)
""",
            topics=["Behaviour", "Play"],
            age_min_weeks=8,
            age_max_weeks=52,
            urgency="",
            analogy_cards=["You are not a 24/7 chew-toy subscription service"],
            diagrams=[
                Diagram(
                    id="cat-body-language",
                    asset_ref="body_language_decoder",
                    alt="Cat body language guide showing happy, overstimulated, and stop signals",
                    caption="Learn to read your kitten's mood before they bite",
                    hotspots=["relaxed-signals", "warning-signs", "stop-signals"]
                ),
                Diagram(
                    id="bite-prevention-flow",
                    asset_ref="bite_prevention_flowchart",
                    alt="Flowchart showing how to respond when kitten approaches hands",
                    caption="What to do when kitten wants to play with your hands",
                    hotspots=["redirect-to-toys", "walk-away-response", "ow-sound"]
                )
            ],
            do_list=["Use wand toys", "Stop when they bite", "Give teething toys", "Tire them out"],
            dont_list=["Pull hand away fast", "Shout or tap nose", "Let them play bite", "Use fingers to play"],
            updated_at=datetime.now()
        ),
        
        Guide(
            id="not-eating",
            title="Won't eat: stress, teething or vet o'clock — checklist",
            summary="Decision tree for when your kitten refuses food and when to panic",
            markdown_body="""# Won't Eat: Is This Normal or Vet o'Clock?

## Why this matters
Kittens are tiny. They have almost no reserves. Not eating for 24 hours can lead to serious problems (dehydration, low blood sugar, liver issues). But sometimes they're just being picky little sods.

## Not Eating Decision Tree
```
    Kitten hasn't eaten
            ↓
    ┌───────────────────┐
    │ How long ago?     │
    └───────────────────┘
            ↓
    ┌───────┴───────┬──────────┬──────────┐
    ↓               ↓          ↓          ↓
  0-12hrs        12-24hrs    24+hrs    Other symptoms?
    ↓               ↓          ↓          ↓
  MONITOR        CALL VET   VET NOW!   VET NOW!
    ↓
Are they drinking?
  ↓         ↓
 YES        NO → CALL VET
  ↓
Try these:
├─ Warm food (room temp)
├─ Different texture (wet/dry)
├─ Flat plate (not bowl)
├─ Hand feeding
└─ Smellier food (tuna)
    ↓
Still not eating after trying?
    ↓
Wait 2-4 hours, try again
    ↓
If reaches 12 hours → CALL VET
```

## Quick Checklist Before Panicking
```
□ Is food fresh? (not day-old)
□ Is bowl clean? (cats are fussy)
□ Has anything changed? (new home/food/stress)
□ Are they drinking water? (crucial!)
□ Any other symptoms? (lethargy/vomiting/diarrhea)

RED FLAGS = VET NOW (even if under 24hrs):
🔴 Not drinking water
🔴 Lethargic/floppy
🔴 Vomiting or diarrhoea
🔴 Pale gums
🔴 Cold ears/paws
```

## Do this now (if you're panicking)
**Time check - how long since they last ate?**
- **Under 12 hours**: Monitor, try different food, stay calm
- **12-24 hours**: Ring vet for advice
- **24+ hours**: Vet NOW (bring kitten with you)

**Quick checks:**
1. Is the food fresh? (Would you eat day-old tuna left out?)
2. Is the bowl clean? (Cats have better noses than you)
3. Has anything changed? (New home, new food, new stress?)
4. Are they drinking water? (If yes, less urgent than if no)

## Common reasons (not scary)
- **New environment**: Stress = no appetite (normal for 12-24 hours)
- **Food temperature**: Too cold (from fridge) or too hot
- **Bowl type**: Whiskers touching sides = annoying
- **Teething** (3-6 months): Sore gums, prefer soft food
- **Just ate a moth**: They're full of insect

## Do
- ✅ Warm food to room temperature (smells better)
- ✅ Offer different textures (wet + dry + treats)
- ✅ Use flat plate instead of bowl (whisker stress is real)
- ✅ Try hand-feeding tiny amounts (reconnects them with eating)
- ✅ Make sure water is fresh and available

## Don't
- ❌ Force feed (makes it worse)
- ❌ Change food brand every 2 hours (tummy upset)
- ❌ Leave wet food out all day (goes rank, they won't touch it)
- ❌ Panic immediately (but do monitor closely)

## If you're stuck
**Kitten interested in food but won't eat**: Could be mouth pain (check teeth, check for sores), could be smell (try smellier food like tuna).
**Kitten ignoring food completely**: More concerning. Vet call.
**Eating but then vomiting**: Different problem - see "Vomiting" guide or ring vet.

## The 24-hour rule
- **0-12 hours**: Watch and try different foods
- **12-24 hours**: Ring vet for advice (have kitten details ready: age, weight, vaccination status, any other symptoms)
- **24+ hours**: Vet appointment NOW

## Human analogy
You've had days where you're too stressed/tired/unwell to eat. But you have reserves. Your kitten is running on a tiny tank. It's like trying to run a phone with 2% battery - it doesn't take long to shut down.

## Red flags - ring vet NOW (even if under 24 hours)
- 🔴 Not drinking water either
- 🔴 Lethargic (floppy, won't play, sleeping more than normal)
- 🔴 Vomiting or diarrhoea as well
- 🔴 Pale gums
- 🔴 Cold ears/paws
- 🔴 Rapid breathing
- 🔴 Any other symptoms
""",
            topics=["Health", "Feeding"],
            age_min_weeks=0,
            age_max_weeks=52,
            urgency="Today",
            analogy_cards=["Like running a phone on 2% battery - doesn't take long to shut down"],
            diagrams=[
                Diagram(
                    id="not-eating-decision-tree",
                    asset_ref="eating_decision_tree",
                    alt="Decision tree flowchart for when kitten won't eat",
                    caption="When to monitor vs when to call the vet",
                    hotspots=["time-based-decision", "red-flags", "monitoring-checklist"]
                ),
                Diagram(
                    id="quick-checks-checklist",
                    asset_ref="not_eating_checklist",
                    alt="Quick checklist of things to verify before panicking",
                    caption="Pre-panic checklist: food freshness, bowl cleanliness, water intake",
                    hotspots=["food-quality", "environment-check", "symptom-check"]
                )
            ],
            do_list=["Warm food to room temp", "Try different textures", "Use flat plate", "Hand-feed tiny amounts"],
            dont_list=["Force feed", "Change brands constantly", "Leave wet food out all day", "Panic immediately"],
            updated_at=datetime.now()
        ),
        
        Guide(
            id="scratching-furniture",
            title="Scratching furniture: issue them a legal scratching licence",
            summary="How to redirect your kitten's natural need to scratch away from your sofa",
            markdown_body="""# Scratching Furniture: The Legal Licence System

## Why this matters
Scratching is not optional for cats. It's like telling you not to stretch in the morning. They HAVE to do it (sharpens claws, stretches muscles, marks territory). So don't try to stop it - redirect it.

## Scratching Post Setup Guide
```
    GOOD SCRATCHING POST ✅        BAD SCRATCHING POST ❌
    
         🐱                              🐱
        ┌──┐                            ┌──┐
    >>> │  │ <<< Rough texture     Smooth│  │ (too smooth)
    >>> │  │ <<< (sisal/cardboard)      │  │
    >>> │██│ <<< TALL (75cm+)      SHORT│▓▓│ (only 30cm)
    >>> │██│     Kitten can stretch     │▓▓│ Can't stretch
    >>> │██│                             └──┘
    >>> │██│                         Wobbles!
        │██│ <<< STURDY base            ○ 
        └══┴═════ Wide base          Tiny base
         Heavy                       Falls over

    PLACEMENT STRATEGY:
    
    ❌ Hidden in corner → No one will see my scratching!
    ✅ Near sofa        → Perfect! High traffic area!
    ✅ By sleep spot    → Wake up, scratch, stretch!
    ✅ By window        → Territory marker visible!
    
    MULTI-POST LAYOUT (ideal):
    Living room: Tall sisal post near sofa
    Bedroom: Flat cardboard scratcher near bed
    Hallway: Vertical post by door
    
    = Kitten has options everywhere
```

## Furniture Protection Methods
```
    SOFA CORNER PROTECTION:
    
    Before (being destroyed):      After (protected):
    ┌────────┐                     ┌────────┐
    │ ╱╱╱╱╱  │ Claw marks          │ 📎Foil │ Unpleasant
    │╱╱╱╱╱   │                     │ or     │ texture
    │╱╱      │                     │ 📦Tape │ deters cat
    └─────────┘                     └────────┘
                                        +
                                    [POST] ← Nearby
                                    Alternative
```

## Do this now (if you're panicking)
1. **Get a scratching post ASAP** - tall, sturdy, rough texture (sisal or cardboard)
2. **Put it where they're already scratching** (yes, next to the sofa they're destroying)
3. **Make the sofa less appealing** - cover with foil, double-sided tape, or a throw
4. **Praise them when they use the post** - treats, soft voice, gentle stroke

## Why they're doing it
- **Claw maintenance**: Removes dead outer claw sheaths (like you cutting your nails)
- **Territory marking**: Visual + scent markers (there are scent glands in their paws)
- **Stretching**: Feels good after a nap (cats are basically yogis)
- **Excitement**: "I'm happy and I must SCRATCH THE THING"

## Do
- ✅ Provide multiple scratching posts (different rooms, different heights)
- ✅ Use sturdy posts (if it wobbles, they'll ignore it)
- ✅ Try different textures (sisal, cardboard, carpet, wood)
- ✅ Place posts near sleep spots (first thing after waking = stretch time)
- ✅ Trim claws every 2-3 weeks (less damage when they rebel)

## Don't
- ❌ Punish after the fact (they won't connect it)
- ❌ Declaw (IT'S AMPUTATION. Illegal in the UK for good reason)
- ❌ Use cheap wobbly posts (waste of money)
- ❌ Hide the post in a corner (they want to scratch in social areas)
- ❌ Give up after 2 days (retraining takes 2-3 weeks)

## If you're stuck
**Kitten ignores expensive scratching post**: Is it tall enough? Sturdy enough? Right texture? Try sprinkling catnip on it. Move it to where they actually scratch.
**Only scratches one specific sofa corner**: Put a scratching post RIGHT THERE. Yes, it looks naff. Your sofa looking like a crime scene also looks naff.
**Scratches at night**: They're bored. Play session before bed to tire them out.

## The relocation method (once they're trained)
1. Put post where they scratch (even if it's your living room centre)
2. Wait until they reliably use it (1-2 weeks)
3. Move it 2 inches per day towards where you want it
4. Patience, human

## Human analogy
Imagine you HAD to stretch when you woke up, and someone put the only stretching spot in the garage. You'd just stretch in the bedroom anyway. Cats are the same - they'll scratch where it's convenient and socially relevant.

## Red flags - ring vet NOW
- 🔴 Claws bleeding or broken
- 🔴 Excessive scratching themselves (could be fleas, allergies, stress)
- 🔴 Limping after scratching (could be claw injury)
""",
            topics=["Behaviour", "Enrichment"],
            age_min_weeks=8,
            age_max_weeks=52,
            urgency="",
            analogy_cards=["Issue them a legal scratching licence - they're going to scratch, so give them the right paperwork"],
            diagrams=[
                Diagram(
                    id="good-vs-bad-post",
                    asset_ref="scratching_post_comparison",
                    alt="Comparison of good scratching post vs bad scratching post features",
                    caption="Tall, sturdy, rough texture = success. Short, wobbly, smooth = ignored.",
                    hotspots=["height-requirement", "stability", "texture-types"]
                ),
                Diagram(
                    id="post-placement-strategy",
                    asset_ref="post_placement_guide",
                    alt="Optimal placement locations for scratching posts around the home",
                    caption="Place posts where they already scratch and in high-traffic areas",
                    hotspots=["near-sofa", "by-sleep-spot", "traffic-areas"]
                ),
                Diagram(
                    id="furniture-protection",
                    asset_ref="furniture_protection_methods",
                    alt="Methods to protect furniture while training kitten to use post",
                    caption="Temporary protection: foil, tape, or throw blankets",
                    hotspots=["foil-tape-method", "alternative-nearby"]
                )
            ],
            do_list=["Get tall sturdy post", "Put where they scratch", "Praise when they use it", "Trim claws every 2-3 weeks"],
            dont_list=["Punish after the fact", "Declaw", "Use cheap wobbly posts", "Hide post in corner"],
            updated_at=datetime.now()
        ),
        
        Guide(
            id="zoomies-2am",
            title="Zoomies at 2am: negotiate an energy budget and bedtime ritual",
            summary="How to convince your kitten that 3am is not parkour practice time",
            markdown_body="""# Zoomies at 2am: The Energy Budget Negotiation

## Why this matters
Cats are crepuscular (active at dawn and dusk). Your kitten's body is telling them that 2am is PRIME HUNTING TIME. Your body is telling you that 2am is SLEEP TIME. Someone has to compromise, and it won't be the cat unless you're strategic.

## Bedtime Energy Management
```
    24-HOUR ENERGY CYCLE:
    
    Your schedule:        Kitten's natural instinct:
    
    7am  Wake up          💤 Sleeping (post-dawn hunt)
    12pm Working          💤 Sleeping  
    6pm  Tired            ⚡ WAKING UP (dusk = hunt time!)
    10pm Bedtime          ⚡ PEAK ENERGY!
    2am  SLEEPING         ⚡⚡⚡ ZOOMIES TIME!!!
    6am  Alarm            ⚡ Still going...
    
    THE FIX: Shift their energy peak earlier
    
    8pm  → Play session (15-20 min) = Tire them out
    9pm  → Small meal = Full tummy  
    10pm → Lights dim, calm = Sleep signals
    2am  → 💤 Sleeping (hopefully)
```

## Bedtime Protocol Flowchart
```
    1 hour before YOUR bedtime
            ↓
    ┌───────────────────────┐
    │ ACTIVE PLAY SESSION   │
    │ 15-20 minutes         │
    │ Use wand toys         │
    │ Make them RUN         │
    └───────────────────────┘
            ↓
    Hunt → Catch → Eat pattern
            ↓
    30 minutes before bed
            ↓
    ┌───────────────────────┐
    │ SMALL MEAL            │
    │ or big treat          │
    │ Full belly = sleepy   │
    └───────────────────────┘
            ↓
    ┌───────────────────────┐
    │ CALM ENVIRONMENT      │
    │ Dim lights            │
    │ Quiet voices          │
    └───────────────────────┘
            ↓
    Your bedtime → Door shut
            ↓
    Kitten screaming?
      ↓           ↓
    IGNORE!    DO NOT ENGAGE
      ↓
    Takes 3-7 days consistency
      ↓
    Success! Sleepy kitten 💤
```

## Do this now (if you're panicking)
1. **Ignore them** - do not engage, do not throw things, do not shout (attention = reward)
2. **Keep bedroom door shut** - they'll yell for a bit, then give up (usually)
3. **Tire them out before bed** - 15-20 minute play session before YOUR bedtime
4. **Feed them before YOUR bed** - full tummy = sleepy kitten

## Why they're doing it
- **Natural instinct**: Cats hunt at dawn/dusk (your 2am is their dusk)
- **Boredom**: They slept all day, now they're READY
- **Learned behaviour**: You've previously given attention (even negative attention)
- **Excess energy**: They're basically toddlers on espresso

## Do
- ✅ Establish bedtime routine (play, small meal, settle down)
- ✅ Tire them out with interactive play (wand toys, laser pointer + physical toy to catch)
- ✅ Puzzle feeders before bed (mental stimulation)
- ✅ Block under-bed access (common zoomie racetrack)
- ✅ Earplugs (for you, not them)

## Don't
- ❌ Feed them when they wake you (trains them to wake you for food)
- ❌ Play with them at 2am (trains them that 2am = playtime)
- ❌ Shout or spray water (creates fear, not sleep)
- ❌ Lock them away without preparation (they'll scream)
- ❌ Expect it to change overnight (takes 2-3 weeks of consistency)

## The bedtime protocol
**1 hour before your bedtime:**
- Play session: 15-20 minutes, tire them out properly
- Hunt (play), catch (give them toy to "kill"), eat (small meal), groom (they'll do this), sleep (hopefully)

**30 minutes before bed:**
- Small meal or big treat
- Calm environment, dim lights

**At your bedtime:**
- Bedroom door shut, earplugs in, ignore all noise

## If you're stuck
**Kitten screams at door all night**: They'll stop after 3-7 days if you never give in. NEVER GIVE IN. Giving in at 4am teaches them "scream for 2 hours = door opens".
**Kitten races around bedroom**: Remove all toys from bedroom, block under furniture, consider baby gate instead of shut door (they can see you, less panic).
**Kitten attacks your feet under duvet**: Thick blanket, or shut them out. This is war.

## Human analogy
Imagine your flatmate woke you at 2am to play football because THEY'RE not tired. You'd be furious. Your kitten doesn't understand human sleep schedules - you have to teach them.

## Red flags - ring vet NOW
- 🔴 Sudden zoomies with yowling (could be pain)
- 🔴 Zoomies after using litter tray (could be UTI or constipation pain)
- 🔴 Zoomies with excessive drinking (could be diabetes or kidney issues - rare in kittens but possible)
""",
            topics=["Behaviour", "Sleep", "Play"],
            age_min_weeks=8,
            age_max_weeks=52,
            urgency="",
            analogy_cards=["Negotiate an energy budget - they have 100 units, make sure they spend them before midnight"],
            diagrams=[
                Diagram(
                    id="energy-cycle-comparison",
                    asset_ref="cat_human_energy_cycles",
                    alt="Comparison of human sleep schedule vs kitten natural energy peaks",
                    caption="Your 2am is their prime time - shift their peak earlier",
                    hotspots=["crepuscular-pattern", "schedule-mismatch", "energy-shift"]
                ),
                Diagram(
                    id="bedtime-protocol-flow",
                    asset_ref="bedtime_routine_flowchart",
                    alt="Step-by-step bedtime protocol flowchart for tiring out kitten",
                    caption="Hunt → Catch → Eat → Sleep pattern for peaceful nights",
                    hotspots=["play-timing", "feeding-timing", "consistency"]
                )
            ],
            do_list=["Tire them out before bed", "Feed before bed", "Ignore nighttime activity", "Block under-bed access"],
            dont_list=["Feed when they wake you", "Play at 2am", "Shout or spray water", "Give in to screaming"],
            updated_at=datetime.now()
        ),
        
        Guide(
            id="preparing-arrival",
            title="Preparing for kitten arrival: turn your flat into a five-star cattery",
            summary="Supply checklist with handy links and a calm room layout so day-one feels like a holiday, not a hostage situation",
            markdown_body="""# Preparing for Kitten Arrival: Five-Star Cattery Setup

## Why this matters
First impressions stick. A kitten who lands in chaos will associate you with chaos. A kitten who lands in a cosy, prepped base camp will think "Ah, my new staff have taste."

## Shopping list with quick links
- [Litter tray](https://amzn.to/4pAAnEJ) — big enough for them to turn comfortably
- [Litter](https://amzn.to/49vJCBz) — unscented, clumping so scooping is easy
- [Kitten food](https://amzn.to/49TqoFQ) — age-appropriate fuel
- Food & water bowls — shallow, whisker-friendly
- Cat carrier — top-opening if possible (feels less like a prison van)
- Snuggly bed or box with blanket (bonus points: your worn t-shirt)
- Scratching post and a couple of toys (wand toy + cardboard scratcher)

## Room layout cheat (base camp)
```
    DOOR
    ┌────────────────────────┐
    │ 👕 Scented bed          │
    │ (your t-shirt)         │
    │                        │
    │            💧 Water    │
    │            🍽️ Food     │
    │                        │
    │ 🚽 Litter tray (far    │
    │ from food)             │
    │                        │
    │ 📦 Cardboard box hide  │
    └────────────────────────┘
```

## Do this now (if you're panicking)
1. Choose the calmest room as base camp; close windows/under-bed gaps.
2. Place [litter tray](https://amzn.to/4pAAnEJ) and [litter](https://amzn.to/49vJCBz) in the furthest corner from food.
3. Set out [kitten food](https://amzn.to/49TqoFQ) and water in shallow bowls.
4. Lay out the carrier as an open den with blanket inside.
5. Add your worn t-shirt to the bed (instant comfort cheat code).

## Do
- ✅ Keep everything in one room for the first 24-48 hours
- ✅ Show them the tray and the bowls calmly, then sit and ignore them
- ✅ Use night-light or dim lamp so they can navigate at night
- ✅ Keep carrier accessible so it feels like a cosy cave, not a kidnap box

## Don't
- ❌ Move the litter tray daily (consistency prevents accidents)
- ❌ Introduce the whole house on day one
- ❌ Light scented candles or use strong cleaners (their nose is better than yours)
- ❌ Chase them to cuddle; let them make the first move

## Human analogy
Imagine checking into a hotel where the bed is made with your favourite jumper, the bathroom is spotless, and room service already knows your order. That's the vibe.

## Red flags - ring vet NOW
- 🔴 Arrives lethargic, unresponsive, or breathing oddly
- 🔴 Vomiting/diarrhoea in the first hours (could be travel stress, could be more)
- 🔴 Not drinking within 12 hours of arrival
""",
            topics=["Onboarding", "Litter", "Feeding"],
            age_min_weeks=0,
            age_max_weeks=24,
            urgency="",
            analogy_cards=["Prep like you're hosting a very small, very judgey celebrity."],
            diagrams=[],
            do_list=["Keep base camp contained", "Use unscented litter", "Make carrier a den", "Add your scent to bedding"],
            dont_list=["Move litter tray around", "Overwhelm with full-house tour", "Use strong scents", "Force cuddles"],
            updated_at=datetime.now()
        ),
        
        Guide(
            id="carrier-training",
            title="Carrier training: turn the cat carrier into a cosy spaceship",
            summary="Make the carrier a safe nap pod so vet trips feel like a taxi, not a kidnap",
            markdown_body="""# Carrier Training: The Cosy Spaceship Protocol

## Why this matters
Emergencies are not the time to discover your kitten thinks the carrier is a dragon's mouth. Teach them now that the box = bed on wheels.

## Setup in 10 minutes
1. Leave the carrier out permanently, door open.
2. Put a soft blanket + your t-shirt inside.
3. Sprinkle a few treats or a pinch of catnip in there daily.
4. Feed one snack a day inside the carrier (door still open).

## Upgrade to door practice
- Start closing the door for 5-10 seconds while they eat, then open and praise.
- Gradually extend to 1-2 minutes with you nearby.
- Pick the carrier up, set it down, treat. Repeat until boring.

## Travel dress rehearsal
```
    Door open → Treats inside → Door closed 20s → Lift & set down → Treat
    Repeat 3-4 times a week until they roll their eyes at you.
```

## Do
- ✅ Keep the carrier visible and inviting daily
- ✅ Use top-loading carriers for easier, calmer loading
- ✅ Practice tiny car rides when they're calm, not when late for vet
- ✅ Line with puppy pad for travel days (in case of nervous wee)

## Don't
- ❌ Only bring carrier out for vet day (guaranteed panic association)
- ❌ Chase them into it; lure with treats or drop a trail of biscuits
- ❌ Lock them in for long periods "to get them used to it"
- ❌ Forget to secure the carrier with a seatbelt in the car

## Human analogy
Imagine if your only experience of cars was being shoved into one while ill. You'd hate cars. Make the carrier their cosy taxi, not a prison van.

## Red flags - ring vet NOW
- 🔴 Panting, drooling, or open-mouth breathing in the carrier
- 🔴 Sudden refusal to walk, collapse, or extreme distress
- 🔴 Vomiting repeatedly during short practice trips
""",
            topics=["Behaviour", "Health", "Emergency"],
            age_min_weeks=0,
            age_max_weeks=52,
            urgency="",
            analogy_cards=["Think of the carrier as a cat-sized spaceship: engines on, blankets ready, destination: vet without drama."],
            diagrams=[],
            do_list=["Leave carrier out daily", "Practice short closures", "Reward calm loading", "Secure carrier in car"],
            dont_list=["Only use carrier for vet days", "Force them inside", "Skip practice lifts", "Travel without lining"],
            updated_at=datetime.now()
        ),
        
        Guide(
            id="emergency-vet-now",
            title="When to call a vet NOW - emergency card",
            summary="Clear red flags that mean immediate vet attention required",
            markdown_body="""# When to Call a Vet NOW 🔴

This is not a complete list. When in doubt, ring your vet. They'd rather you called unnecessarily than waited too long.

## Emergency Quick Reference Chart
```
    SYMPTOM                          TIMEFRAME        ACTION
    ═══════════════════════════════════════════════════════════
    
    🫁 Difficulty breathing          IMMEDIATELY      VET NOW
    💙 Pale/blue gums                IMMEDIATELY      VET NOW
    🚫 No urine 12+ hours            IMMEDIATELY      VET NOW
    🩸 Blood anywhere                IMMEDIATELY      VET NOW
    💤 Unresponsive/collapse         IMMEDIATELY      VET NOW
    🤮 Repeated vomiting             IMMEDIATELY      VET NOW
    🌡️ Very cold/hot                 IMMEDIATELY      VET NOW
    ☠️ Possible poisoning            IMMEDIATELY      VET NOW
    
    💧 No drinking 12+ hours         CALL VET NOW
    🍽️ No eating 24+ hours          CALL VET NOW
    😾 Sudden aggression             CALL VET NOW
    👁️ Eye injury/swelling           CALL VET NOW
    🤕 Fall from height              CALL VET NOW
    
    WHEN IN DOUBT → RING VET
```

## Urgency Level Guide
```
    🔴 RED = VET NOW (0-30 minutes)
    ├─ Can't breathe properly
    ├─ Can't urinate (straining with nothing)
    ├─ Collapsed/unresponsive
    ├─ Suspected poisoning
    └─ Severe bleeding
    
    🟠 ORANGE = VET TODAY (within hours)
    ├─ Not eating 24+ hours
    ├─ Not drinking 12+ hours
    ├─ Repeated vomiting
    ├─ Severe diarrhoea
    └─ Sudden behaviour change
    
    🟡 YELLOW = MONITOR & VET SOON (next day)
    ├─ Not eating 12-24 hours
    ├─ Single vomit (but otherwise OK)
    ├─ Sneezing (but eating/playing)
    └─ Minor scratches (no swelling)
```

## Common UK Kitten Poisons ☠️
```
    EXTREMELY TOXIC:             TOXIC:
    ✗ Lilies (all parts)         ✗ Chocolate
    ✗ Paracetamol               ✗ Onions/garlic
    ✗ Essential oils             ✗ Grapes/raisins
    ✗ Antifreeze                ✗ Xylitol (sugar-free)
    
    ONE DOSE CAN KILL A KITTEN
    ↓
    CALL VET IMMEDIATELY
    (Even if they seem fine now)
```

## Ring vet IMMEDIATELY if:

### Breathing & circulation
- 🔴 **Difficulty breathing** or panting (cats don't pant unless in distress)
- 🔴 **Pale or blue gums**
- 🔴 **Rapid breathing at rest** (normal is 20-30 breaths per minute)
- 🔴 **Weak pulse or cold extremities**

### Eating & drinking
- 🔴 **No drinking for 12+ hours** (dehydration is fast in kittens)
- 🔴 **No eating for 24+ hours**
- 🔴 **Repeated vomiting** (more than twice in 24 hours)
- 🔴 **Bloody vomit**

### Toilet troubles
- 🔴 **No urine for 12+ hours** or **straining to urinate with nothing coming out** (URGENT - can be fatal)
- 🔴 **Blood in urine or stool**
- 🔴 **Severe diarrhoea** (especially if lethargic too)
- 🔴 **Crying or straining in litter tray**

### Behaviour & consciousness
- 🔴 **Completely limp, unresponsive, or collapse**
- 🔴 **Seizures or fitting**
- 🔴 **Extreme lethargy** (won't wake properly, won't respond to stimuli)
- 🔴 **Sudden aggression** from a previously calm kitten (could be pain)

### Injuries & poisoning
- 🔴 **Any injury from a fall** (especially from height)
- 🔴 **Hit by car** (even if seems OK - internal injuries)
- 🔴 **Possible poisoning** (ate lilies, paracetamol, chocolate, cleaning products, anything toxic)
- 🔴 **Bite from another animal** (infection risk)
- 🔴 **Swallowed string, ribbon, tinsel** (can cause fatal intestinal damage)

### Temperature
- 🔴 **Very cold** (ears, paws feel like ice)
- 🔴 **Very hot** (fever - normal temp is 38-39°C / 100.5-102.5°F)

### Eyes & ears
- 🔴 **Sudden blindness**
- 🔴 **Eye injury or extreme swelling**
- 🔴 **Continuous head tilting** (could be ear infection or neurological)

## What to say when you ring
Keep this info handy:
- Kitten's age and weight
- When symptoms started
- What they've eaten/drunk in last 24 hours
- Any known medical history
- Vaccination status
- What the emergency is (be specific)

## What to do while waiting
- **Keep them warm** (wrapped in towel, not hot water bottle)
- **Keep them calm** (quiet, dark, no fuss)
- **Don't give food or water** if vet says not to
- **Bring them in a secure carrier** (not loose in car)
- **Bring any packaging** if suspected poisoning

## Common UK kitten poisons
- **Lilies** (all parts, even pollen - EXTREMELY TOXIC)
- **Paracetamol** (one tablet can kill a kitten)
- **Ibuprofen**
- **Chocolate** (especially dark)
- **Onions, garlic, chives**
- **Grapes and raisins**
- **Xylitol** (sugar-free gum, peanut butter)
- **Essential oils** (especially tea tree)
- **Antifreeze** (tastes sweet, highly lethal)
- **Household cleaners**
- **String, ribbon, tinsel** (not poison but can kill)

## After hours
Most vets have an emergency number. It will be on their answerphone. If not:
- **PDSA** (if you qualify): 0800 731 2502
- **Vets Now** (emergency provider): google "Vets Now near me"
- **RSPCA advice**: 0300 1234 999 (not emergency vet, but can advise)

## The golden rule
**If you think "should I ring the vet?", the answer is YES.**

Vets would rather you called. You will not be wasting their time. Kittens can deteriorate FAST. Trust your instincts.
""",
            topics=["Health", "Emergency"],
            age_min_weeks=0,
            age_max_weeks=52,
            urgency="Now",
            analogy_cards=["When in doubt, ring. Vets prefer false alarms to too late."],
            diagrams=[
                Diagram(
                    id="emergency-quick-reference",
                    asset_ref="emergency_symptoms_chart",
                    alt="Quick reference chart of emergency symptoms and required response times",
                    caption="Symptom → Timeframe → Action guide",
                    hotspots=["immediate-symptoms", "urgent-symptoms", "monitor-symptoms"]
                ),
                Diagram(
                    id="urgency-levels",
                    asset_ref="urgency_level_guide",
                    alt="Three-tier urgency system: Red (now), Orange (today), Yellow (soon)",
                    caption="Red = 0-30 min | Orange = hours | Yellow = next day",
                    hotspots=["red-flags", "orange-flags", "yellow-flags"]
                ),
                Diagram(
                    id="common-poisons",
                    asset_ref="uk_kitten_poisons_chart",
                    alt="Visual list of common UK household poisons toxic to kittens",
                    caption="Lilies, paracetamol, essential oils - one dose can kill",
                    hotspots=["extremely-toxic", "toxic", "poison-response"]
                )
            ],
            do_list=["Have vet number saved", "Know out-of-hours emergency number", "Trust your instincts", "Keep kitten warm and calm"],
            dont_list=["Wait to see if it gets better", "Google for hours instead of calling", "Give human medicine", "Panic - act calmly"],
            updated_at=datetime.now()
        ),
    ]
    
    # Add all guides to database
    for guide in guides:
        db.add_guide(guide)
    
    print(f"✅ Loaded {len(guides)} sample guides into database")
