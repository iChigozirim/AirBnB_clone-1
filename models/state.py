#!/usr/bin/python3
"""Define a class State that inherits from BaseModel."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.
    Attributes:
        name (str): The name of the state.
    """

    name = ""