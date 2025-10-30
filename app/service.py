from app.database import sessionmaker
from app.models import User, Todo, Profile
from sqlalchemy import select

#⁡⁣⁢⁡⁢⁣⁣CRUD User⁡

async def get_all_users() -> list[User]:
    async with sessionmaker() as session:
        result = await session.execute(select(User))
        return result.scalars().all()

async def create_user(name : str) -> User:
    async with sessionmaker() as session:
        user_obj = User(name = name)
        session.add(user_obj)
        try:
            await session.commit()
            await session.refresh(user_obj)
        except Exception as e:
            await session.rollback()
            raise e
        return user_obj

async def create_user_with_profile(telegram_id: int, profile_name: str) -> User:
    async with sessionmaker() as session:
        user_obj = User(telegram_id=telegram_id)
        session.add(user_obj)
        try:
            await session.commit()
            await session.refresh(user_obj)

            profile_obj = Profile(
                name=profile_name,
                user_id=user_obj.id     
            )
            session.add(profile_obj)
            await session.commit()
            await session.refresh(profile_obj)

        except Exception as e:
            await session.rollback()
            raise e
        return user_obj


async def get_user_by_id(user_id : int) -> User | None:
    async with sessionmaker() as session:
        return await session.get(User, user_id)

async def update_user(user_id: int, **kwargs) -> User:
    async with sessionmaker() as session:
        user_obj = await session.get(User, user_id)
        if user_obj is None:
            return None
        for key, value in kwargs.items():
            if hasattr(user_obj, key):
                setattr(user_obj, key, value)
        await session.commit()
        await session.refresh(user_obj)
        return user_obj

async def delete_user(user_id: int) -> bool:
    async with sessionmaker() as session:
        user_obj = await session.get(User, user_id)
        if user_obj is None:
            return False
        await session.delete(user_obj)
        await session.commit()
        return True
        
#⁡⁢⁣⁣CRUD Todo⁡
async def create_todo(user_id: int ,name : str) -> User:
    async with sessionmaker() as session:
        todo_obj = Todo(user_id = user_id,name = name)
        session.add(todo_obj)
        await session.commit()
        await session.refresh(todo_obj)


async def get_todo_by_id(todo_id: int) -> Todo | None:
    async with sessionmaker() as session:
        return await session.get(Todo, todo_id)

async def get_todos_by_user(user_id: int) -> list[Todo]:
    async with sessionmaker() as session:
        result = await session.execute(
            select(Todo).where(Todo.user_id == user_id)
        )
        return result.scalars().all()

async def update_todo(todo_id: int, **kwargs) -> Todo | None:
    async with sessionmaker() as session:
        todo_obj = await session.get(Todo, todo_id)
        if todo_obj is None:
            return None
        for key, value in kwargs.items():
            if hasattr(todo_obj, key):
                setattr(todo_obj, key, value)
        await session.commit()
        await session.refresh(todo_obj)
        return todo_obj

async def delete_todo(todo_id: int) -> bool:
    async with sessionmaker() as session:
        todo_obj = await session.get(Todo, todo_id)
        if todo_obj is None:
            return False
        await session.delete(todo_obj)
        await session.commit()
        return True

#⁡⁢⁣⁣CRUD Profile⁡

async def create_profile(user_id: int, name: str) -> Profile:
    async with sessionmaker() as session:
        profile_obj = Profile(user_id=user_id, name=name)
        session.add(profile_obj)
        await session.commit()
        await session.refresh(profile_obj)
        return profile_obj

async def get_profile_by_id(profile_id: int) -> Profile | None:
    async with sessionmaker() as session:
        return await session.get(Profile, profile_id)

async def get_profiles_by_user(user_id: int) -> list[Profile]:
    async with sessionmaker() as session:
        result = await session.execute(
            select(Profile).where(Profile.user_id == user_id)
        )
        return result.scalars().all()

async def update_profile(profile_id: int, **kwargs) -> Profile | None:
    async with sessionmaker() as session:
        profile_obj = await session.get(Profile, profile_id)
        if profile_obj is None:
            return None
        for key, value in kwargs.items():
            if hasattr(profile_obj, key):
                setattr(profile_obj, key, value)
        await session.commit()
        await session.refresh(profile_obj)
        return profile_obj

async def delete_profile(profile_id: int) -> bool:
    async with sessionmaker() as session:
        profile_obj = await session.get(Profile, profile_id)
        if profile_obj is None:
            return False
        await session.delete(profile_obj)
        await session.commit()
        return True    
