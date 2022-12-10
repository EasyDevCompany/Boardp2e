import re
from pydantic import BaseModel, validator


class RegUserIn(BaseModel):
    email: str
    login: str
    password: str
    image: bytes or None

    @validator("password")
    def validate_password(cls, v):
        if len(v) <= 6:
            raise ValueError("Ваш должен бфть больше 5 символов")
        if v.isdigit() or v.isalpha():
            raise ValueError("Ваш пароль должен содержать хотябы одну букву или цифру")
        return v

    @validator("email")
    def validate_email(cls, v):
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(pattern, v) is None:
            raise ValueError("Некорректный email!")
        return v


class AuthUserIn(BaseModel):
    login: str
    password: str

