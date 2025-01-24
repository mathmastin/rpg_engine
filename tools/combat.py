from phi.tools import Toolkit
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

from examples.combat_state import combat_state

from models.character import Character
from models.combat import Action, CombatState


class CombatToolkit(Toolkit):
    def __init__(self):
        super().__init__(name="combat_toolkit")
        self.register(self.generate_next_action)
        self.register(self.get_current_combat_state)
        self.register(self.update_combat_state)
        self.register(self.roll_dice)

        self.combat_state = combat_state


    # Define a tool for generating the next action for a monster
    def generate_next_action(self) -> str:
        """
        combat_state: CombatState = The state of the battle.
        """
        # Initialize a Phidata agent to determine the next action
        decision_agent = Agent(
            model=OpenAIChat(id="gpt-4o-mini"),
            description=(
                "You are a strategic combat AI for Dungeons & Dragons. "
                "You analyze the current combat situation, including player stats, "
                "monster stats, and the active combatant, to generate the best next action for that combatant. "
                "Remember that you can be creative with actions and use all available equipment, skill, spells, and other "
                "abilities described in the character description. Be sure to keep in mind how that character would react given "
                "their particular abilities, flaws, and other attributes."
            ),
            response_model=Action,
        )

        # Prepare the input prompt for the decision agent
        prompt = (
            f"Description of current state of the battle: \n {combat_state.model_dump()}"
        )

        # Get the response from the decision agent
        response = decision_agent.run(prompt, stream=False)

        return str(response.model_dump())

    def get_current_combat_state(self) -> str:
        return f"Here is a summary of the combat state: \n {self.combat_state.model_dump()}"
    
    def update_combat_state(self, turn_summary: str):
        """
        This function should be used any time something of significance happens and the state of the battle should be updated.
        This could include, damage, character movement, a combat turn being taken, etc...

        turn_summary: str = A summary of a single combatant's turn with all the information necessary to 
                            update the state of the battle.
        """
        update_agent = Agent(
            model=OpenAIChat(id="gpt-4o-mini"),
            description=(
                "You are a record keeping assistant for a Dungeons and Dragons DM. You will be given the actions taken and \n"
                "the results of those actions for single turn of combat. Your job is to update the state of the combat. You \n"
                "should apply any necessary changes to the combat state including, but not limited to:\n"
                "- apply damage to a character's hit points\n"
                "- increase a characters current hit points if, for example, the player was healed\n"
                "- update the description of the players location on the battle field and any other necessary descriptive fields.\n"
                "- update the active character.\n"
                "- If all characters have taken their turn for this round, make sure to update the round value AND BEGIN THE NEXT ROUND\n"

                "Remember that there are going to be characters not involved in this turn and battle status related to them \n"
                "should simply be copied into the new combat state.\n"

                "Here is the previous combat state: \n"
                f"{self.combat_state.model_dump()}"
            ),
            response_model=CombatState,
        )

        # Prepare the input prompt for the decision agent
        prompt = (
            f"Here is the description of the actions and outcomes: \n {turn_summary}"
        )

        # Get the response from the decision agent
        response = update_agent.run(prompt, stream=False)

        self.combat_state = response

        return f"Combat state updated. New combat state: \n {self.combat_state.model_dump()}"

    def roll_dice(self, dice_to_roll: str):
        """
        dice_to_roll: str = A description of the dice to be rolled.
        """
        dice_agent = Agent(
            model=OpenAIChat(id="gpt-4o-mini"),
            description=(
                "You are a dungeons and dragons dice rolling simulator. \n"
                "Roll the dice asked of you and make the results as random as possible. \n"
                "Be sure to add any modifiers to the roll."
            ),
        )

        # Prepare the input prompt for the decision agent
        prompt = (
            f"Here is the description of the actions and outcomes: \n {dice_to_roll}"
        )

        # Get the response from the decision agent
        response = dice_agent.run(prompt, stream=False)

        return str(response.model_dump())
