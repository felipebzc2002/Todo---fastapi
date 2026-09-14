from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_session
from ..models import Todo, User
from ..schemas import FilterTodo, TodoList, TodoPublic, TodoSchema, UpdateTodo
from ..security import current_user

router = APIRouter(prefix='/todos', tags=['todos'])
Session = Annotated[AsyncSession, Depends(get_session)]
CurrentUser = Annotated[User, Depends(current_user)]


@router.post('/', status_code=HTTPStatus.CREATED, response_model=TodoPublic)
async def create_todos(session: Session, user: CurrentUser, todo: TodoSchema):

    new_todo = Todo(
        nome=todo.nome,
        descricao=todo.descricao,
        status=todo.status,
        user_id=user.id,
    )

    session.add(new_todo)
    await session.commit()
    await session.refresh(new_todo)

    return new_todo


@router.get('/', status_code=HTTPStatus.OK, response_model=TodoList)
async def read_todos(
    session: Session,
    user: CurrentUser,
    todo_filter: Annotated[FilterTodo, Query()],
):

    query = select(Todo).where(Todo.user_id == user.id)

    if todo_filter.title:
        query = query.filter(Todo.nome.contains(todo_filter.title))

    if todo_filter.descricao:
        query = query.filter(Todo.descricao.contains(todo_filter.descricao))

    if todo_filter.Status:
        query = query.filter(Todo.status.contains(todo_filter.Status))

    todos = await session.scalars(
        query.limit(todo_filter.limit).offset(todo_filter.offset)
    )

    return {'todos': todos.all()}


@router.delete('/{todo_id}')
async def delete_todo(session: Session, user: CurrentUser, todo_id: int):

    todo = await session.scalar(
        select(Todo).where(Todo.user_id == user.id, Todo.id == todo_id)
    )

    if not todo:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='task not found'
        )

    session.delete(todo)
    await session.commit()

    return {'message': 'task has been deleted succesfuly'}


@router.patch(
    '/{todo_id}', status_code=HTTPStatus.OK, response_model=UpdateTodo
)
async def patch_todo(
    session: Session, user: CurrentUser, todo_id: int, todo: UpdateTodo
):

    db_todo = await session.scalar(
        select(Todo).where(Todo.user_id == user.id, Todo.id == todo_id)
    )

    if not db_todo:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='task not found'
        )

    for key, value in todo.model_dump(exclude_unset=True).items():
        setattr(db_todo, key, value)

    session.add(db_todo)
    await session.commit()
    await session.refresh(db_todo)

    return db_todo
