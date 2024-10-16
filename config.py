import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    CANVAS_API_URL = os.getenv('CANVAS_API_URL')
    CANVAS_API_KEY = os.getenv('CANVAS_API_KEY')
    CANVAS_CLIENT_ID = os.getenv('CANVAS_CLIENT_ID')
    CANVAS_CLIENT_SECRET = os.getenv('CANVAS_CLIENT_SECRET')
    REDIRECT_URI = os.getenv('REDIRECT_URI')