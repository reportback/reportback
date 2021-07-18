"""Common dependencies, to reduce cyclic imports.
"""
import os

from dotenv import load_dotenv
from fastapi_auth0 import Auth0

load_dotenv()

auth0_domain = os.getenv("AUTH0_DOMAIN")
auth0_api_audience = os.getenv("AUTH0_API_AUDIENCE")

auth = Auth0(domain=auth0_domain, api_audience=auth0_api_audience)
