import os 
from pathlib import Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOW_DEBUG_RECORDING = True

BASE_PATH = Path(__file__).resolve().parent
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

LLM_CONFIGS = {
    'DEFAULT': {
        'TYPE': 'openai',
        'HOST': 'https://api.openai.com',
        'API_KEY': OPENAI_API_KEY,
        'PORT': 443,
        'MODEL': 'gpt-4o',
    }
}




