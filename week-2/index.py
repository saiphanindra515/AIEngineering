from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    id:int = Field(gt=0, description="The unique identifier for the user")
    name: str = Field(min_length=3)
    is_active: bool = True
    email: str = None
    age: int = Field(gt=0, lt=200)

    @field_validator("username")
    @classmethod
    def validate_username(cls, value):
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric")
        return value    


user = User(id=1, name="John Doe", email="john.doe@example.com", age=30)
print(user)

raw_data = {
    "id": 2,
    "name": "Jane Smith",
    "is_active": False,
    "email": "jane.smith@example.com",
    "age": 25
}

user2 = User.model_validate(raw_data)
print(user2)
print(user2.model_dump_json(indent=4)) # convert to json
print(user2.model_dump()) # convert to dict