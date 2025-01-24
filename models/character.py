from pydantic import BaseModel, Field
from typing import List, Dict, Optional

from models.items import Weapon

class Character(BaseModel):
    # Basic Information
    name: str = Field(..., description="The name of the character")
    race: str = Field(..., description="The race of the character")
    character_class: str = Field(..., description="The class of the character")
    level: int = Field(..., description="The level of the character")
    alignment: str = Field(..., description="The moral and ethical alignment of the character")
    background: str = Field(..., description="The character's background, providing skills and features")

    # Core Stats
    strength: int = Field(..., description="The character's Strength ability score")
    dexterity: int = Field(..., description="The character's Dexterity ability score")
    constitution: int = Field(..., description="The character's Constitution ability score")
    intelligence: int = Field(..., description="The character's Intelligence ability score")
    wisdom: int = Field(..., description="The character's Wisdom ability score")
    charisma: int = Field(..., description="The character's Charisma ability score")

    # Derived Stats
    max_hit_points: int = Field(..., description="The maximum hit points of the character")
    armor_class: int = Field(..., description="The armor class of the character, representing defense")
    proficiency_bonus: int = Field(..., description="The character's proficiency bonus")

    # Skills and Saving Throws
    skills: Dict[str, int] = Field(..., description="Skill proficiencies and bonuses")
    saving_throws: Dict[str, int] = Field(..., description="Saving throw proficiencies and bonuses")

    # Equipment and Features
    weapons: List[Weapon] = Field(..., description="List of weapons available to the character")
    armor: str = Field(..., description="Armor worn by the character")
    equipment: List[str] = Field(..., description="Other equipment carried by the character")
    spells: List[str] = Field(..., description="List of spells available to the character")
    spell_slots: Dict[int, int] = Field(..., description="Remaining spell slots by level")
    features: List[str] = Field(..., description="Class and racial features of the character")
