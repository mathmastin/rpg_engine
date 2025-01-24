from phi.agent import Agent
from phi.model.openai import OpenAIChat
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

from examples.characters import elven_wizard, goblin_skirmisher

from examples.combat_state import combat_state

from models.character import Character
from models.dice import DiceRoll
from models.items import Weapon

from tools.combat import CombatToolkit


# Example usage
if __name__ == "__main__":

    combat_toolkit = CombatToolkit()

    next_action = combat_toolkit.generate_next_action(combat_state)
    print(next_action.content)
  