from sqlmodel import Field, SQLModel


class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=False)
    email: str = Field(index=True, unique=True)
    password: str = Field(index=False)
