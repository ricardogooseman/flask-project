import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DATABASE")
USER_NAME = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
