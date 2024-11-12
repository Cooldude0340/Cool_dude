# copyright 2023 © Xron Trix | https://github.com/Xrontrix10


# @title 🖥️ Main Colab Leech Code

# @title Main Code
# @markdown <div><center><img src="https://user-images.githubusercontent.com/125879861/255391401-371f3a64-732d-4954-ac0f-4f093a6605e1.png" height=80></center></div>
# @markdown <center><h4><a href="https://github.com/XronTrix10/Telegram-Leecher/wiki/INSTRUCTIONS">READ</a> How to use</h4></center>

# @markdown <br>

API_ID = 2712818  # @param {type: "integer"}
API_HASH = "fda406cc4f648c303a0fb77255f2a026"  # @param {type: "string"}
BOT_TOKEN = "1880774062:AAHbe7FpEsd1UT5Yx7PITGrSTuWmQfQWc_g"  # @param {type: "string"}
USER_ID = 1517181772  # @param {type: "integer"}
DUMP_ID = 1713544941  # @param {type: "integer"}


import subprocess, time, json, shutil, os
from IPython.display import clear_output
from threading import Thread

Working = True

banner = '''

 ____   ____.______  ._______  .______       _____._.______  .___  ____   ____
 \\   \\_/   /: __   \\ : .___  \\ :      \\      \\__ _:|: __   \\ : __| \\   \\_/   /
  \\___ ___/ |  \\____|| :   |  ||       |       |  :||  \\____|| : |  \\___ ___/ 
  /   _   \\ |   :  \\ |     :  ||   |   |       |   ||   :  \\ |   |  /   _   \\ 
 /___/ \\___\\|   |___\\ \\_. ___/ |___|   |       |   ||   |___\\|   | /___/ \\___\\
            |___|       :/         |___|       |___||___|    |___|            
                        :                                                     
                          Dhinka chika bhai bhai cool dude                                                    
 
              _____     __     __     __              __          
             / ___/__  / /__ _/ /    / / ___ ___ ____/ /  ___ ____
            / /__/ _ \\/ / _ `/ _ \\  / /_/ -_) -_) __/ _ \\/ -_) __/
            \\___/\\___/_/\\_,_/_.__/ /____|__/\\__/\\__/_//_/\\__/_/   

                                                

'''

print(banner)

def Loading():
    white = 37
    black = 0
    while Working:
        print("\r" + "░"*white + "▒▒"+ "▓"*black + "▒▒" + "░"*white, end="")
        black = (black + 2) % 75
        white = (white -1) if white != 0 else 37
        time.sleep(2)
    clear_output()


_Thread = Thread(target=Loading, name="Prepare", args=())
_Thread.start()

if len(str(DUMP_ID)) == 10 and "-100" not in str(DUMP_ID):
    n_dump = "-100" + str(DUMP_ID)
    DUMP_ID = int(n_dump)

if os.path.exists("/content/sample_data"):
    shutil.rmtree("/content/sample_data")

cmd = "git clone https://github.com/XronTrix10/Telegram-Leecher"
proc = subprocess.run(cmd, shell=True)
cmd = "apt update && apt install ffmpeg aria2"
proc = subprocess.run(cmd, shell=True)
cmd = "pip3 install -r /content/Telegram-Leecher/requirements.txt"
proc = subprocess.run(cmd, shell=True)

credentials = {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "USER_ID": USER_ID,
    "DUMP_ID": DUMP_ID,
}

with open('/content/Telegram-Leecher/credentials.json', 'w') as file:
    file.write(json.dumps(credentials))

Working = False

if os.path.exists("/content/Telegram-Leecher/my_bot.session"):
    os.remove("/content/Telegram-Leecher/my_bot.session") # Remove previous bot session
    
print("\rStarting Bot....")

!cd /content/Telegram-Leecher/ && python3 -m colab_leecher #type:ignore
