from pydantic import BaseModel, ConfigDict, EmailStr, Field

from .models import TodoState

# ========================================================
# SCHEMAS DE USUARIOS
# ========================================================


class UserSchema(BaseModel):
    username: str = Field(min_length=4, max_length=10)
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str = Field(min_length=4, max_length=10)
    email: EmailStr
    id: int

    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]


# ========================================================
# SCHEMAS DE FILTRAGEM E PAGINAÇÂO
# ========================================================
class FilterPage(BaseModel):
    offset: int = Field(0, ge=0)
    limit: int = Field(100, ge=1)


class FilterTodo(FilterPage):
    title: str | None = Field(default=None, min_length=3, max_length=20)
    descricao: str | None
    Status: TodoState | None


# ========================================================
# SCHEMA DE TOKENS
# ========================================================


class Token(BaseModel):
    access_token: str
    token_type: str


# ========================================================
# SCHEMAS DE TODOS
# ========================================================


class TodoSchema(BaseModel):
    nome: str
    descricao: str
    status: TodoState = Field(default=TodoState.todo)


class TodoPublic(TodoSchema):
    id: int

    model_config = ConfigDict(from_attributes=True)


class TodoList(BaseModel):
    todos: list[TodoPublic]


class UpdateTodo(BaseModel):
    title: str | None = None
    descricao: str | None = None
    Status: TodoState | None = None
