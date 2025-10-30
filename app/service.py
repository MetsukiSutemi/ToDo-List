from app.database import sessionmaker
from app.models import User, Todo

async def create_user(name : str) -> User:
    async with sessionmaker() as session:
        user_obj = User(name = name)
        session.add(user_obj)
        await session.commit()
        await session.refresh(user_obj)

async def create_todo(user_id: int ,name : str) -> User:
    async with sessionmaker() as session:
        todo_obj = Todo(user_id = user_id,name = name)
        session.add(todo_obj)
        await session.commit()
        await session.refresh(todo_obj)