from pydantic import BaseModel, Field
from typing import List, Dict, Optional

from models.dice import DiceRoll

# Update the Weapon model to use DiceRoll instead of DiceRollType
class Weapon(BaseModel):
    name: str = Field(..., description="The name of the weapon. For example, scimitar or crossbow.")
    damage: List[DiceRoll] = Field(..., description="The dice rolls that represent the base damage of the weapon.")
    damage_type: str = Field(..., description="The type of damage the weapon does. For example, bludgeoning or piercing.")
