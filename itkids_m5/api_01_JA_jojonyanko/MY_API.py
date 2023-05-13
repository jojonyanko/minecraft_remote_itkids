from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
import make_story
import keyboard
import make_all
import time

mc = Minecraft.create(port=param.PORT_MC)

mc.postToChat("Please push Z")
# make_all.make_ALL(mc,0,0,0,True,False,True,False,False,False,False)

make_story.Story("???:Hello")

make_story.Story("thief:I'm thief")

make_story.Story("thief:You want to learn about how to steal DIAMONDBLOCK right?")

make_story.Story("thief:OK, I tell you")

mc.setBlock(0,50,-60,8)
make_story.Story("thief:I think we must start at little thing.")

mc.player.setPos(0,50,-60)
mc.setBlock(0,50,-60,0)
make_all.make_ALL(mc,0,0,0,True,False,False,False,False,False,False)
make_story.Story("thief:First, I think there are big tower in front of you.")

make_story.Story("thief:You must take WOOD to climb this tower.")
while True:
    x,y,z = mc.player.getPos()
    if(y < 100):
        if(-12 < x < 12 and -12 < z < 12):
            mc.setBlocks(-10,int(y),-10,10,int(y)+10,10,0)
            mc.spawnEntity(0,int(y)+1,0,64)
            mc.postToChat("thief:Oh no, you are found by this tower's monster. Let's leave this point.")
            mc.setBlock(-100,50,-100,8)
            time.sleep(5)
            mc.player.setPos(-100,50,-100)
            mc.setBlock(-100,50,-100,0)
            break






