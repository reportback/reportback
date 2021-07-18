"""Models

Need User, Contact, Adventure. These are early drafts
"""
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class Contact(BaseModel):
    """Each user has multiple contacts, who should be sent notifications"""

    name: str
    phone: str
    email: EmailStr


class Adventure(BaseModel):
    """Represents everything needed to start an adventure

    Should also contain all the information about status of the adventure,
    and the status of any attempts to make contacts about being back in
    civilization.

    TODO Compose with user_id to create a class that can reliably be used to use Mongo Index?
    """

    expected_start: str  # Should change to tz aware, bc daylight savings
    expected_end: str
    start_location: str  # enough to plug into Google maps, a name should be ok
    # Draft should have clickable, so user can check that a map appears as expected
    end_location: Optional[str]
    contacts: List[Contact]
