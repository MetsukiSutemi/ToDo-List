import asyncio
from app.database import init_db
from app.service import create_user, create_todo
def main():
    asyncio.run(create_todo(user_id=1 ,name="Pepe"))


if __name__ == "__main__":
    main()
