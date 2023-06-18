from mcpi.minecraft import Minecraft
import param_MCJE1122 as param

import make_story
import make_all
import time

mc = Minecraft.create(port=param.PORT_MC)

mc.postToChat("Please push Z")

make_story.Storys(["???:Hello",
                   "thief:I'm thief",
                   "thief:You want to learn about how to steal DIAMONDBLOCK right?",
                   "thief:OK, I tell you"])

mc.setBlock(0,50,-60,8)
make_story.Story("thief:I think we must start at little thing.")

mc.postToChat("Push Z")
mc.player.setPos(0,50,-60)
mc.setBlock(0,50,-60,0)
make_all.make_ALL(mc,0,0,0,True,False,False,False,False,False,False)
make_story.Storys(["thief:First, I think there are big tower in front of you.",
                   "thief:You must take WOOD to climb this tower."])

while True:
    if mc.player.getPos() != None:
        x,y,z = mc.player.getPos()
        if(y < 100):
            if(-12 < x < 12 and -12 < z < 12):
                x,y,z = int(x),int(y),int(z)
                mc.setBlocks(x-1,y,z-1,x+1,y-100,z+1,param.AIR)
        elif (y > 100):
            if(-12 < x < 12 and -12 < z < 12):
                mc.setBlock(0,y,0,14)
                Block_y = y
                if mc.getBlock(0,Block_y,0) == param.AIR:
                    break
mc.postToChat("thief:Wow, you did it!!")
make_story.Storys(["thief:What are you welt now? I'm must you are very happy!",
                   "thief:What? When you were near at the tower, you felt down to deas area?",
                   "thief:Oh, sorry. I didn't know that..."])
mc.setBlock(-60,50,0,8)
make_story.Story("thief:By the way, we should level up. Let's go to another tower!!")

mc.player.setPos(-60,51,0,8)
mc.setBlock(-60,50,0,0)
make_all.make_ALL(mc,0,0,0,True,False,True,True,True,False,True)
make_story.Storys(["This is the next stage's tower.",
                   "It among deas area, but it have loard.",
                   "You can use this and take it GOLD_BLOCK.",
                   "Don't forget WOOD!! ...What? you don't want GOLD? You want DIAMOND?",
                   "Hey come on! Do you know we can get it now? The level up is first!"])

while True:
    if mc.player.getPos() != None:
        x,y,z = mc.player.getPos()
        if(y < 100):
            if(-12 < x < 12 and -12 < z < 12):
                x,y,z = int(x),int(y),int(z)
                mc.setBlocks(x-1,y,z-1,x+1,y-100,z+1,param.AIR)
        elif (y > 100):
            if(-12 < x < 12 and -12 < z < 12):
                mc.setBlock(0,y,0,14)
                Block_y = y
                if mc.getBlock(0,Block_y,0) == param.AIR:
                    break