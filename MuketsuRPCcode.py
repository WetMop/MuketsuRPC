##############READ###############
# Hello :)

# I will mark Changable options with a comment in green just like this

# When you change a option you must change the word inside the "" 

# To save your changes press ctrl + s

# Then to apply your changes you must click on your terminal and press ctrl+c and then run the file again



from pypresence import Presence
import time

client_id = '426143265671086122'  
RPC = Presence(client_id) 
RPC.connect()

print(RPC.update(state="Chillin", 
                 details="Who are you?",
                 large_image="muketsu",
                 large_text="discord.gg/muketsu", 
                 small_image="discord", 
                 small_text="Chillin on Discord", 
                 buttons=[{"label": "Join Muketsu", "url":"https://discord.com/invite/muketsu"}] )) 

# Hellow :) 
