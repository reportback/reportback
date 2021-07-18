"""Contacts
"""

from typing import List

from fastapi import APIRouter, Security
from fastapi_auth0 import Auth0User

from app.dependencies import auth
from app.models.models import Contact

router = APIRouter(
    prefix="/contacts",
    tags=["items"],
)


@router.get(
    "/",
    response_model=List[Contact],
    # dependencies=[Depends(auth.implicit_scheme)],
)
async def get_contacts(user: Auth0User = Security(auth.get_user)) -> List[Contact]:
    """Given the user, return the contacts

    How to get authorize: Go to auth0, Applications -> Report Back -> Quickstart

    There will be an example response. Use the copy button there, and paste it into the lock
    button. You will see what the cURL result will want.

    TODO: Next step, go to 11:23 on the FastAPI video to how to get users.
    """
    print(f"User was {user}")

    return [Contact(name="James", phone="3125545548", email="james@jamesliu.cc")]


@router.post("/")
async def post_contact(contact: Contact):
    """Add a contact to a user

    Should really just return 201 created.
    """
    print(f"Contact was {contact}")
    return {}
