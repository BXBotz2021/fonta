import pyrogram
import logging
import os
import time
import subprocess
import threading
from config import Config
from pyrogram import Client

# Logging setup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Function to check for updates and restart bot if needed
def check_for_updates():
    while True:
        try:
            logger.info("Checking for updates...")

            # Run `git fetch` to check for updates
            fetch_output = subprocess.run(["git", "fetch"], capture_output=True, text=True)
            
            # Check if there are any new commits
            status_output = subprocess.run(["git", "status", "-uno"], capture_output=True, text=True)
            
            if "Your branch is behind" in status_output.stdout:
                logger.info("New update found! Pulling changes...")
                subprocess.run(["git", "pull"], check=True)

                # Restart the bot after pulling updates
                logger.info("Restarting bot...")
                os.execv(sys.executable, ['python3'] + sys.argv)

            else:
                logger.info("No new updates.")

        except Exception as e:
            logger.error(f"Error while checking for updates: {e}")

        time.sleep(60)  # Check for updates every 1 minute

if __name__ == "__main__":
    plugins = dict(root="plugins")
    
    app = Client(
        "ShowJson",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=100
    )

    # Start update checker in a separate thread
    update_thread = threading.Thread(target=check_for_updates, daemon=True)
    update_thread.start()

    # Run the bot
    app.run()
