import asyncio
from app.database import init_db
from app.service import create_user, create_todo, get_user_by_id, update_user
from app.bot.config import start_bot
def main():
    asyncio.run(start_bot())


if __name__ == "__main__":
    main()
