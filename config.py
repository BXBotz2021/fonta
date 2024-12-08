import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8185385351:AAFiRBjdC50laiZfIUNloySQ19QUbU85-Z0")
    API_ID = int(os.environ.get('API_ID', '4088138'))
    API_HASH = os.environ.get('API_HASH', '4b19fd7339c360e956461f0f5535c5b1')
    OWNER_ID = int(os.environ.get("OWNER_ID", "1890385137"))
    
    # Add your AUTH_CHANNEL here
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1002437864651")  # Replace with your channel ID or username
