##############READ###############
# Hello :)

# I will mark Changable options with a comment in gray just like this

# When you change a option you must change the word inside the "" 

# To save your changes press ctrl + s

# Then to apply your changes you must click on your terminal and press ctrl+c and then run the file again



from pypresence import Presence
import time

client_id = '426143265671086122'  
RPC = Presence(client_id) 
RPC.connect()

print(RPC.update(state="Chillin", # Optional
                 details="Who are you?", # Optional
                 large_image="muketsu",
                 large_text="discord.gg/muketsu", #Optional
                 small_image="discord", 
                 small_text="Chillin on Discord", #Optional
                 buttons=[{"label": "Join Muketsu", "url":"https://discord.com/invite/muketsu"}] )) 

# Hellow :) 
