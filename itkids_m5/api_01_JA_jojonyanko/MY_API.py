from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
import make_story
import keyboard
import make_all

mc = Minecraft.create(port=param.PORT_MC)

mc.postToChat("Please push Z")
# make_all.make_ALL(mc,0,0,0,True,False,True,False,False,False,False)
language = 1

make_story.Story("???:Hello")
make_story.Story("thief:I'm thief")





