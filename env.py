from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
END_POINT = os.getenv("END_POINT")