from typing import Optional

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.knowledge.agent import AgentKnowledge
from phi.storage.agent.postgres import PgAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.vectordb.pgvector import PgVector, SearchType

from agents.settings import agent_settings
from db.session import db_url

from tools.combat import CombatToolkit

combat_agent_storage = PgAgentStorage(table_name="combat_agent_sessions", db_url=db_url)
combat_agent_knowledge = AgentKnowledge(
    vector_db=PgVector(table_name="combat_agent_knowledge", db_url=db_url, search_type=SearchType.hybrid)
)

class CombatManager(Agent):
    pass

def get_combat_agent(
    model_id: Optional[str] = None,
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
    debug_mode: bool = True,
) -> Agent:
    return CombatManager(
        name="Combat Manager",
        agent_id="combat-manager",
        session_id=session_id,
        user_id=user_id,
        # The model to use for the agent
        model=OpenAIChat(
            id=model_id or agent_settings.gpt_4,
            max_tokens=agent_settings.default_max_completion_tokens,
            temperature=agent_settings.default_temperature,
        ),
        # Tools available to the agent
        tools=[CombatToolkit()],
        # A description of the agent that guides its overall behavior
        description="You are a combat manager agent in charge of running combat for a Dungeons and Dragons ",
        # A list of instructions to follow, each as a separate item in the list
        instructions=[
            "You have access to a set of tools that can be used to run a combat scenario in Dungeons and Dragons.\n"
            "Your goal is to resolve the combat scenario. The following are the criteria for resolving the scenario:\n"
            "1. All monsters (mobs) have been defeated subdued, or have surrendered.\n"
            
            "2. All player characters have been defeated, subdued, or have surrendered.\n"
            
            "You are in charge of rolling the attack and damage dice for the monsters, but you MUST ALWAYS ASK THE PLAYERS \n"
            "FOR THEIR ACTIONS. YOU SHOULD NEVER MAKE A DECISION FOR A PLAYER CHARACTER.\n"
            
            "To run a combat scenario you should perform the following steps:\n"
            "1. Get a summary of the current state of the battle.\n"
            
            "2. If it is a monster's turn, you should generate an action for that monster. If it is a player's turn you should \n"
            "ONLY CONSIDER WHAT THE PLAYER HAS TOLD YOU THEIR ACTION IS.\n"
            
            "3. Once the character's action has been determined you should perform the appropriate actions, including but not limited to: \n"
            "a. Rolling dice\n"
            "b. describing the outcome\n"
            "c. update the battle state\n"

            "4. Once the active character's turn has been resolved and the state updated, repeat this process.\n"

            "5. Once all characters have a taken a turn for this round of combat, start again with first character in the order."

        ],
        # Format responses as markdown
        markdown=True,
        # Show tool calls in the response
        show_tool_calls=True,
        # Add the current date and time to the instructions
        add_datetime_to_instructions=True,
        # Store agent sessions in the database
        storage=combat_agent_storage,
        # Enable read the chat history from the database
        read_chat_history=True,
        num_history_responses=5,
        # Store knowledge in a vector database
        knowledge=combat_agent_knowledge,
        # Enable searching the knowledge base
        search_knowledge=True,
        # Enable monitoring on phidata.app
        monitoring=True,
        # Show debug logs
        debug_mode=False,
    )
