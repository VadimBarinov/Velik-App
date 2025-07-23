from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from db_config import DATABASES

settings = DATABASES['default']

# Создаем строку подключения к базе данных
DATABASE_URL = f"mysql+pymysql://{settings['USER']}:{settings['PASSWORD']}@{settings['HOST']}:{settings['PORT']}/{settings['NAME']}"

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