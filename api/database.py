from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from core.config import settings_app

settings = settings_app.db

# Создаем строку подключения к базе данных
DATABASE_URL = f"mysql+pymysql://{settings.user}:{settings.password}@{settings.host}:{settings.port}/{settings.name}"

# Создаем движок базы данных
engine = create_engine(DATABASE_URL)

# Создаем фабрику сессий
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()