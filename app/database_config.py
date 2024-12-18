import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from app.models.database_models import Base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("MYSQL_DATABASE")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
metadata = MetaData()

def init_db():
    # Base.metadata.drop_all(engine) 
    # print("Tables dropped successfully!") 
    
    Base.metadata.create_all(engine)
    print("Tables created successfully!")
