from mcje.minecraft import Minecraft
import param_MCJE1122 as param
import make_story
import keyboard
import make_all
import time
import mcpi.entity as entity

mc = Minecraft.create(port=param.PORT_MC)
# mc = Minecraft.create(address="localhost", port=25565)

mc.postToChat("Please push Z")
# make_all.make_ALL(mc,0,0,0,True,False,True,False,False,False,False)

# make_story.Story("???:Hello")

# make_story.Story("thief:I'm thief")

make_story.Storys(["???:Hello",
                   "thief:I'm thief",
                   "thief:You want to learn about how to steal DIAMONDBLOCK right?",
                   "thief:OK, I tell you"])

mc.setBlock(0,50,-60,8)
make_story.Story("thief:I think we must start at little thing.")

mc.player.setPos(0,50,-60)
mc.setBlock(0,50,-60,0)
make_all.make_ALL(mc,0,0,0,True,False,False,False,False,False,False)
make_story.Storys(["thief:First, I think there are big tower in front of you.",
                   "thief:You must take WOOD to climb this tower."])
while True:
    x,y,z = mc.player.getPos()
    if(y < 100):
        if(-12 < x < 12 and -12 < z < 12):
            mc.setBlocks(-10,int(y),-10,10,int(y)+10,10,0)
            time.sleep(2)
            for i in range(1,10):
                mc.spawnEntity(0,int(y),0,entity.BLAZE)
            mc.postToChat("thief:Oh no, you are found by this tower's monster!!")
            # mc.setBlock(-100,50,-100,8)
            # time.sleep(5)
            # mc.player.setPos(-100,50,-100)
            # mc.setBlock(-100,50,-100,0)
            break






