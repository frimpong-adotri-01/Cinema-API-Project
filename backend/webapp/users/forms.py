from typing import List, Optional
from fastapi import Request
import pydantic


def is_valid_email(email_str: str) -> bool:
    try:
        pydantic.EmailStr(email_str)
        return True
    except pydantic.error_wrappers.ValidationError:
        return False


class UserCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.username: Optional[str] = None
        self.email: Optional[str] = None
        self. password: Optional[str] = None
        self.confirmed_password: Optional[str] = None


    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.email = form. get("email")
        self.password = form.get("password")
        self.confirmed_password = form.get("confirmed_password")


    async def is_valid(self):
        if not self.username or not len(self.username) > 3:
            self.username = ""
            self.errors.append("Username should be > 3 chars")
        if not self.email or not(self.email.__contains__("@")):  # pydantic.EmailStr cause problem
            self.email = ""
            self.errors.append( "Email is required" )
        if not self.password or len(self.password) < 4:
            self.password = ""
            self.confirmed_password = ""
            self.errors.append( "Password must be > 4 chars")
        if not (self.password == self.confirmed_password):
            self.password = ""
            self.confirmed_password = ""
            self.errors.append( "Passwords doesn't match !")
        if not self.errors: 
            return True
        # Effacer les données saisies
        
        
        
        return False