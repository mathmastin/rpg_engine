from examples.characters import boneclaw, grum, thalia

from models.combat import Action, BattleSetting, CharacterState, CombatState
from models.items import Weapon, DiceRoll

# Player Characters

grum_state = CharacterState(
    character = grum,
    current_hp = 44,
    status_effects = [],
    is_conscious = True,
    position = "Standing guard in front of Thalia",

)

thalia_state = CharacterState(
    character =  thalia,
    current_hp = 32,
    status_effects = [],
    is_conscious = True,
    position = "Standing back and preparing spells.",

)

boneclaw_state = CharacterState(
    character = boneclaw,
    current_hp = 127,
    status_effects = [],
    is_conscious = True,
    position = "Waiting for battle across the field from the players.",
)


# Battle Setting
battle_setting = BattleSetting(
    location_name="Darkwood Forest",
    description="A dense, shadowy forest filled with thick underbrush and ancient trees.\n"
                "Several boulders appear in the area that could be used for cover."
)

# Combat State
combat_state = CombatState(
    player_characters=[grum_state, thalia_state],
    mobs=[boneclaw_state],
    battle_setting=battle_setting,
    previous_actions=[],
    turn_order=["grum", "boneclaw", "thalia"],
    round_number=1,
    active_character_name="grum"
)
