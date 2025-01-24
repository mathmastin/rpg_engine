from models.character import Character
from models.dice import DiceRoll
from models.items import Weapon


thalia = Character(
    name="Thalia Starwhisper",
    race="Elf",
    character_class="Wizard",
    level=5,
    alignment="Chaotic Good",
    background="Sage",
    strength=8,
    dexterity=14,
    constitution=12,
    intelligence=18,
    wisdom=13,
    charisma=10,
    max_hit_points=32,
    armor_class=12,
    proficiency_bonus=3,
    skills={"Arcana": 7, "History": 7, "Insight": 3, "Investigation": 7},
    saving_throws={"Intelligence": 6, "Wisdom": 3},
    weapons=[
        Weapon(
            name="Quarterstaff",
            damage=[
                DiceRoll(
                    sides=6,
                    modifier=0,
                    modifier_description="No modifier for base damage",
                    success_value=None,
                    success_value_justification=None
                )
            ],
            damage_type="Bludgeoning"
        )
    ],
    armor="None",
    equipment=["Spellbook", "Component Pouch", "Explorer's Pack"],
    spells=["Fireball", "Mage Armor", "Magic Missile", "Detect Magic", "Misty Step", "Shield"],
    spell_slots={1: 4, 2: 3, 3: 2},
    features=["Darkvision", "Fey Ancestry", "Arcane Recovery", "Evocation Savant"]
)


grum = Character(
    name="Grum Ironfist",
    race="Dwarf",
    character_class="Fighter",
    level=4,
    alignment="Lawful Neutral",
    background="Soldier",
    strength=16,
    dexterity=12,
    constitution=16,
    intelligence=10,
    wisdom=12,
    charisma=8,
    max_hit_points=44,
    armor_class=18,
    proficiency_bonus=2,
    skills={"Athletics": 5, "Perception": 3, "Intimidation": 1, "Survival": 3},
    saving_throws={"Strength": 5, "Constitution": 5},
    weapons=[
        Weapon(
            name="Battleaxe",
            damage=[
                DiceRoll(
                    sides=8,
                    modifier=0,
                    modifier_description="No modifier for base damage",
                    success_value=None,
                    success_value_justification=None
                )
            ],
            damage_type="Slashing"
        ),
        Weapon(
            name="Handaxe",
            damage=[
                DiceRoll(
                    sides=6,
                    modifier=0,
                    modifier_description="No modifier for base damage",
                    success_value=None,
                    success_value_justification=None
                )
            ],
            damage_type="Slashing"
        )
    ],
    armor="Chain Mail",
    equipment=["Shield", "Smith's Tools", "Explorer's Pack"],
    spells=[],
    spell_slots={},
    features=["Darkvision", "Dwarven Resilience", "Second Wind", "Action Surge"]
)


boneclaw = Character(
    name="Boneclaw",
    race="Undead",
    character_class="Monster",
    level=9,
    alignment="Neutral Evil",
    background="Former Wizard turned Undead Horror",
    strength=18,
    dexterity=16,
    constitution=15,
    intelligence=14,
    wisdom=13,
    charisma=12,
    max_hit_points=127,
    armor_class=16,
    proficiency_bonus=4,
    skills={"Perception": 7, "Stealth": 6, "Arcana": 5},
    saving_throws={"Strength": 7, "Dexterity": 6, "Wisdom": 5},
    weapons=[
        Weapon(
            name="Shadow Claw",
            damage=[
                DiceRoll(
                    sides=10,
                    modifier=4,
                    modifier_description="Strength modifier for melee attacks",
                    success_value=None,
                    success_value_justification=None
                ),
                DiceRoll(
                    sides=8,
                    modifier=0,
                    modifier_description="Additional necrotic damage",
                    success_value=None,
                    success_value_justification=None
                )
            ],
            damage_type="Slashing and Necrotic"
        )
    ],
    armor="Natural Armor",
    equipment=["Tattered Robes", "Amulet of Shadows"],
    spells=[
        "Misty Step",
        "Darkness",
        "Chill Touch"
    ],
    spell_slots={2: 3, 3: 2},
    features=[
        "Reach 15 ft. with Shadow Claw",
        "Shadow Jump: Teleport up to 120 ft. in dim light or darkness",
        "Undead Fortitude: Survive lethal damage with a Constitution save",
        "Darkvision 120 ft."
    ]
)
