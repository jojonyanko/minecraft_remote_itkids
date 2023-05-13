from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
import keyboard

mc = Minecraft.create(port=param.PORT_MC)

def Story(story):
        while keyboard.is_pressed("z") == False:
            while keyboard.is_pressed("z"):
                mc.postToChat(story)
                break
