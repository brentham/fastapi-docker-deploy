from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from config.database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column (Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # todos = relationship("Todos", back_populates="owner")


import msal
from config.config import CLIENT_ID, CLIENT_SECRET, AUTHORITY

class MSALAuthModel:
    def __init__(self):
        self.app = msal.ConfidentialClientApplication(
            CLIENT_ID,
            authority=AUTHORITY,
            client_credential=CLIENT_SECRET,
        )

    def get_authorization_url(self, scopes, redirect_uri):
        return self.app.get_authorization_request_url(scopes, redirect_uri=redirect_uri)

    def acquire_token_by_code(self, code, scopes, redirect_uri):
        return self.app.acquire_token_by_authorization_code(code, scopes=scopes, redirect_uri=redirect_uri)

    def get_user(self):
        accounts = self.app.get_accounts()
        return accounts[0] if accounts else None
