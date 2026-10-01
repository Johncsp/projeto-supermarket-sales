import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# Banco 
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USUARIO')}:{os.getenv('DB_SENHA')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORTA')}/{os.getenv('DB_BANCO')}"
)
