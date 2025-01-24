from typing import List, Dict, Optional
from pydantic import BaseModel, Field
from enum import Enum

from models.character import Character
from models.dice import DiceRoll
from models.items import Weapon

class StatusEffect(str, Enum):
    STUNNED = "stunned"
    POISONED = "poisoned"
    PARALYZED = "paralyzed"
    BURNING = "burning"
    FROZEN = "frozen"
    BLESSED = "blessed"
    NONE = "none"

class CharacterState(BaseModel):
    character: Character = Field(..., description="The character sheet for this character.")
    current_hp: int = Field(..., description="The current hit points of the character.")
    status_effects: List[StatusEffect] = Field(default_factory=list, description="A list of status effects currently affecting the character.")
    is_conscious: bool = Field(default=True, description="Indicates whether the character is conscious.")
    position: str = Field(None, description="A description of where this character is on the battle field.")

class Action(BaseModel):
    actor: str = Field(..., description="The name of the actor performing the action.")
    action: str = Field(..., description="The action to be performed by the monster (e.g., Attack, Defend)")
    round: int = Field(..., description="The round in which this action took place.")
    action_type: str = Field(..., description="The type of action performed, e.g., 'attack', 'cast_spell', 'move'.")
    weapon: List[Weapon] = Field(..., description="The list of weapons used in the attack, if any.")
    target: Optional[str] = Field(None, description="The name of the target (if applicable)")
    description: str = Field(..., description="A detailed description of the action")
    attack_dice_rolls: List[DiceRoll] = Field(..., description="The dice rolls that need to be rolled in order to know if the action was successful.")
    damage_dice_rolls: List[DiceRoll] = Field(..., description="The dice rolls that need to be rolled in order to compute damage assuming the attack is successful.")    

class BattleSetting(BaseModel):
    location_name: str = Field(..., description="The name of the battle location.")
    description: str = Field(..., description="A description of the battle setting.")

class CombatState(BaseModel):
    player_characters: List[CharacterState] = Field(..., description="A list of player characters involved in the combat.")
    mobs: List[CharacterState] = Field(..., description="A list of mobs involved in the combat.")
    turn_order: List[str] = Field(..., description="The that the players characters and monsters take their actions.")
    round_number: int = Field(..., description="The current round of combat. Each character gets one turn per round.")
    battle_setting: BattleSetting = Field(..., description="The setting information for the battle.")
    previous_actions: List[Action] = Field(..., description="An ordered log of all player and monster actions taken so far in the combat.")
    active_character_name: str = Field(..., description="The name of the active character. It is this characters turn to take an action.")
