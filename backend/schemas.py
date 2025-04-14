from pydantic import BaseModel

class Client(BaseModel):
    name: str
    industry: str 
    contact: str

class Deal(BaseModel):
    client: str
    value: int
    status: str

class User(BaseModel):
    id: int
    name: str
    role: str
    region: str
    skills: list[str] = []
    deals: list[Deal] = []
    clients: list[Client] = []