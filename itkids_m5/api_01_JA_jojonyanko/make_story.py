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

def Storys(storys=[]):
     story=0
     while story != len(storys):
          if keyboard.is_pressed("z"):
               mc.postToChat(storys[story])
               story += 1
               while keyboard.is_pressed("z"):
                    True
