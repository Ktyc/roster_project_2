from enum import Enum, auto
import dataclasses
from datetime import date


# Determine Fixed and Fluid Classes

class Role(Enum):
    WEEKDAY_PM = auto()
    WEEKEND_AM = auto()
    WEEKEND_PM = auto()
    # REMEMBER TO DISTINGUISH PUBLIC HOL FROM WEEKEND AND WEEKDAY DUTIES
    PUBLIC_HOL_AM = auto()
    PUBLIC_HOL_PM = auto()

class Shift: # Fluid
    pass

@dataclasses # don't need write __init__()
class Staff: # Fluid
    name: str
    role: Role(Staff)
    blackout_dates: Set(date)
    bidding_date: Set(date)