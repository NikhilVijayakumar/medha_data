#src.bavans.agasthya.backend.app.config.settings
import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    """Application configuration settings."""
    INPUT_CONFIG_PATH: str = os.getenv('INPUT_CONFIG_PATH')

