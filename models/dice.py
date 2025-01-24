from pydantic import BaseModel, Field
from typing import List, Dict, Optional

# Define a Pydantic model for a dice roll
class DiceRoll(BaseModel):
    sides: int = Field(..., description="The number of sides on the die (e.g., 4, 6, 8, 10, 12, 20, 100).")
    modifier: Optional[int] = Field(0, description="An optional modifier to add to the roll result.")
    modifier_description: Optional[str] = Field("", description="The justification for the modifier based on game rules.")
    success_value: Optional[int] = Field(None, description="The value needed in order for this dice roll to be considered successful based on game rules.")
    success_value_justification: Optional[str] = Field(None, description="The justification, based on game rules, for the provided success_value.")