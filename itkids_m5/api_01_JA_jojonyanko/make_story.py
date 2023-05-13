from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
import keyboard
import time

mc = Minecraft.create(port=param.PORT_MC)

def Story(story):
        while True:
            if keyboard.is_pressed("z"):
                mc.postToChat(story)
                time.sleep(1)
                break
                
