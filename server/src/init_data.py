"""
Initialize database with game objects and scoring systems
Run this script to populate the database with initial data
"""
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import GameObject, ScoringSystem

# Create all tables
Base.metadata.create_all(bind=engine)


def init_scoring_systems(db: Session):
    """Initialize the 10 scoring systems"""
    scoring_systems = [
        {
            "name": "nutritional_value",
            "display_name": "Nutritional Value",
            "description": "How healthy is this concoction?",
            "unit": "vitamins",
            "icon": "🥗",
            "visible_from_start": True
        },
        {
            "name": "impossibility_index",
            "display_name": "Impossibility Index",
            "description": "How physically impossible is this blend?",
            "unit": "paradoxes",
            "icon": "🌀",
            "visible_from_start": False
        },
        {
            "name": "awful_colour",
            "display_name": "Awful Colour",
            "description": "How visually disturbing is this mixture?",
            "unit": "yikes",
            "icon": "🎨",
            "visible_from_start": False
        },
        {
            "name": "deep_lore",
            "display_name": "Deep Lore",
            "description": "How much forbidden knowledge does this contain?",
            "unit": "secrets",
            "icon": "📜",
            "visible_from_start": False
        },
        {
            "name": "gift_quality",
            "display_name": "Would Make a Good Gift",
            "description": "Would you give this to someone you care about?",
            "unit": "regrets avoided",
            "icon": "🎁",
            "visible_from_start": False
        },
        {
            "name": "chaos_energy",
            "display_name": "Chaos Energy",
            "description": "Raw chaotic potential emanating from the blend",
            "unit": "entropy units",
            "icon": "⚡",
            "visible_from_start": False
        },
        {
            "name": "temporal_displacement",
            "display_name": "Temporal Displacement",
            "description": "How much does this bend the fabric of time?",
            "unit": "chrono-wobbles",
            "icon": "⏰",
            "visible_from_start": False
        },
        {
            "name": "existential_dread",
            "display_name": "Existential Dread",
            "description": "How much does this make you question reality?",
            "unit": "void stares",
            "icon": "👁️",
            "visible_from_start": False
        },
        {
            "name": "aesthetic_vibes",
            "display_name": "Aesthetic Vibes",
            "description": "Pure vibes radiating from this blend",
            "unit": "vibes",
            "icon": "✨",
            "visible_from_start": False
        },
        {
            "name": "forbidden_power",
            "display_name": "Forbidden Power",
            "description": "Ancient power that mortals should not possess",
            "unit": "elder souls",
            "icon": "🔮",
            "visible_from_start": False
        }
    ]

    for system_data in scoring_systems:
        existing = db.query(ScoringSystem).filter(
            ScoringSystem.name == system_data["name"]
        ).first()
        if not existing:
            system = ScoringSystem(**system_data)
            db.add(system)

    db.commit()
    print(f"✓ Initialized {len(scoring_systems)} scoring systems")


def init_game_objects(db: Session):
    """Initialize game objects with their scores and unlock thresholds"""
    game_objects = [
        # Starting objects (unlock_threshold = 0)
        {
            "name": "Apple",
            "category": "fruit",
            "unlock_threshold": 0,
            "sprite_path": "/sprites/apple.svg",
            "description": "A crisp red apple. Classic.",
            "rarity": "common",
            "color": "#DC143C",  # Crimson red
            "scores": {
                "nutritional_value": 15.5
            }
        },
        {
            "name": "Banana",
            "category": "fruit",
            "unlock_threshold": 0,
            "sprite_path": "/sprites/banana.svg",
            "description": "A yellow banana. Full of potassium.",
            "rarity": "common",
            "color": "#FFE135",  # Banana yellow
            "scores": {
                "nutritional_value": 18.2
            }
        },
        {
            "name": "Carrot",
            "category": "vegetable",
            "unlock_threshold": 0,
            "sprite_path": "/sprites/carrot.svg",
            "description": "An orange carrot. Good for your eyes.",
            "rarity": "common",
            "color": "#FF8C00",  # Dark orange
            "scores": {
                "nutritional_value": 12.7
            }
        },
        {
            "name": "Strawberry",
            "category": "fruit",
            "unlock_threshold": 0,
            "sprite_path": "/sprites/strawberry.svg",
            "description": "Sweet and red.",
            "rarity": "common",
            "color": "#FF0800",  # Bright red
            "scores": {
                "nutritional_value": 14.3,
                "aesthetic_vibes": 5.5
            }
        },
        {
            "name": "Broccoli",
            "category": "vegetable",
            "unlock_threshold": 0,
            "sprite_path": "/sprites/broccoli.svg",
            "description": "Little trees of nutrition.",
            "rarity": "common",
            "color": "#228B22",  # Forest green
            "scores": {
                "nutritional_value": 21.8,
                "awful_colour": 3.2
            }
        },

        # Unlock after 2 blends
        {
            "name": "Rubber Duck",
            "category": "absurd",
            "unlock_threshold": 2,
            "sprite_path": "/sprites/rubber_duck.svg",
            "description": "Squeaks when compressed. Not edible.",
            "rarity": "uncommon",
            "color": "#FFD700",  # Gold/yellow
            "scores": {
                "impossibility_index": 42.7,
                "awful_colour": 8.9,
                "chaos_energy": 12.3
            }
        },
        {
            "name": "Old Boot",
            "category": "absurd",
            "unlock_threshold": 2,
            "sprite_path": "/sprites/old_boot.svg",
            "description": "Someone's been walking in this.",
            "rarity": "uncommon",
            "color": "#8B4513",  # Saddle brown
            "scores": {
                "impossibility_index": 38.4,
                "awful_colour": 15.6,
                "gift_quality": -22.0
            }
        },

        # Unlock after 4 blends
        {
            "name": "Ancient Scroll",
            "category": "magical",
            "unlock_threshold": 4,
            "sprite_path": "/sprites/ancient_scroll.svg",
            "description": "Contains forbidden knowledge from a lost civilization.",
            "rarity": "rare",
            "color": "#F5DEB3",  # Parchment/wheat
            "scores": {
                "deep_lore": 87.3,
                "impossibility_index": 55.1,
                "temporal_displacement": 31.8,
                "existential_dread": 12.7
            }
        },
        {
            "name": "Cloud Fragment",
            "category": "magical",
            "unlock_threshold": 4,
            "sprite_path": "/sprites/cloud_fragment.svg",
            "description": "A piece of cloud, somehow solid.",
            "rarity": "rare",
            "color": "#E0F6FF",  # Light sky blue
            "scores": {
                "impossibility_index": 91.2,
                "aesthetic_vibes": 23.4,
                "chaos_energy": 18.9
            }
        },

        # Unlock after 6 blends
        {
            "name": "Bottled Scream",
            "category": "absurd",
            "unlock_threshold": 6,
            "sprite_path": "/sprites/bottled_scream.svg",
            "description": "Someone's eternal anguish, preserved in glass.",
            "rarity": "rare",
            "color": "#4B0082",  # Indigo/deep purple
            "scores": {
                "existential_dread": 67.9,
                "chaos_energy": 44.2,
                "gift_quality": -88.3,
                "awful_colour": 12.1
            }
        },
        {
            "name": "Vintage Telephone",
            "category": "absurd",
            "unlock_threshold": 6,
            "sprite_path": "/sprites/vintage_telephone.svg",
            "description": "It still rings sometimes. Nobody's on the other end.",
            "rarity": "uncommon",
            "color": "#2F4F4F",  # Dark slate gray
            "scores": {
                "temporal_displacement": 44.7,
                "deep_lore": 22.8,
                "impossibility_index": 35.6
            }
        },

        # Unlock after 8 blends
        {
            "name": "Philosopher's Stone",
            "category": "magical",
            "unlock_threshold": 8,
            "sprite_path": "/sprites/philosophers_stone.svg",
            "description": "Turns lead into gold. Probably.",
            "rarity": "epic",
            "color": "#B8860B",  # Dark goldenrod
            "scores": {
                "forbidden_power": 156.8,
                "deep_lore": 92.4,
                "impossibility_index": 77.3,
                "gift_quality": 103.5
            }
        },
        {
            "name": "Miniature Sun",
            "category": "magical",
            "unlock_threshold": 8,
            "sprite_path": "/sprites/miniature_sun.svg",
            "description": "Pocket-sized solar fusion. Handle with care.",
            "rarity": "epic",
            "color": "#FFA500",  # Orange
            "scores": {
                "chaos_energy": 198.7,
                "impossibility_index": 143.2,
                "awful_colour": 89.4,
                "temporal_displacement": 55.1
            }
        },

        # Unlock after 10 blends
        {
            "name": "Expired Coupon",
            "category": "absurd",
            "unlock_threshold": 10,
            "sprite_path": "/sprites/expired_coupon.svg",
            "description": "Missed savings opportunities haunt this paper.",
            "rarity": "uncommon",
            "color": "#D3D3D3",  # Light gray
            "scores": {
                "existential_dread": 91.3,
                "temporal_displacement": 67.8,
                "gift_quality": -45.2
            }
        },
        {
            "name": "Dream Catcher",
            "category": "magical",
            "unlock_threshold": 10,
            "sprite_path": "/sprites/dream_catcher.svg",
            "description": "Still has someone's dreams tangled in it.",
            "rarity": "rare",
            "color": "#D2691E",  # Chocolate/tan
            "scores": {
                "aesthetic_vibes": 78.9,
                "deep_lore": 44.5,
                "existential_dread": 23.7,
                "chaos_energy": 31.2
            }
        },

        # Unlock after 12 blends
        {
            "name": "Void Marble",
            "category": "magical",
            "unlock_threshold": 12,
            "sprite_path": "/sprites/void_marble.svg",
            "description": "Stare into it and it stares back. Forever.",
            "rarity": "legendary",
            "color": "#1A0033",  # Deep void purple
            "scores": {
                "existential_dread": 234.6,
                "forbidden_power": 189.3,
                "chaos_energy": 156.8,
                "temporal_displacement": 98.7,
                "impossibility_index": 167.9
            }
        },
        {
            "name": "Crystallized Laughter",
            "category": "magical",
            "unlock_threshold": 12,
            "sprite_path": "/sprites/crystallized_laughter.svg",
            "description": "Pure joy, frozen in time.",
            "rarity": "legendary",
            "color": "#FFB6C1",  # Light pink
            "scores": {
                "aesthetic_vibes": 198.4,
                "temporal_displacement": 87.2,
                "gift_quality": 156.7,
                "chaos_energy": 67.3,
                "impossibility_index": 134.5
            }
        },

        # More variety at different unlock levels
        {
            "name": "Kale",
            "category": "vegetable",
            "unlock_threshold": 1,
            "sprite_path": "/sprites/kale.svg",
            "description": "Trendy superfood.",
            "rarity": "common",
            "color": "#355E3B",  # Dark green
            "scores": {
                "nutritional_value": 28.9,
                "awful_colour": 4.2
            }
        },
        {
            "name": "Mango",
            "category": "fruit",
            "unlock_threshold": 1,
            "sprite_path": "/sprites/mango.svg",
            "description": "Tropical sweetness.",
            "rarity": "common",
            "color": "#FF8243",  # Mango orange
            "scores": {
                "nutritional_value": 19.6,
                "aesthetic_vibes": 8.3
            }
        },
        {
            "name": "Sock (Single)",
            "category": "absurd",
            "unlock_threshold": 3,
            "sprite_path": "/sprites/single_sock.svg",
            "description": "Its partner is lost to the dryer dimension.",
            "rarity": "uncommon",
            "color": "#808080",  # Gray
            "scores": {
                "existential_dread": 34.2,
                "temporal_displacement": 23.8,
                "impossibility_index": 28.4
            }
        },
        {
            "name": "Parking Ticket",
            "category": "absurd",
            "unlock_threshold": 5,
            "sprite_path": "/sprites/parking_ticket.svg",
            "description": "Still owe $45 for this.",
            "rarity": "uncommon",
            "color": "#FFF8DC",  # Cornsilk/pale yellow
            "scores": {
                "existential_dread": 56.7,
                "gift_quality": -67.8,
                "chaos_energy": 22.1
            }
        },
        {
            "name": "Fairy Dust",
            "category": "magical",
            "unlock_threshold": 7,
            "sprite_path": "/sprites/fairy_dust.svg",
            "description": "Makes you believe... in allergies.",
            "rarity": "rare",
            "color": "#DA70D6",  # Orchid/sparkly purple
            "scores": {
                "aesthetic_vibes": 89.3,
                "chaos_energy": 44.7,
                "impossibility_index": 67.2,
                "gift_quality": 45.8
            }
        },
        {
            "name": "Tax Form",
            "category": "absurd",
            "unlock_threshold": 9,
            "sprite_path": "/sprites/tax_form.svg",
            "description": "The numbers refuse to add up.",
            "rarity": "uncommon",
            "color": "#F5F5F5",  # White smoke
            "scores": {
                "existential_dread": 187.9,
                "chaos_energy": 92.3,
                "awful_colour": 34.1
            }
        },

        # === TIER 1: Very Normal (0-5 blends) ===
        # More common fruits
        {
            "name": "Orange",
            "category": "fruit",
            "unlock_threshold": 0,
            "sprite_path": "/sprites/orange.svg",
            "description": "Citrus perfection.",
            "rarity": "common",
            "color": "#FFA500",
            "scores": {"nutritional_value": 16.8, "aesthetic_vibes": 4.2}
        },
        {
            "name": "Grapes",
            "category": "fruit",
            "unlock_threshold": 0,
            "sprite_path": "/sprites/grapes.svg",
            "description": "Purple or green, both are good.",
            "rarity": "common",
            "color": "#6F2DA8",
            "scores": {"nutritional_value": 13.5}
        },
        {
            "name": "Watermelon",
            "category": "fruit",
            "unlock_threshold": 1,
            "sprite_path": "/sprites/watermelon.svg",
            "description": "Mostly water, entirely delicious.",
            "rarity": "common",
            "color": "#FC6C85",
            "scores": {"nutritional_value": 11.2, "aesthetic_vibes": 6.7}
        },
        {
            "name": "Pineapple",
            "category": "fruit",
            "unlock_threshold": 1,
            "sprite_path": "/sprites/pineapple.svg",
            "description": "Tropical and spiky.",
            "rarity": "common",
            "color": "#FFE135",
            "scores": {"nutritional_value": 17.9, "aesthetic_vibes": 5.3}
        },
        {
            "name": "Blueberries",
            "category": "fruit",
            "unlock_threshold": 1,
            "sprite_path": "/sprites/blueberries.svg",
            "description": "Tiny blue superfoods.",
            "rarity": "common",
            "color": "#4169E1",
            "scores": {"nutritional_value": 22.3, "aesthetic_vibes": 7.8}
        },
        {
            "name": "Peach",
            "category": "fruit",
            "unlock_threshold": 2,
            "sprite_path": "/sprites/peach.svg",
            "description": "Fuzzy and sweet.",
            "rarity": "common",
            "color": "#FFE5B4",
            "scores": {"nutritional_value": 14.6, "aesthetic_vibes": 8.9}
        },
        {
            "name": "Pear",
            "category": "fruit",
            "unlock_threshold": 2,
            "sprite_path": "/sprites/pear.svg",
            "description": "Like an apple's sophisticated cousin.",
            "rarity": "common",
            "color": "#D1E231",
            "scores": {"nutritional_value": 15.3}
        },
        {
            "name": "Cherries",
            "category": "fruit",
            "unlock_threshold": 2,
            "sprite_path": "/sprites/cherries.svg",
            "description": "Sweet little red gems.",
            "rarity": "common",
            "color": "#DE3163",
            "scores": {"nutritional_value": 16.1, "aesthetic_vibes": 9.2}
        },
        # Common vegetables
        {
            "name": "Spinach",
            "category": "vegetable",
            "unlock_threshold": 1,
            "sprite_path": "/sprites/spinach.svg",
            "description": "Popeye's favorite.",
            "rarity": "common",
            "color": "#228B22",
            "scores": {"nutritional_value": 24.7, "awful_colour": 2.1}
        },
        {
            "name": "Tomato",
            "category": "vegetable",
            "unlock_threshold": 1,
            "sprite_path": "/sprites/tomato.svg",
            "description": "Technically a fruit, emotionally a vegetable.",
            "rarity": "common",
            "color": "#FF6347",
            "scores": {"nutritional_value": 13.8, "existential_dread": 1.2}
        },
        {
            "name": "Cucumber",
            "category": "vegetable",
            "unlock_threshold": 2,
            "sprite_path": "/sprites/cucumber.svg",
            "description": "Cool as a...",
            "rarity": "common",
            "color": "#9ACD32",
            "scores": {"nutritional_value": 9.7, "aesthetic_vibes": 3.4}
        },
        {
            "name": "Bell Pepper",
            "category": "vegetable",
            "unlock_threshold": 2,
            "sprite_path": "/sprites/bell_pepper.svg",
            "description": "Comes in rainbow colors.",
            "rarity": "common",
            "color": "#FF4500",
            "scores": {"nutritional_value": 18.4, "aesthetic_vibes": 6.1}
        },
        {
            "name": "Lettuce",
            "category": "vegetable",
            "unlock_threshold": 2,
            "sprite_path": "/sprites/lettuce.svg",
            "description": "Crunchy water leaves.",
            "rarity": "common",
            "color": "#7FFF00",
            "scores": {"nutritional_value": 8.2}
        },
        {
            "name": "Celery",
            "category": "vegetable",
            "unlock_threshold": 3,
            "sprite_path": "/sprites/celery.svg",
            "description": "Negative calories, positive crunch.",
            "rarity": "common",
            "color": "#7BA05B",
            "scores": {"nutritional_value": 7.9, "awful_colour": 1.8}
        },
        {
            "name": "Onion",
            "category": "vegetable",
            "unlock_threshold": 3,
            "sprite_path": "/sprites/onion.svg",
            "description": "Makes you cry, makes food better.",
            "rarity": "common",
            "color": "#E8D5C4",
            "scores": {"nutritional_value": 10.5, "existential_dread": 3.4}
        },
        {
            "name": "Garlic",
            "category": "vegetable",
            "unlock_threshold": 3,
            "sprite_path": "/sprites/garlic.svg",
            "description": "Vampire repellent.",
            "rarity": "common",
            "color": "#FFFACD",
            "scores": {"nutritional_value": 14.1, "deep_lore": 2.3}
        },
        # Basic kitchen items
        {
            "name": "Milk",
            "category": "beverage",
            "unlock_threshold": 3,
            "sprite_path": "/sprites/milk.svg",
            "description": "Does a body good, allegedly.",
            "rarity": "common",
            "color": "#FFFFF0",
            "scores": {"nutritional_value": 19.3, "awful_colour": 5.6}
        },
        {
            "name": "Coffee Beans",
            "category": "beverage",
            "unlock_threshold": 4,
            "sprite_path": "/sprites/coffee_beans.svg",
            "description": "The source of morning consciousness.",
            "rarity": "common",
            "color": "#3B2414",
            "scores": {"nutritional_value": 5.7, "chaos_energy": 8.3, "temporal_displacement": 4.2}
        },
        {
            "name": "Honey",
            "category": "food",
            "unlock_threshold": 4,
            "sprite_path": "/sprites/honey.svg",
            "description": "Bee vomit. Delicious bee vomit.",
            "rarity": "common",
            "color": "#FFC30B",
            "scores": {"nutritional_value": 12.4, "aesthetic_vibes": 11.2}
        },
        {
            "name": "Chocolate",
            "category": "food",
            "unlock_threshold": 4,
            "sprite_path": "/sprites/chocolate.svg",
            "description": "The food of love and happiness.",
            "rarity": "common",
            "color": "#7B3F00",
            "scores": {"nutritional_value": 8.9, "aesthetic_vibes": 15.6, "gift_quality": 12.3}
        },
        {
            "name": "Egg",
            "category": "food",
            "unlock_threshold": 5,
            "sprite_path": "/sprites/egg.svg",
            "description": "Potential chicken in a shell.",
            "rarity": "common",
            "color": "#F0EAD6",
            "scores": {"nutritional_value": 21.7, "existential_dread": 2.1}
        },
        {
            "name": "Cheese",
            "category": "food",
            "unlock_threshold": 5,
            "sprite_path": "/sprites/cheese.svg",
            "description": "Aged milk, somehow amazing.",
            "rarity": "common",
            "color": "#FFF8DC",
            "scores": {"nutritional_value": 16.8, "awful_colour": 7.3, "gift_quality": 8.7}
        },
        {
            "name": "Bread",
            "category": "food",
            "unlock_threshold": 5,
            "sprite_path": "/sprites/bread.svg",
            "description": "The staff of life.",
            "rarity": "common",
            "color": "#DEB887",
            "scores": {"nutritional_value": 13.2}
        },

        # === TIER 2: Still Normal but Expanding (6-12 blends) ===
        # Exotic fruits and vegetables
        {
            "name": "Dragon Fruit",
            "category": "fruit",
            "unlock_threshold": 6,
            "sprite_path": "/sprites/dragon_fruit.svg",
            "description": "Looks cooler than it tastes.",
            "rarity": "uncommon",
            "color": "#FF1493",
            "scores": {"nutritional_value": 15.4, "aesthetic_vibes": 18.9, "deep_lore": 2.1}
        },
        {
            "name": "Starfruit",
            "category": "fruit",
            "unlock_threshold": 6,
            "sprite_path": "/sprites/starfruit.svg",
            "description": "Star-shaped for some reason.",
            "rarity": "uncommon",
            "color": "#FFE87C",
            "scores": {"nutritional_value": 14.2, "aesthetic_vibes": 16.3}
        },
        {
            "name": "Lychee",
            "category": "fruit",
            "unlock_threshold": 6,
            "sprite_path": "/sprites/lychee.svg",
            "description": "Tiny and translucent.",
            "rarity": "uncommon",
            "color": "#FFC0CB",
            "scores": {"nutritional_value": 13.7, "aesthetic_vibes": 12.8}
        },
        {
            "name": "Passion Fruit",
            "category": "fruit",
            "unlock_threshold": 7,
            "sprite_path": "/sprites/passion_fruit.svg",
            "description": "Lives up to its name.",
            "rarity": "uncommon",
            "color": "#9B59B6",
            "scores": {"nutritional_value": 17.3, "aesthetic_vibes": 14.5, "chaos_energy": 3.2}
        },
        {
            "name": "Artichoke",
            "category": "vegetable",
            "unlock_threshold": 7,
            "sprite_path": "/sprites/artichoke.svg",
            "description": "A vegetable that fights back.",
            "rarity": "uncommon",
            "color": "#8F9779",
            "scores": {"nutritional_value": 19.8, "impossibility_index": 4.2}
        },
        {
            "name": "Avocado",
            "category": "fruit",
            "unlock_threshold": 7,
            "sprite_path": "/sprites/avocado.svg",
            "description": "Millennial fuel.",
            "rarity": "uncommon",
            "color": "#568203",
            "scores": {"nutritional_value": 23.4, "aesthetic_vibes": 11.7, "gift_quality": 9.2}
        },
        {
            "name": "Pomegranate",
            "category": "fruit",
            "unlock_threshold": 8,
            "sprite_path": "/sprites/pomegranate.svg",
            "description": "Tiny ruby seeds of sweetness.",
            "rarity": "uncommon",
            "color": "#C0362C",
            "scores": {"nutritional_value": 20.6, "aesthetic_vibes": 13.9, "deep_lore": 5.4}
        },
        {
            "name": "Coconut",
            "category": "fruit",
            "unlock_threshold": 8,
            "sprite_path": "/sprites/coconut.svg",
            "description": "Hairy on the outside, refreshing inside.",
            "rarity": "uncommon",
            "color": "#8B4513",
            "scores": {"nutritional_value": 18.9, "impossibility_index": 5.7}
        },
        # Herbs and spices
        {
            "name": "Basil",
            "category": "herb",
            "unlock_threshold": 8,
            "sprite_path": "/sprites/basil.svg",
            "description": "Fragrant Italian essential.",
            "rarity": "uncommon",
            "color": "#355E3B",
            "scores": {"nutritional_value": 11.3, "aesthetic_vibes": 9.8}
        },
        {
            "name": "Cinnamon",
            "category": "spice",
            "unlock_threshold": 9,
            "sprite_path": "/sprites/cinnamon.svg",
            "description": "Tree bark that tastes like Christmas.",
            "rarity": "uncommon",
            "color": "#8B4513",
            "scores": {"nutritional_value": 9.7, "aesthetic_vibes": 12.4, "deep_lore": 3.2}
        },
        {
            "name": "Vanilla Bean",
            "category": "spice",
            "unlock_threshold": 9,
            "sprite_path": "/sprites/vanilla_bean.svg",
            "description": "The second most expensive spice.",
            "rarity": "uncommon",
            "color": "#3B2414",
            "scores": {"nutritional_value": 7.8, "aesthetic_vibes": 14.3, "gift_quality": 11.7}
        },
        # Processed foods
        {
            "name": "Peanut Butter",
            "category": "food",
            "unlock_threshold": 9,
            "sprite_path": "/sprites/peanut_butter.svg",
            "description": "Spreadable protein.",
            "rarity": "uncommon",
            "color": "#C19A6B",
            "scores": {"nutritional_value": 17.2, "awful_colour": 8.9}
        },
        {
            "name": "Marshmallow",
            "category": "food",
            "unlock_threshold": 10,
            "sprite_path": "/sprites/marshmallow.svg",
            "description": "Solidified clouds of sugar.",
            "rarity": "uncommon",
            "color": "#FEFEFA",
            "scores": {"nutritional_value": 2.3, "aesthetic_vibes": 17.8, "awful_colour": 3.4}
        },
        {
            "name": "Pickles",
            "category": "food",
            "unlock_threshold": 10,
            "sprite_path": "/sprites/pickles.svg",
            "description": "Cucumbers that took a vinegar bath.",
            "rarity": "uncommon",
            "color": "#8DB600",
            "scores": {"nutritional_value": 6.7, "awful_colour": 11.2, "existential_dread": 4.3}
        },
        {
            "name": "Ice Cream",
            "category": "food",
            "unlock_threshold": 10,
            "sprite_path": "/sprites/ice_cream.svg",
            "description": "Frozen happiness.",
            "rarity": "uncommon",
            "color": "#FFE5CC",
            "scores": {"nutritional_value": 4.8, "aesthetic_vibes": 21.7, "gift_quality": 15.3}
        },
        # Household items start appearing
        {
            "name": "Tea Bag",
            "category": "household",
            "unlock_threshold": 11,
            "sprite_path": "/sprites/tea_bag.svg",
            "description": "Leaf water in a convenient pouch.",
            "rarity": "uncommon",
            "color": "#8B7355",
            "scores": {"nutritional_value": 3.2, "aesthetic_vibes": 8.9, "temporal_displacement": 2.1}
        },
        {
            "name": "Sugar Cube",
            "category": "food",
            "unlock_threshold": 11,
            "sprite_path": "/sprites/sugar_cube.svg",
            "description": "Concentrated sweetness in geometric form.",
            "rarity": "uncommon",
            "color": "#FFFFFF",
            "scores": {"nutritional_value": 1.7, "aesthetic_vibes": 6.4}
        },
        {
            "name": "Salt",
            "category": "spice",
            "unlock_threshold": 11,
            "sprite_path": "/sprites/salt.svg",
            "description": "Makes everything better. Don't overdo it.",
            "rarity": "uncommon",
            "color": "#F8F8FF",
            "scores": {"nutritional_value": 0.3, "impossibility_index": 1.2}
        },
        {
            "name": "Pepper",
            "category": "spice",
            "unlock_threshold": 12,
            "sprite_path": "/sprites/pepper.svg",
            "description": "Makes you sneeze, makes food zing.",
            "rarity": "uncommon",
            "color": "#2C2C2C",
            "scores": {"nutritional_value": 2.1, "chaos_energy": 3.7}
        },
        {
            "name": "Olive Oil",
            "category": "food",
            "unlock_threshold": 12,
            "sprite_path": "/sprites/olive_oil.svg",
            "description": "Liquid gold from the Mediterranean.",
            "rarity": "uncommon",
            "color": "#B5B35C",
            "scores": {"nutritional_value": 15.6, "aesthetic_vibes": 10.2}
        },
        {
            "name": "Maple Syrup",
            "category": "food",
            "unlock_threshold": 12,
            "sprite_path": "/sprites/maple_syrup.svg",
            "description": "Tree blood that tastes amazing.",
            "rarity": "uncommon",
            "color": "#D4A574",
            "scores": {"nutritional_value": 6.9, "aesthetic_vibes": 13.8}
        },

        # === TIER 3: Slightly Unusual (13-20 blends) ===
        {
            "name": "Pencil",
            "category": "office",
            "unlock_threshold": 13,
            "sprite_path": "/sprites/pencil.svg",
            "description": "For writing. Not for eating.",
            "rarity": "uncommon",
            "color": "#FFD700",
            "scores": {"impossibility_index": 15.3, "awful_colour": 6.7, "existential_dread": 2.1}
        },
        {
            "name": "Eraser",
            "category": "office",
            "unlock_threshold": 13,
            "sprite_path": "/sprites/eraser.svg",
            "description": "Makes mistakes disappear. Smells weird.",
            "rarity": "uncommon",
            "color": "#FF69B4",
            "scores": {"impossibility_index": 14.8, "temporal_displacement": 8.3, "awful_colour": 4.2}
        },
        {
            "name": "Paper Clip",
            "category": "office",
            "unlock_threshold": 13,
            "sprite_path": "/sprites/paper_clip.svg",
            "description": "Bent wire with infinite uses.",
            "rarity": "uncommon",
            "color": "#C0C0C0",
            "scores": {"impossibility_index": 18.4, "chaos_energy": 5.6}
        },
        {
            "name": "Sticky Note",
            "category": "office",
            "unlock_threshold": 14,
            "sprite_path": "/sprites/sticky_note.svg",
            "description": "Someone's forgotten reminder.",
            "rarity": "uncommon",
            "color": "#FFFF99",
            "scores": {"temporal_displacement": 11.2, "existential_dread": 6.8, "awful_colour": 3.4}
        },
        {
            "name": "Button",
            "category": "household",
            "unlock_threshold": 14,
            "sprite_path": "/sprites/button.svg",
            "description": "Fell off someone's shirt.",
            "rarity": "uncommon",
            "color": "#4169E1",
            "scores": {"impossibility_index": 16.7, "aesthetic_vibes": 7.2}
        },
        {
            "name": "Coin",
            "category": "object",
            "unlock_threshold": 14,
            "sprite_path": "/sprites/coin.svg",
            "description": "Found between couch cushions.",
            "rarity": "uncommon",
            "color": "#B87333",
            "scores": {"impossibility_index": 19.3, "gift_quality": -3.2, "aesthetic_vibes": 8.9}
        },
        {
            "name": "Rubber Band",
            "category": "office",
            "unlock_threshold": 15,
            "sprite_path": "/sprites/rubber_band.svg",
            "description": "Stretchy and useful.",
            "rarity": "uncommon",
            "color": "#D2691E",
            "scores": {"impossibility_index": 21.4, "chaos_energy": 7.3}
        },
        {
            "name": "Postage Stamp",
            "category": "office",
            "unlock_threshold": 15,
            "sprite_path": "/sprites/postage_stamp.svg",
            "description": "Tiny art that travels.",
            "rarity": "uncommon",
            "color": "#DC143C",
            "scores": {"temporal_displacement": 14.6, "aesthetic_vibes": 11.2, "deep_lore": 4.3}
        },
        {
            "name": "Matchstick",
            "category": "household",
            "unlock_threshold": 15,
            "sprite_path": "/sprites/matchstick.svg",
            "description": "Controlled fire on a stick.",
            "rarity": "uncommon",
            "color": "#8B0000",
            "scores": {"chaos_energy": 12.8, "impossibility_index": 17.2}
        },
        {
            "name": "Candle",
            "category": "household",
            "unlock_threshold": 16,
            "sprite_path": "/sprites/candle.svg",
            "description": "Waxy light source.",
            "rarity": "uncommon",
            "color": "#FFFACD",
            "scores": {"aesthetic_vibes": 16.7, "temporal_displacement": 9.4, "gift_quality": 8.3}
        },
        {
            "name": "Key",
            "category": "object",
            "unlock_threshold": 16,
            "sprite_path": "/sprites/key.svg",
            "description": "Opens something. What? Who knows.",
            "rarity": "uncommon",
            "color": "#B8860B",
            "scores": {"impossibility_index": 22.7, "deep_lore": 11.3, "existential_dread": 8.4}
        },
        {
            "name": "Marble",
            "category": "toy",
            "unlock_threshold": 16,
            "sprite_path": "/sprites/marble.svg",
            "description": "A glass sphere. Normal sized.",
            "rarity": "uncommon",
            "color": "#4169E1",
            "scores": {"aesthetic_vibes": 13.8, "impossibility_index": 15.6}
        },
        {
            "name": "Dice",
            "category": "toy",
            "unlock_threshold": 17,
            "sprite_path": "/sprites/dice.svg",
            "description": "Randomness in a cube.",
            "rarity": "uncommon",
            "color": "#FFFFFF",
            "scores": {"chaos_energy": 18.9, "temporal_displacement": 6.7, "impossibility_index": 19.2}
        },
        {
            "name": "Playing Card",
            "category": "toy",
            "unlock_threshold": 17,
            "sprite_path": "/sprites/playing_card.svg",
            "description": "The Ace of Spades.",
            "rarity": "uncommon",
            "color": "#000000",
            "scores": {"chaos_energy": 14.3, "deep_lore": 8.9, "aesthetic_vibes": 12.7}
        },
        {
            "name": "Thimble",
            "category": "household",
            "unlock_threshold": 17,
            "sprite_path": "/sprites/thimble.svg",
            "description": "Tiny finger armor for sewing.",
            "rarity": "uncommon",
            "color": "#C0C0C0",
            "scores": {"impossibility_index": 24.1, "temporal_displacement": 15.8}
        },
        {
            "name": "Feather",
            "category": "object",
            "unlock_threshold": 18,
            "sprite_path": "/sprites/feather.svg",
            "description": "From a bird that's probably fine.",
            "rarity": "uncommon",
            "color": "#FFFFF0",
            "scores": {"aesthetic_vibes": 18.4, "impossibility_index": 20.3, "deep_lore": 5.6}
        },
        {
            "name": "Seashell",
            "category": "object",
            "unlock_threshold": 18,
            "sprite_path": "/sprites/seashell.svg",
            "description": "Echoes of the ocean inside.",
            "rarity": "uncommon",
            "color": "#FFF5EE",
            "scores": {"aesthetic_vibes": 21.3, "temporal_displacement": 12.7, "deep_lore": 7.8}
        },
        {
            "name": "Pine Cone",
            "category": "object",
            "unlock_threshold": 18,
            "sprite_path": "/sprites/pine_cone.svg",
            "description": "Nature's spiral sculpture.",
            "rarity": "uncommon",
            "color": "#8B4513",
            "scores": {"nutritional_value": 0.8, "aesthetic_vibes": 14.2, "impossibility_index": 12.9}
        },
        {
            "name": "Pebble",
            "category": "object",
            "unlock_threshold": 19,
            "sprite_path": "/sprites/pebble.svg",
            "description": "Smooth and ancient.",
            "rarity": "uncommon",
            "color": "#808080",
            "scores": {"impossibility_index": 26.8, "temporal_displacement": 18.4, "deep_lore": 6.3}
        },
        {
            "name": "Acorn",
            "category": "object",
            "unlock_threshold": 19,
            "sprite_path": "/sprites/acorn.svg",
            "description": "Future tree in a shell.",
            "rarity": "uncommon",
            "color": "#8B4513",
            "scores": {"nutritional_value": 4.3, "temporal_displacement": 21.7, "deep_lore": 9.8}
        },
        {
            "name": "Glass Bead",
            "category": "object",
            "unlock_threshold": 19,
            "sprite_path": "/sprites/glass_bead.svg",
            "description": "Tiny and translucent.",
            "rarity": "uncommon",
            "color": "#00CED1",
            "scores": {"aesthetic_vibes": 19.7, "impossibility_index": 22.3}
        },
        {
            "name": "Cork",
            "category": "object",
            "unlock_threshold": 20,
            "sprite_path": "/sprites/cork.svg",
            "description": "Kept the wine in once.",
            "rarity": "uncommon",
            "color": "#C4A484",
            "scores": {"impossibility_index": 25.6, "temporal_displacement": 13.9, "awful_colour": 8.7}
        },
        {
            "name": "Bottle Cap",
            "category": "object",
            "unlock_threshold": 20,
            "sprite_path": "/sprites/bottle_cap.svg",
            "description": "Ridged metal disc.",
            "rarity": "uncommon",
            "color": "#CD7F32",
            "scores": {"impossibility_index": 27.4, "chaos_energy": 9.8}
        },
        {
            "name": "Chalk",
            "category": "office",
            "unlock_threshold": 20,
            "sprite_path": "/sprites/chalk.svg",
            "description": "For sidewalk art or classrooms.",
            "rarity": "uncommon",
            "color": "#FFFFFF",
            "scores": {"impossibility_index": 23.8, "awful_colour": 9.3, "temporal_displacement": 11.2}
        },

        # === TIER 4: Getting Weird (21-30 blends) ===
        {
            "name": "Invisible Ink",
            "category": "absurd",
            "unlock_threshold": 21,
            "sprite_path": "/sprites/invisible_ink.svg",
            "description": "It's definitely in there. Trust me.",
            "rarity": "rare",
            "color": "#F0FFFF",
            "scores": {"impossibility_index": 34.7, "deep_lore": 18.3, "chaos_energy": 15.6}
        },
        {
            "name": "Lucky Penny",
            "category": "absurd",
            "unlock_threshold": 21,
            "sprite_path": "/sprites/lucky_penny.svg",
            "description": "Found heads-up. Slightly warm.",
            "rarity": "rare",
            "color": "#B87333",
            "scores": {"chaos_energy": 24.3, "gift_quality": 11.7, "temporal_displacement": 16.8}
        },
        {
            "name": "Four-Leaf Clover",
            "category": "absurd",
            "unlock_threshold": 21,
            "sprite_path": "/sprites/four_leaf_clover.svg",
            "description": "Defied the odds to grow this way.",
            "rarity": "rare",
            "color": "#00FF00",
            "scores": {"chaos_energy": 28.9, "aesthetic_vibes": 23.4, "impossibility_index": 31.2}
        },
        {
            "name": "Rabbit's Foot",
            "category": "absurd",
            "unlock_threshold": 22,
            "sprite_path": "/sprites/rabbits_foot.svg",
            "description": "Lucky for you. Not for the rabbit.",
            "rarity": "rare",
            "color": "#DEB887",
            "scores": {"chaos_energy": 32.7, "deep_lore": 21.8, "existential_dread": 19.4, "gift_quality": -8.3}
        },
        {
            "name": "Wishbone",
            "category": "absurd",
            "unlock_threshold": 22,
            "sprite_path": "/sprites/wishbone.svg",
            "description": "Make a wish. Pull carefully.",
            "rarity": "rare",
            "color": "#FFF8DC",
            "scores": {"chaos_energy": 27.4, "temporal_displacement": 24.3, "deep_lore": 14.7}
        },
        {
            "name": "Fortune Cookie Paper",
            "category": "absurd",
            "unlock_threshold": 22,
            "sprite_path": "/sprites/fortune_cookie_paper.svg",
            "description": "Your fortune: You will blend weird things.",
            "rarity": "rare",
            "color": "#FFFACD",
            "scores": {"temporal_displacement": 29.8, "deep_lore": 23.6, "existential_dread": 12.3}
        },
        {
            "name": "Worry Stone",
            "category": "absurd",
            "unlock_threshold": 23,
            "sprite_path": "/sprites/worry_stone.svg",
            "description": "Smoothed by a thousand anxious thumbs.",
            "rarity": "rare",
            "color": "#708090",
            "scores": {"existential_dread": 28.7, "temporal_displacement": 26.4, "aesthetic_vibes": 17.8}
        },
        {
            "name": "Mood Ring",
            "category": "absurd",
            "unlock_threshold": 23,
            "sprite_path": "/sprites/mood_ring.svg",
            "description": "Currently showing 'confused'.",
            "rarity": "rare",
            "color": "#9370DB",
            "scores": {"chaos_energy": 31.8, "existential_dread": 24.2, "aesthetic_vibes": 22.7, "impossibility_index": 36.9}
        },
        {
            "name": "Snow Globe",
            "category": "absurd",
            "unlock_threshold": 23,
            "sprite_path": "/sprites/snow_globe.svg",
            "description": "A tiny world in eternal winter.",
            "rarity": "rare",
            "color": "#B0E0E6",
            "scores": {"temporal_displacement": 33.8, "aesthetic_vibes": 28.9, "impossibility_index": 38.7, "deep_lore": 16.4}
        },
        {
            "name": "Music Box",
            "category": "absurd",
            "unlock_threshold": 24,
            "sprite_path": "/sprites/music_box.svg",
            "description": "Plays the same tune it always has.",
            "rarity": "rare",
            "color": "#CD853F",
            "scores": {"temporal_displacement": 37.3, "aesthetic_vibes": 32.4, "existential_dread": 21.8, "deep_lore": 24.7}
        },
        {
            "name": "Pocket Watch",
            "category": "absurd",
            "unlock_threshold": 24,
            "sprite_path": "/sprites/pocket_watch.svg",
            "description": "Ticks backwards sometimes.",
            "rarity": "rare",
            "color": "#FFD700",
            "scores": {"temporal_displacement": 44.8, "deep_lore": 28.3, "impossibility_index": 41.2, "chaos_energy": 26.7}
        },
        {
            "name": "Hourglass Sand",
            "category": "absurd",
            "unlock_threshold": 24,
            "sprite_path": "/sprites/hourglass_sand.svg",
            "description": "Time in granular form.",
            "rarity": "rare",
            "color": "#F5DEB3",
            "scores": {"temporal_displacement": 48.9, "deep_lore": 31.2, "existential_dread": 27.6}
        },
        {
            "name": "Compass",
            "category": "absurd",
            "unlock_threshold": 25,
            "sprite_path": "/sprites/compass.svg",
            "description": "Points to something, but not north.",
            "rarity": "rare",
            "color": "#B8860B",
            "scores": {"impossibility_index": 45.3, "deep_lore": 34.8, "chaos_energy": 29.7}
        },
        {
            "name": "Broken Mirror Shard",
            "category": "absurd",
            "unlock_threshold": 25,
            "sprite_path": "/sprites/broken_mirror.svg",
            "description": "Seven years of something.",
            "rarity": "rare",
            "color": "#E0FFFF",
            "scores": {"chaos_energy": 38.4, "existential_dread": 36.7, "temporal_displacement": 32.8, "impossibility_index": 42.9}
        },
        {
            "name": "Wind Chime",
            "category": "absurd",
            "unlock_threshold": 25,
            "sprite_path": "/sprites/wind_chime.svg",
            "description": "Sings songs the wind teaches it.",
            "rarity": "rare",
            "color": "#C0C0C0",
            "scores": {"aesthetic_vibes": 36.8, "temporal_displacement": 28.4, "impossibility_index": 39.7}
        },
        {
            "name": "Kaleidoscope",
            "category": "absurd",
            "unlock_threshold": 26,
            "sprite_path": "/sprites/kaleidoscope.svg",
            "description": "Infinite patterns from finite pieces.",
            "rarity": "rare",
            "color": "#FF1493",
            "scores": {"aesthetic_vibes": 44.7, "chaos_energy": 35.3, "impossibility_index": 47.8}
        },
        {
            "name": "Prism",
            "category": "absurd",
            "unlock_threshold": 26,
            "sprite_path": "/sprites/prism.svg",
            "description": "Splits light into its secrets.",
            "rarity": "rare",
            "color": "#E0FFFF",
            "scores": {"aesthetic_vibes": 41.9, "impossibility_index": 44.3, "deep_lore": 29.7}
        },
        {
            "name": "Message in a Bottle",
            "category": "absurd",
            "unlock_threshold": 26,
            "sprite_path": "/sprites/message_bottle.svg",
            "description": "The message says 'HELP'. From when?",
            "rarity": "rare",
            "color": "#40E0D0",
            "scores": {"temporal_displacement": 42.7, "existential_dread": 39.8, "deep_lore": 37.2}
        },
        {
            "name": "Treasure Map",
            "category": "absurd",
            "unlock_threshold": 27,
            "sprite_path": "/sprites/treasure_map.svg",
            "description": "X marks the spot. What spot?",
            "rarity": "rare",
            "color": "#F5DEB3",
            "scores": {"deep_lore": 43.8, "chaos_energy": 32.9, "temporal_displacement": 36.4}
        },
        {
            "name": "Magic 8-Ball Fluid",
            "category": "absurd",
            "unlock_threshold": 27,
            "sprite_path": "/sprites/magic_8_ball_fluid.svg",
            "description": "Reply hazy, try again.",
            "rarity": "rare",
            "color": "#000080",
            "scores": {"chaos_energy": 41.8, "temporal_displacement": 38.6, "impossibility_index": 51.2, "deep_lore": 34.3}
        },
        {
            "name": "Rorschach Blot",
            "category": "absurd",
            "unlock_threshold": 27,
            "sprite_path": "/sprites/rorschach.svg",
            "description": "What do you see?",
            "rarity": "rare",
            "color": "#000000",
            "scores": {"existential_dread": 44.3, "chaos_energy": 39.7, "deep_lore": 31.8}
        },
        {
            "name": "Ouija Board Planchette",
            "category": "absurd",
            "unlock_threshold": 28,
            "sprite_path": "/sprites/planchette.svg",
            "description": "Moved by 'spirits'. Sure.",
            "rarity": "rare",
            "color": "#8B4513",
            "scores": {"deep_lore": 48.7, "existential_dread": 42.9, "chaos_energy": 44.3, "temporal_displacement": 39.8}
        },
        {
            "name": "Lucky Horseshoe",
            "category": "absurd",
            "unlock_threshold": 28,
            "sprite_path": "/sprites/horseshoe.svg",
            "description": "U-shaped luck container.",
            "rarity": "rare",
            "color": "#4A4A4A",
            "scores": {"chaos_energy": 37.8, "deep_lore": 26.3, "gift_quality": 19.7}
        },
        {
            "name": "Skeleton Key",
            "category": "absurd",
            "unlock_threshold": 28,
            "sprite_path": "/sprites/skeleton_key.svg",
            "description": "Opens doors that don't exist.",
            "rarity": "rare",
            "color": "#C0C0C0",
            "scores": {"impossibility_index": 54.7, "deep_lore": 46.3, "temporal_displacement": 41.8}
        },
        {
            "name": "Cursed Monopoly Piece",
            "category": "absurd",
            "unlock_threshold": 29,
            "sprite_path": "/sprites/cursed_monopoly.svg",
            "description": "Always lands on Boardwalk.",
            "rarity": "rare",
            "color": "#FFD700",
            "scores": {"chaos_energy": 46.8, "existential_dread": 38.4, "impossibility_index": 49.3}
        },
        {
            "name": "Polaroid That Never Developed",
            "category": "absurd",
            "unlock_threshold": 29,
            "sprite_path": "/sprites/polaroid.svg",
            "description": "The image refuses to appear.",
            "rarity": "rare",
            "color": "#FFFAFA",
            "scores": {"temporal_displacement": 47.3, "existential_dread": 46.8, "impossibility_index": 52.7}
        },
        {
            "name": "VHS Tape (Rewound Halfway)",
            "category": "absurd",
            "unlock_threshold": 29,
            "sprite_path": "/sprites/vhs_tape.svg",
            "description": "Stuck in the middle of the movie.",
            "rarity": "rare",
            "color": "#2F4F4F",
            "scores": {"temporal_displacement": 51.8, "existential_dread": 41.2, "awful_colour": 18.7}
        },
        {
            "name": "Yo-Yo",
            "category": "absurd",
            "unlock_threshold": 30,
            "sprite_path": "/sprites/yoyo.svg",
            "description": "Goes down. Comes up. Philosophically troubling.",
            "rarity": "rare",
            "color": "#FF6347",
            "scores": {"temporal_displacement": 43.8, "chaos_energy": 35.9, "existential_dread": 34.7}
        },
        {
            "name": "Spinning Top",
            "category": "absurd",
            "unlock_threshold": 30,
            "sprite_path": "/sprites/spinning_top.svg",
            "description": "Still spinning. Has it ever stopped?",
            "rarity": "rare",
            "color": "#8B0000",
            "scores": {"temporal_displacement": 49.7, "existential_dread": 48.3, "chaos_energy": 42.8, "impossibility_index": 56.4}
        },
        {
            "name": "Boomerang",
            "category": "absurd",
            "unlock_threshold": 30,
            "sprite_path": "/sprites/boomerang.svg",
            "description": "Always returns. Always.",
            "rarity": "rare",
            "color": "#D2691E",
            "scores": {"temporal_displacement": 45.9, "impossibility_index": 58.2, "chaos_energy": 39.4}
        },

        # === TIER 5: Absurd Territory (31-45 blends) ===
        {
            "name": "Schrödinger's Lunch",
            "category": "absurd",
            "unlock_threshold": 31,
            "sprite_path": "/sprites/schrodingers_lunch.svg",
            "description": "Both fresh and moldy until you check.",
            "rarity": "rare",
            "color": "#A9A9A9",
            "scores": {"impossibility_index": 67.8, "existential_dread": 56.3, "chaos_energy": 51.7, "temporal_displacement": 48.9}
        },
        {
            "name": "Bottled Echo",
            "category": "absurd",
            "unlock_threshold": 31,
            "sprite_path": "/sprites/bottled_echo.svg",
            "description": "Someone's voice, repeating forever.",
            "rarity": "rare",
            "color": "#E6E6FA",
            "scores": {"impossibility_index": 64.2, "existential_dread": 52.8, "temporal_displacement": 54.3}
        },
        {
            "name": "Captured Shadow",
            "category": "absurd",
            "unlock_threshold": 32,
            "sprite_path": "/sprites/captured_shadow.svg",
            "description": "Dark, but somehow tangible.",
            "rarity": "rare",
            "color": "#2F2F2F",
            "scores": {"impossibility_index": 71.3, "existential_dread": 58.7, "chaos_energy": 54.9, "deep_lore": 41.2}
        },
        {
            "name": "Jar of Fireflies",
            "category": "absurd",
            "unlock_threshold": 32,
            "sprite_path": "/sprites/fireflies.svg",
            "description": "Blinking in morse code. What's the message?",
            "rarity": "rare",
            "color": "#FFFF00",
            "scores": {"aesthetic_vibes": 48.7, "deep_lore": 44.3, "impossibility_index": 59.8}
        },
        {
            "name": "Gravity-Defying Orb",
            "category": "absurd",
            "unlock_threshold": 33,
            "sprite_path": "/sprites/gravity_orb.svg",
            "description": "Floats. Refuses to fall.",
            "rarity": "rare",
            "color": "#87CEEB",
            "scores": {"impossibility_index": 78.4, "chaos_energy": 61.3, "aesthetic_vibes": 44.2}
        },
        {
            "name": "Frozen Flame",
            "category": "absurd",
            "unlock_threshold": 33,
            "sprite_path": "/sprites/frozen_flame.svg",
            "description": "Fire, but cold to the touch.",
            "rarity": "epic",
            "color": "#00BFFF",
            "scores": {"impossibility_index": 82.7, "chaos_energy": 67.8, "aesthetic_vibes": 52.3, "awful_colour": 34.6}
        },
        {
            "name": "Liquid Marble",
            "category": "absurd",
            "unlock_threshold": 34,
            "sprite_path": "/sprites/liquid_marble.svg",
            "description": "Solid and liquid. Both. Neither.",
            "rarity": "epic",
            "color": "#4169E1",
            "scores": {"impossibility_index": 76.9, "chaos_energy": 63.4, "existential_dread": 54.8}
        },
        {
            "name": "Singing Stone",
            "category": "absurd",
            "unlock_threshold": 34,
            "sprite_path": "/sprites/singing_stone.svg",
            "description": "Hums ancient melodies.",
            "rarity": "epic",
            "color": "#708090",
            "scores": {"impossibility_index": 69.3, "deep_lore": 58.7, "aesthetic_vibes": 49.8, "temporal_displacement": 52.3}
        },
        {
            "name": "Perpetual Motion Marble",
            "category": "absurd",
            "unlock_threshold": 35,
            "sprite_path": "/sprites/perpetual_marble.svg",
            "description": "Rolls forever. Never stops.",
            "rarity": "epic",
            "color": "#C0C0C0",
            "scores": {"impossibility_index": 89.7, "temporal_displacement": 71.8, "chaos_energy": 68.4}
        },
        {
            "name": "Backwards Clock",
            "category": "absurd",
            "unlock_threshold": 35,
            "sprite_path": "/sprites/backwards_clock.svg",
            "description": "Counts down to... something.",
            "rarity": "epic",
            "color": "#FFD700",
            "scores": {"temporal_displacement": 78.9, "existential_dread": 67.3, "impossibility_index": 73.8}
        },
        {
            "name": "Memory Foam (Literal)",
            "category": "absurd",
            "unlock_threshold": 36,
            "sprite_path": "/sprites/memory_foam.svg",
            "description": "Remembers everyone who touched it.",
            "rarity": "epic",
            "color": "#F0F8FF",
            "scores": {"impossibility_index": 81.2, "deep_lore": 64.8, "existential_dread": 62.7, "temporal_displacement": 58.9}
        },
        {
            "name": "Invisible Paint",
            "category": "absurd",
            "unlock_threshold": 36,
            "sprite_path": "/sprites/invisible_paint.svg",
            "description": "Colors you can't see.",
            "rarity": "epic",
            "color": "#F8F8FF",
            "scores": {"impossibility_index": 77.6, "chaos_energy": 59.3, "aesthetic_vibes": 51.7}
        },
        {
            "name": "Everlasting Bubble",
            "category": "absurd",
            "unlock_threshold": 37,
            "sprite_path": "/sprites/everlasting_bubble.svg",
            "description": "Never pops. Never will.",
            "rarity": "epic",
            "color": "#E0FFFF",
            "scores": {"impossibility_index": 84.3, "aesthetic_vibes": 56.8, "temporal_displacement": 64.2}
        },
        {
            "name": "Unbreakable Wishbone",
            "category": "absurd",
            "unlock_threshold": 37,
            "sprite_path": "/sprites/unbreakable_wishbone.svg",
            "description": "Wishes forever pending.",
            "rarity": "epic",
            "color": "#FAEBD7",
            "scores": {"impossibility_index": 79.8, "temporal_displacement": 69.4, "existential_dread": 65.8, "chaos_energy": 61.7}
        },
        {
            "name": "Taste of Purple",
            "category": "absurd",
            "unlock_threshold": 38,
            "sprite_path": "/sprites/taste_purple.svg",
            "description": "What purple tastes like, extracted.",
            "rarity": "epic",
            "color": "#9370DB",
            "scores": {"impossibility_index": 86.7, "aesthetic_vibes": 63.2, "chaos_energy": 71.8, "awful_colour": 42.3}
        },
        {
            "name": "Solidified Whisper",
            "category": "absurd",
            "unlock_threshold": 38,
            "sprite_path": "/sprites/solidified_whisper.svg",
            "description": "A secret you can hold.",
            "rarity": "epic",
            "color": "#F5F5F5",
            "scores": {"impossibility_index": 88.9, "deep_lore": 68.4, "existential_dread": 59.7}
        },
        {
            "name": "Déjà Vu Crystal",
            "category": "absurd",
            "unlock_threshold": 39,
            "sprite_path": "/sprites/deja_vu_crystal.svg",
            "description": "You feel like you've blended this before.",
            "rarity": "epic",
            "color": "#E6E6FA",
            "scores": {"temporal_displacement": 82.7, "existential_dread": 74.3, "impossibility_index": 79.4, "chaos_energy": 68.9}
        },
        {
            "name": "Uncertainty Principle",
            "category": "absurd",
            "unlock_threshold": 39,
            "sprite_path": "/sprites/uncertainty.svg",
            "description": "The more you know where it is, the less you know where it's going.",
            "rarity": "epic",
            "color": "#B0C4DE",
            "scores": {"impossibility_index": 93.8, "existential_dread": 78.9, "chaos_energy": 84.3}
        },
        {
            "name": "Paradox Cube",
            "category": "absurd",
            "unlock_threshold": 40,
            "sprite_path": "/sprites/paradox_cube.svg",
            "description": "Bigger on the inside. And the outside.",
            "rarity": "epic",
            "color": "#4B0082",
            "scores": {"impossibility_index": 97.3, "chaos_energy": 87.8, "temporal_displacement": 76.4, "existential_dread": 81.2}
        },
        {
            "name": "Recursive Mirror",
            "category": "absurd",
            "unlock_threshold": 41,
            "sprite_path": "/sprites/recursive_mirror.svg",
            "description": "Reflects reflections reflecting reflections.",
            "rarity": "epic",
            "color": "#E0FFFF",
            "scores": {"impossibility_index": 91.7, "existential_dread": 84.8, "chaos_energy": 79.3, "aesthetic_vibes": 61.4}
        },
        {
            "name": "Quantum Coin",
            "category": "absurd",
            "unlock_threshold": 41,
            "sprite_path": "/sprites/quantum_coin.svg",
            "description": "Both heads and tails until observed.",
            "rarity": "epic",
            "color": "#FFD700",
            "scores": {"impossibility_index": 95.4, "chaos_energy": 91.7, "temporal_displacement": 72.8, "existential_dread": 77.9}
        },
        {
            "name": "Bottled Nostalgia",
            "category": "absurd",
            "unlock_threshold": 42,
            "sprite_path": "/sprites/bottled_nostalgia.svg",
            "description": "Smells like childhood and regret.",
            "rarity": "epic",
            "color": "#FFE4B5",
            "scores": {"temporal_displacement": 87.9, "existential_dread": 79.3, "aesthetic_vibes": 68.7, "deep_lore": 63.8}
        },
        {
            "name": "Silence (Canned)",
            "category": "absurd",
            "unlock_threshold": 42,
            "sprite_path": "/sprites/canned_silence.svg",
            "description": "Absolute absence of sound, preserved.",
            "rarity": "epic",
            "color": "#2F4F4F",
            "scores": {"impossibility_index": 89.2, "existential_dread": 82.4, "aesthetic_vibes": 54.3}
        },
        {
            "name": "Tangible Idea",
            "category": "absurd",
            "unlock_threshold": 43,
            "sprite_path": "/sprites/tangible_idea.svg",
            "description": "A thought you can hold in your hand.",
            "rarity": "epic",
            "color": "#FFE4E1",
            "scores": {"impossibility_index": 99.8, "chaos_energy": 88.4, "deep_lore": 71.9, "existential_dread": 85.7}
        },
        {
            "name": "Frozen Moment",
            "category": "absurd",
            "unlock_threshold": 43,
            "sprite_path": "/sprites/frozen_moment.svg",
            "description": "3:42 PM, Tuesday, forever.",
            "rarity": "epic",
            "color": "#87CEEB",
            "scores": {"temporal_displacement": 94.8, "existential_dread": 88.3, "impossibility_index": 92.7, "deep_lore": 69.4}
        },
        {
            "name": "Probability Dice",
            "category": "absurd",
            "unlock_threshold": 44,
            "sprite_path": "/sprites/probability_dice.svg",
            "description": "Shows all numbers simultaneously.",
            "rarity": "epic",
            "color": "#FFFFFF",
            "scores": {"chaos_energy": 96.8, "impossibility_index": 94.3, "temporal_displacement": 81.7}
        },
        {
            "name": "Sentient Doorknob",
            "category": "absurd",
            "unlock_threshold": 44,
            "sprite_path": "/sprites/sentient_doorknob.svg",
            "description": "Judges you when you turn it.",
            "rarity": "epic",
            "color": "#B8860B",
            "scores": {"impossibility_index": 87.9, "existential_dread": 76.8, "chaos_energy": 73.4, "deep_lore": 58.3}
        },
        {
            "name": "Yesterday's Tomorrow",
            "category": "absurd",
            "unlock_threshold": 45,
            "sprite_path": "/sprites/yesterdays_tomorrow.svg",
            "description": "Time folded in on itself.",
            "rarity": "epic",
            "color": "#DA70D6",
            "scores": {"temporal_displacement": 103.8, "existential_dread": 91.7, "impossibility_index": 98.4, "chaos_energy": 89.3}
        },

        # === TIER 6: Magical-Lite (46-65 blends) ===
        {
            "name": "Wishing Star Fragment",
            "category": "magical",
            "unlock_threshold": 46,
            "sprite_path": "/sprites/wishing_star.svg",
            "description": "Fell from the night sky.",
            "rarity": "epic",
            "color": "#FFD700",
            "scores": {"aesthetic_vibes": 78.9, "chaos_energy": 67.3, "deep_lore": 72.4, "gift_quality": 48.7}
        },
        {
            "name": "Mermaid Scale",
            "category": "magical",
            "unlock_threshold": 46,
            "sprite_path": "/sprites/mermaid_scale.svg",
            "description": "Shimmers with oceanic secrets.",
            "rarity": "epic",
            "color": "#40E0D0",
            "scores": {"aesthetic_vibes": 74.3, "deep_lore": 68.9, "impossibility_index": 81.7}
        },
        {
            "name": "Phoenix Feather",
            "category": "magical",
            "unlock_threshold": 47,
            "sprite_path": "/sprites/phoenix_feather.svg",
            "description": "Warm to the touch. Occasionally smolders.",
            "rarity": "epic",
            "color": "#FF4500",
            "scores": {"forbidden_power": 67.8, "chaos_energy": 72.9, "aesthetic_vibes": 81.3, "temporal_displacement": 64.2}
        },
        {
            "name": "Unicorn Hair",
            "category": "magical",
            "unlock_threshold": 47,
            "sprite_path": "/sprites/unicorn_hair.svg",
            "description": "Pure and impossibly soft.",
            "rarity": "epic",
            "color": "#FFFFFF",
            "scores": {"aesthetic_vibes": 86.7, "deep_lore": 74.8, "impossibility_index": 84.3, "gift_quality": 52.9}
        },
        {
            "name": "Dragon's Tear",
            "category": "magical",
            "unlock_threshold": 48,
            "sprite_path": "/sprites/dragons_tear.svg",
            "description": "Crystallized sorrow of an ancient beast.",
            "rarity": "epic",
            "color": "#8B0000",
            "scores": {"deep_lore": 89.3, "forbidden_power": 74.7, "aesthetic_vibes": 79.8, "existential_dread": 68.4}
        },
        {
            "name": "Will-o'-Wisp",
            "category": "magical",
            "unlock_threshold": 48,
            "sprite_path": "/sprites/will_o_wisp.svg",
            "description": "Leads travelers astray. Beautifully.",
            "rarity": "epic",
            "color": "#00FF7F",
            "scores": {"aesthetic_vibes": 88.4, "chaos_energy": 76.8, "deep_lore": 81.9, "temporal_displacement": 69.7}
        },
        {
            "name": "Enchanted Acorn",
            "category": "magical",
            "unlock_threshold": 49,
            "sprite_path": "/sprites/enchanted_acorn.svg",
            "description": "Will grow into a world tree. Eventually.",
            "rarity": "epic",
            "color": "#8B4513",
            "scores": {"temporal_displacement": 91.8, "deep_lore": 84.3, "forbidden_power": 69.7, "aesthetic_vibes": 73.2}
        },
        {
            "name": "Moonbeam (Bottled)",
            "category": "magical",
            "unlock_threshold": 49,
            "sprite_path": "/sprites/bottled_moonbeam.svg",
            "description": "Captured at midnight.",
            "rarity": "epic",
            "color": "#F0FFFF",
            "scores": {"aesthetic_vibes": 93.8, "deep_lore": 77.9, "impossibility_index": 89.4, "temporal_displacement": 73.8}
        },
        {
            "name": "Stardust",
            "category": "magical",
            "unlock_threshold": 50,
            "sprite_path": "/sprites/stardust.svg",
            "description": "The remnants of dead stars.",
            "rarity": "epic",
            "color": "#FFD700",
            "scores": {"aesthetic_vibes": 97.3, "forbidden_power": 81.8, "deep_lore": 93.4, "temporal_displacement": 87.9}
        },
        {
            "name": "Leprechaun Gold",
            "category": "magical",
            "unlock_threshold": 50,
            "sprite_path": "/sprites/leprechaun_gold.svg",
            "description": "Might disappear at sunrise.",
            "rarity": "epic",
            "color": "#FFD700",
            "scores": {"chaos_energy": 84.3, "temporal_displacement": 79.8, "gift_quality": -23.7, "deep_lore": 71.8}
        },
        {
            "name": "Witch's Brew",
            "category": "magical",
            "unlock_threshold": 51,
            "sprite_path": "/sprites/witchs_brew.svg",
            "description": "Bubbles ominously.",
            "rarity": "epic",
            "color": "#4B0082",
            "scores": {"forbidden_power": 88.9, "chaos_energy": 91.7, "awful_colour": 67.8, "deep_lore": 87.3}
        },
        {
            "name": "Luck Potion",
            "category": "magical",
            "unlock_threshold": 51,
            "sprite_path": "/sprites/luck_potion.svg",
            "description": "Or is it a curse? Hard to tell.",
            "rarity": "epic",
            "color": "#00FF00",
            "scores": {"chaos_energy": 87.4, "temporal_displacement": 82.3, "impossibility_index": 91.8}
        },
        {
            "name": "Invisibility Cloak Thread",
            "category": "magical",
            "unlock_threshold": 52,
            "sprite_path": "/sprites/invisibility_thread.svg",
            "description": "Can barely see it. That's the point.",
            "rarity": "legendary",
            "color": "#F0F8FF",
            "scores": {"impossibility_index": 102.7, "forbidden_power": 86.3, "deep_lore": 91.8, "chaos_energy": 79.4}
        },
        {
            "name": "Time Turner Sand",
            "category": "magical",
            "unlock_threshold": 52,
            "sprite_path": "/sprites/time_turner_sand.svg",
            "description": "Each grain is a second you could revisit.",
            "rarity": "legendary",
            "color": "#F5DEB3",
            "scores": {"temporal_displacement": 118.9, "forbidden_power": 97.8, "existential_dread": 89.3, "deep_lore": 94.7}
        },
        {
            "name": "Enchanted Rose Petal",
            "category": "magical",
            "unlock_threshold": 53,
            "sprite_path": "/sprites/enchanted_rose.svg",
            "description": "Never wilts. Counts down to... something.",
            "rarity": "legendary",
            "color": "#FF0000",
            "scores": {"aesthetic_vibes": 104.8, "temporal_displacement": 96.7, "deep_lore": 88.9, "gift_quality": 73.4}
        },
        {
            "name": "Genie's Lamp Oil",
            "category": "magical",
            "unlock_threshold": 53,
            "sprite_path": "/sprites/lamp_oil.svg",
            "description": "Three wishes not included.",
            "rarity": "legendary",
            "color": "#FFD700",
            "scores": {"forbidden_power": 103.8, "chaos_energy": 98.7, "deep_lore": 101.3}
        },
        {
            "name": "Philosopher's Mercury",
            "category": "magical",
            "unlock_threshold": 54,
            "sprite_path": "/sprites/philosophers_mercury.svg",
            "description": "The first step to transmutation.",
            "rarity": "legendary",
            "color": "#C0C0C0",
            "scores": {"forbidden_power": 112.7, "deep_lore": 107.8, "impossibility_index": 98.3, "chaos_energy": 91.8}
        },
        {
            "name": "Alchemical Salt",
            "category": "magical",
            "unlock_threshold": 54,
            "sprite_path": "/sprites/alchemical_salt.svg",
            "description": "Not for seasoning food.",
            "rarity": "legendary",
            "color": "#FFFAFA",
            "scores": {"forbidden_power": 98.4, "deep_lore": 103.7, "impossibility_index": 94.8}
        },
        {
            "name": "Elder Wand Splinter",
            "category": "magical",
            "unlock_threshold": 55,
            "sprite_path": "/sprites/elder_wand.svg",
            "description": "Thrums with barely-contained power.",
            "rarity": "legendary",
            "color": "#8B4513",
            "scores": {"forbidden_power": 124.8, "deep_lore": 118.3, "chaos_energy": 106.7}
        },
        {
            "name": "Resurrection Stone Dust",
            "category": "magical",
            "unlock_threshold": 55,
            "sprite_path": "/sprites/resurrection_dust.svg",
            "description": "Calls to the departed.",
            "rarity": "legendary",
            "color": "#2F4F4F",
            "scores": {"forbidden_power": 127.9, "existential_dread": 112.8, "temporal_displacement": 108.4, "deep_lore": 121.7}
        },
        {
            "name": "Magic Mirror Shard",
            "category": "magical",
            "unlock_threshold": 56,
            "sprite_path": "/sprites/magic_mirror.svg",
            "description": "Shows not what is, but what could be.",
            "rarity": "legendary",
            "color": "#E0FFFF",
            "scores": {"temporal_displacement": 114.7, "deep_lore": 109.8, "existential_dread": 98.3, "chaos_energy": 103.4}
        },
        {
            "name": "Prophecy Scroll Fragment",
            "category": "magical",
            "unlock_threshold": 56,
            "sprite_path": "/sprites/prophecy_scroll.svg",
            "description": "The future, written in riddles.",
            "rarity": "legendary",
            "color": "#F5DEB3",
            "scores": {"temporal_displacement": 121.8, "deep_lore": 117.9, "existential_dread": 104.7, "forbidden_power": 98.3}
        },
        {
            "name": "Basilisk Fang",
            "category": "magical",
            "unlock_threshold": 57,
            "sprite_path": "/sprites/basilisk_fang.svg",
            "description": "Destroys Horcruxes. Probably still venomous.",
            "rarity": "legendary",
            "color": "#556B2F",
            "scores": {"forbidden_power": 134.7, "chaos_energy": 118.9, "deep_lore": 124.8, "existential_dread": 97.3}
        },
        {
            "name": "Sorting Hat Thread",
            "category": "magical",
            "unlock_threshold": 57,
            "sprite_path": "/sprites/sorting_hat.svg",
            "description": "Whispers your true nature.",
            "rarity": "legendary",
            "color": "#8B4513",
            "scores": {"deep_lore": 128.9, "existential_dread": 108.4, "chaos_energy": 94.7}
        },
        {
            "name": "Patronus Essence",
            "category": "magical",
            "unlock_threshold": 58,
            "sprite_path": "/sprites/patronus.svg",
            "description": "Your happiest memory, given form.",
            "rarity": "legendary",
            "color": "#E0FFFF",
            "scores": {"aesthetic_vibes": 127.8, "forbidden_power": 119.3, "deep_lore": 113.7, "gift_quality": 89.4}
        },
        {
            "name": "Floo Powder",
            "category": "magical",
            "unlock_threshold": 58,
            "sprite_path": "/sprites/floo_powder.svg",
            "description": "For traveling through fireplaces.",
            "rarity": "legendary",
            "color": "#228B22",
            "scores": {"impossibility_index": 117.8, "chaos_energy": 112.4, "temporal_displacement": 99.7}
        },
        {
            "name": "Polyjuice Potion Base",
            "category": "magical",
            "unlock_threshold": 59,
            "sprite_path": "/sprites/polyjuice.svg",
            "description": "Become someone else. Just add hair.",
            "rarity": "legendary",
            "color": "#9ACD32",
            "scores": {"forbidden_power": 121.8, "chaos_energy": 128.7, "existential_dread": 114.9, "awful_colour": 78.3}
        },
        {
            "name": "Felix Felicis Drop",
            "category": "magical",
            "unlock_threshold": 59,
            "sprite_path": "/sprites/felix_felicis.svg",
            "description": "Liquid luck. Use wisely.",
            "rarity": "legendary",
            "color": "#FFD700",
            "scores": {"chaos_energy": 134.8, "temporal_displacement": 117.9, "forbidden_power": 128.3, "gift_quality": 94.7}
        },
        {
            "name": "Veritaserum",
            "category": "magical",
            "unlock_threshold": 60,
            "sprite_path": "/sprites/veritaserum.svg",
            "description": "Three drops will make you speak only truth.",
            "rarity": "legendary",
            "color": "#F0F8FF",
            "scores": {"forbidden_power": 118.9, "deep_lore": 122.4, "existential_dread": 109.8, "chaos_energy": 103.7}
        },
        {
            "name": "Amortentia Essence",
            "category": "magical",
            "unlock_threshold": 60,
            "sprite_path": "/sprites/amortentia.svg",
            "description": "Smells different to everyone.",
            "rarity": "legendary",
            "color": "#FFB6C1",
            "scores": {"forbidden_power": 126.7, "chaos_energy": 119.8, "aesthetic_vibes": 108.9, "existential_dread": 101.3}
        },
        {
            "name": "Pensieve Memory",
            "category": "magical",
            "unlock_threshold": 61,
            "sprite_path": "/sprites/pensieve_memory.svg",
            "description": "A memory you can dive into.",
            "rarity": "legendary",
            "color": "#87CEEB",
            "scores": {"temporal_displacement": 131.8, "deep_lore": 127.9, "existential_dread": 118.7, "aesthetic_vibes": 114.3}
        },
        {
            "name": "Horcrux Fragment",
            "category": "magical",
            "unlock_threshold": 61,
            "sprite_path": "/sprites/horcrux.svg",
            "description": "A piece of a soul. Don't ask how.",
            "rarity": "legendary",
            "color": "#2F2F2F",
            "scores": {"forbidden_power": 178.9, "existential_dread": 167.8, "chaos_energy": 154.3, "deep_lore": 171.4}
        },
        {
            "name": "Deathly Hallow Echo",
            "category": "magical",
            "unlock_threshold": 62,
            "sprite_path": "/sprites/deathly_hallow.svg",
            "description": "Resonates with the tale of three brothers.",
            "rarity": "legendary",
            "color": "#FFD700",
            "scores": {"forbidden_power": 189.7, "deep_lore": 184.3, "temporal_displacement": 167.9, "existential_dread": 173.8}
        },
        {
            "name": "Triwizard Cup Glow",
            "category": "magical",
            "unlock_threshold": 62,
            "sprite_path": "/sprites/triwizard.svg",
            "description": "Magical competition distilled.",
            "rarity": "legendary",
            "color": "#4169E1",
            "scores": {"chaos_energy": 141.8, "aesthetic_vibes": 118.9, "deep_lore": 134.7}
        },
        {
            "name": "Goblet of Fire Flame",
            "category": "magical",
            "unlock_threshold": 63,
            "sprite_path": "/sprites/goblet_flame.svg",
            "description": "Blue fire that chooses champions.",
            "rarity": "legendary",
            "color": "#0000FF",
            "scores": {"forbidden_power": 142.9, "chaos_energy": 148.7, "aesthetic_vibes": 127.8}
        },
        {
            "name": "Room of Requirement Dust",
            "category": "magical",
            "unlock_threshold": 63,
            "sprite_path": "/sprites/room_requirement.svg",
            "description": "Becomes what you need it to be.",
            "rarity": "legendary",
            "color": "#D3D3D3",
            "scores": {"impossibility_index": 147.8, "chaos_energy": 138.9, "temporal_displacement": 124.7, "deep_lore": 142.3}
        },
        {
            "name": "Marauder's Map Ink",
            "category": "magical",
            "unlock_threshold": 64,
            "sprite_path": "/sprites/marauders_ink.svg",
            "description": "I solemnly swear I am up to no good.",
            "rarity": "legendary",
            "color": "#2F4F4F",
            "scores": {"deep_lore": 138.9, "chaos_energy": 127.4, "temporal_displacement": 119.8}
        },
        {
            "name": "Remembrall Mist",
            "category": "magical",
            "unlock_threshold": 64,
            "sprite_path": "/sprites/remembrall.svg",
            "description": "Turns red when you forget something. What did you forget?",
            "rarity": "legendary",
            "color": "#FF0000",
            "scores": {"temporal_displacement": 128.7, "existential_dread": 121.9, "chaos_energy": 114.8}
        },
        {
            "name": "Howler Echo",
            "category": "magical",
            "unlock_threshold": 65,
            "sprite_path": "/sprites/howler.svg",
            "description": "Residual anger from a screaming letter.",
            "rarity": "legendary",
            "color": "#8B0000",
            "scores": {"chaos_energy": 152.8, "awful_colour": 89.7, "existential_dread": 98.4}
        },

        # === TIER 7: Full Magical (66-85 blends) ===
        {
            "name": "Cosmic Dust",
            "category": "magical",
            "unlock_threshold": 66,
            "sprite_path": "/sprites/cosmic_dust.svg",
            "description": "From the birth of galaxies.",
            "rarity": "legendary",
            "color": "#191970",
            "scores": {"forbidden_power": 198.7, "deep_lore": 203.8, "temporal_displacement": 187.9, "aesthetic_vibes": 164.3}
        },
        {
            "name": "Nebula Fragment",
            "category": "magical",
            "unlock_threshold": 67,
            "sprite_path": "/sprites/nebula_fragment.svg",
            "description": "A piece of a stellar nursery.",
            "rarity": "legendary",
            "color": "#9370DB",
            "scores": {"aesthetic_vibes": 187.9, "forbidden_power": 173.8, "deep_lore": 191.4, "chaos_energy": 168.7}
        },
        {
            "name": "Black Hole Whisper",
            "category": "magical",
            "unlock_threshold": 68,
            "sprite_path": "/sprites/black_hole.svg",
            "description": "The sound of everything becoming nothing.",
            "rarity": "legendary",
            "color": "#000000",
            "scores": {"forbidden_power": 212.9, "existential_dread": 224.8, "temporal_displacement": 198.7, "chaos_energy": 203.4}
        },
        {
            "name": "Supernova Spark",
            "category": "magical",
            "unlock_threshold": 69,
            "sprite_path": "/sprites/supernova.svg",
            "description": "A star's last breath.",
            "rarity": "legendary",
            "color": "#FF4500",
            "scores": {"chaos_energy": 234.8, "forbidden_power": 221.7, "aesthetic_vibes": 198.9, "temporal_displacement": 187.3}
        },
        {
            "name": "Primordial Chaos",
            "category": "magical",
            "unlock_threshold": 70,
            "sprite_path": "/sprites/primordial_chaos.svg",
            "description": "From before the universe had form.",
            "rarity": "legendary",
            "color": "#4B0082",
            "scores": {"chaos_energy": 267.9, "forbidden_power": 243.8, "temporal_displacement": 251.4, "existential_dread": 239.7}
        },
        {
            "name": "Divine Spark",
            "category": "magical",
            "unlock_threshold": 71,
            "sprite_path": "/sprites/divine_spark.svg",
            "description": "A fragment of creation itself.",
            "rarity": "legendary",
            "color": "#FFD700",
            "scores": {"forbidden_power": 278.9, "deep_lore": 267.8, "aesthetic_vibes": 234.7, "chaos_energy": 256.3}
        },
        {
            "name": "Eldritch Tentacle",
            "category": "magical",
            "unlock_threshold": 72,
            "sprite_path": "/sprites/eldritch_tentacle.svg",
            "description": "From something that should not be.",
            "rarity": "legendary",
            "color": "#2F4F4F",
            "scores": {"existential_dread": 287.9, "forbidden_power": 271.8, "chaos_energy": 264.7, "deep_lore": 278.3}
        },
        {
            "name": "Reality Anchor",
            "category": "magical",
            "unlock_threshold": 73,
            "sprite_path": "/sprites/reality_anchor.svg",
            "description": "Keeps existence from unraveling.",
            "rarity": "legendary",
            "color": "#C0C0C0",
            "scores": {"impossibility_index": 267.8, "existential_dread": 254.9, "forbidden_power": 248.7, "temporal_displacement": 241.8}
        },
        {
            "name": "Dimensional Tear",
            "category": "magical",
            "unlock_threshold": 74,
            "sprite_path": "/sprites/dimensional_tear.svg",
            "description": "A rip between worlds.",
            "rarity": "legendary",
            "color": "#8B008B",
            "scores": {"chaos_energy": 289.7, "impossibility_index": 276.8, "temporal_displacement": 267.9, "forbidden_power": 281.4}
        },
        {
            "name": "Infinity Stone Shard",
            "category": "magical",
            "unlock_threshold": 75,
            "sprite_path": "/sprites/infinity_shard.svg",
            "description": "Controls one aspect of existence.",
            "rarity": "legendary",
            "color": "#9400D3",
            "scores": {"forbidden_power": 312.8, "chaos_energy": 298.9, "temporal_displacement": 287.4, "impossibility_index": 294.7}
        },
        {
            "name": "Yggdrasil Root",
            "category": "magical",
            "unlock_threshold": 76,
            "sprite_path": "/sprites/yggdrasil.svg",
            "description": "From the World Tree itself.",
            "rarity": "legendary",
            "color": "#8B4513",
            "scores": {"deep_lore": 298.9, "forbidden_power": 287.3, "temporal_displacement": 276.8, "aesthetic_vibes": 267.4}
        },
        {
            "name": "Olympian Nectar",
            "category": "magical",
            "unlock_threshold": 77,
            "sprite_path": "/sprites/olympian_nectar.svg",
            "description": "The drink of gods.",
            "rarity": "legendary",
            "color": "#FFD700",
            "scores": {"forbidden_power": 301.8, "deep_lore": 289.7, "aesthetic_vibes": 278.9, "gift_quality": 187.3}
        },
        {
            "name": "Ambrosia Crumb",
            "category": "magical",
            "unlock_threshold": 78,
            "sprite_path": "/sprites/ambrosia.svg",
            "description": "The food of immortals.",
            "rarity": "legendary",
            "color": "#FFE4B5",
            "scores": {"forbidden_power": 294.7, "nutritional_value": 67.8, "deep_lore": 281.9, "gift_quality": 198.4}
        },
        {
            "name": "Valkyrie Feather",
            "category": "magical",
            "unlock_threshold": 79,
            "sprite_path": "/sprites/valkyrie_feather.svg",
            "description": "Guides the worthy to Valhalla.",
            "rarity": "legendary",
            "color": "#FFFFFF",
            "scores": {"deep_lore": 287.8, "forbidden_power": 276.9, "aesthetic_vibes": 264.3, "temporal_displacement": 258.7}
        },
        {
            "name": "Atlantean Crystal",
            "category": "magical",
            "unlock_threshold": 80,
            "sprite_path": "/sprites/atlantean_crystal.svg",
            "description": "From the lost city beneath the waves.",
            "rarity": "legendary",
            "color": "#00CED1",
            "scores": {"deep_lore": 312.9, "temporal_displacement": 298.7, "forbidden_power": 289.4, "aesthetic_vibes": 278.8}
        },
        {
            "name": "Shangri-La Lotus",
            "category": "magical",
            "unlock_threshold": 81,
            "sprite_path": "/sprites/shangri_la_lotus.svg",
            "description": "From paradise hidden in mountains.",
            "rarity": "legendary",
            "color": "#FFB6C1",
            "scores": {"aesthetic_vibes": 298.7, "temporal_displacement": 287.9, "deep_lore": 294.3, "existential_dread": -78.4}
        },
        {
            "name": "El Dorado Gold",
            "category": "magical",
            "unlock_threshold": 82,
            "sprite_path": "/sprites/el_dorado_gold.svg",
            "description": "From the city of gold that never was.",
            "rarity": "legendary",
            "color": "#FFD700",
            "scores": {"deep_lore": 301.8, "temporal_displacement": 289.7, "chaos_energy": 276.9, "gift_quality": 234.7}
        },
        {
            "name": "Excalibur Fragment",
            "category": "magical",
            "unlock_threshold": 83,
            "sprite_path": "/sprites/excalibur.svg",
            "description": "From the sword of kings.",
            "rarity": "legendary",
            "color": "#C0C0C0",
            "scores": {"forbidden_power": 324.8, "deep_lore": 318.9, "aesthetic_vibes": 287.4}
        },
        {
            "name": "Holy Grail Water",
            "category": "magical",
            "unlock_threshold": 84,
            "sprite_path": "/sprites/holy_grail.svg",
            "description": "The cup used at the Last Supper.",
            "rarity": "legendary",
            "color": "#FFD700",
            "scores": {"forbidden_power": 334.9, "deep_lore": 328.7, "temporal_displacement": 312.8, "existential_dread": 289.4}
        },
        {
            "name": "Ark of Covenant Glow",
            "category": "magical",
            "unlock_threshold": 85,
            "sprite_path": "/sprites/ark_glow.svg",
            "description": "Don't look directly at it.",
            "rarity": "legendary",
            "color": "#FFD700",
            "scores": {"forbidden_power": 387.9, "existential_dread": 367.8, "chaos_energy": 354.7, "deep_lore": 378.9}
        },

        # === TIER 8: Legendary+ (86-100+ blends) ===
        {
            "name": "Concept of Time",
            "category": "magical",
            "unlock_threshold": 86,
            "sprite_path": "/sprites/concept_time.svg",
            "description": "Time itself, made tangible.",
            "rarity": "legendary",
            "color": "#4B0082",
            "scores": {"temporal_displacement": 456.8, "forbidden_power": 423.9, "existential_dread": 412.7, "impossibility_index": 434.8}
        },
        {
            "name": "Pure Entropy",
            "category": "magical",
            "unlock_threshold": 88,
            "sprite_path": "/sprites/pure_entropy.svg",
            "description": "The heat death of the universe, bottled.",
            "rarity": "legendary",
            "color": "#2F2F2F",
            "scores": {"chaos_energy": 478.9, "existential_dread": 467.8, "forbidden_power": 445.7, "temporal_displacement": 434.9}
        },
        {
            "name": "Singularity Core",
            "category": "magical",
            "unlock_threshold": 90,
            "sprite_path": "/sprites/singularity.svg",
            "description": "Infinite density in finite space.",
            "rarity": "legendary",
            "color": "#000000",
            "scores": {"impossibility_index": 512.9, "forbidden_power": 498.7, "existential_dread": 487.9, "chaos_energy": 503.4}
        },
        {
            "name": "Big Bang Echo",
            "category": "magical",
            "unlock_threshold": 92,
            "sprite_path": "/sprites/big_bang.svg",
            "description": "The first sound. Still reverberating.",
            "rarity": "legendary",
            "color": "#FFFFFF",
            "scores": {"temporal_displacement": 534.8, "forbidden_power": 521.9, "chaos_energy": 512.7, "deep_lore": 498.9}
        },
        {
            "name": "Omnipotence Fragment",
            "category": "magical",
            "unlock_threshold": 94,
            "sprite_path": "/sprites/omnipotence.svg",
            "description": "A piece of unlimited power.",
            "rarity": "legendary",
            "color": "#FFD700",
            "scores": {"forbidden_power": 567.8, "chaos_energy": 543.9, "impossibility_index": 534.7, "existential_dread": 521.8}
        },
        {
            "name": "Absolute Zero",
            "category": "magical",
            "unlock_threshold": 96,
            "sprite_path": "/sprites/absolute_zero.svg",
            "description": "The coldest possible temperature.",
            "rarity": "legendary",
            "color": "#E0FFFF",
            "scores": {"impossibility_index": 487.9, "chaos_energy": 467.8, "temporal_displacement": 456.3}
        },
        {
            "name": "The Number Between 2 and 3",
            "category": "magical",
            "unlock_threshold": 98,
            "sprite_path": "/sprites/number_between.svg",
            "description": "Not 2.5. The other one.",
            "rarity": "legendary",
            "color": "#9370DB",
            "scores": {"impossibility_index": 598.7, "existential_dread": 578.9, "chaos_energy": 567.4, "deep_lore": 543.8}
        },
        {
            "name": "Forgotten Color",
            "category": "magical",
            "unlock_threshold": 100,
            "sprite_path": "/sprites/forgotten_color.svg",
            "description": "A hue no living being remembers.",
            "rarity": "legendary",
            "color": "#UNCERTAIN",
            "scores": {"aesthetic_vibes": 612.8, "existential_dread": 598.7, "impossibility_index": 587.9, "deep_lore": 567.3}
        }
    ]

    for obj_data in game_objects:
        existing = db.query(GameObject).filter(
            GameObject.name == obj_data["name"]
        ).first()
        if not existing:
            obj = GameObject(**obj_data)
            db.add(obj)

    db.commit()
    print(f"✓ Initialized {len(game_objects)} game objects")


def main():
    """Initialize all game data"""
    db = SessionLocal()
    try:
        print("Initializing Chaos Blender database...")
        init_scoring_systems(db)
        init_game_objects(db)
        print("✓ Database initialization complete!")
    except Exception as e:
        print(f"✗ Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()
