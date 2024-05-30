from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from app.config.config import config

class SqlBase:
    def __init__(self):
        # self.db_file = config.CONFIG_BDD['PATH']
        self.SQLALCHEMY_DATABASE_URL = f"sqlite:///database/database.db"
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()
    
    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

db_instance = SqlBase()