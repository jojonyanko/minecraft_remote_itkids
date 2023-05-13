from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
import make_story
import keyboard
import make_all

mc = Minecraft.create(port=param.PORT_MC)

mc.postToChat("Please push Z")
# make_all.make_ALL(mc,0,0,0,True,False,True,False,False,False,False)
language = 0

make_story.Story(mc,"Hello")
make_story.Story(mc,"Which is your language Japanese or English? If it is Japanese, please push J. If it is English, please push E")
while keyboard.is_pressed:
    if keyboard.is_pressed("j"):
        language = 1
        mc.postToChat("へぇ、日本人だったのか")
    if keyboard.is_pressed("e"):
        language = 0
        mc.postToChat("Oh, you use at English right? I see.")
