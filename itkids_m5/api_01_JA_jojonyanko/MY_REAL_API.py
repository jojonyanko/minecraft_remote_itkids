from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
import mcpi.entity as Entity

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
def Charenge_thief(Block_ID=14,Around_Block=False,Around_Block_ID=1,Kanshi=False):
    block_was_breaked = False
    while True:
        x,y,z = mc.player.getPos()
        if(y < 100):
            if(-12 < x < 12 and -12 < z < 12):
                x,y,z = int(x),int(y),int(z)
                mc.setBlocks(x-1,y+2,z-1,x+1,y-100,z+1,param.AIR)
        elif (y > 100):
            if(-12 < x < 12 and -12 < z < 12) and block_was_breaked == False:
                block_was_breaked = True
                if Around_Block==True:
                    mc.setBlocks(-1,100,-1,1,102,1,Around_Block_ID)
                mc.setBlock(0,y,0,Block_ID,1)
                Block_y = y
            if mc.getBlock(0,Block_y,0) == 0 and block_was_breaked == True:
                break
        elif (y < -10):
            make_story.Storys(["Oh, are you all right?",
                            "Please respown and try again!!"])
        if Kanshi == True:
            if(( x and y )or( x and y )or( x and y )or( x and y )):
                x,y,z = int(x),int(y),int(z)
                mc.setBlocks(x-1,y+2,z-1,x+1,y-100,z+1,param.AIR)
Charenge_thief(1,True,1)
mc.postToChat("thief:Wow, you did it!!")
make_story.Storys(["thief:What are you welt now? I'm must you are very happy!",
                   "thief:What? When you were near at the tower, you felt down to dead area?",
                   "thief:Oh, sorry. I didn't know that..."])
mc.setBlock(-60,50,0,8)
make_story.Story("thief:By the way, we should level up. Let's go to another tower!!")

mc.player.setPos(-60,51,0,8)
mc.setBlock(-60,50,0,0)
make_all.make_ALL(mc,0,0,0,True,False,True,True,True,False,True)
make_story.Storys(["This is the next stage's tower.",
                   "It among deas area, but it have loard.",
                   "You can use this and take it IRON_ORE.",
                   "Don't forget WOOD!! ...What? you don't want IRON? You want DIAMOND?",
                   "Hey come on! Do you think we can get it now? The level up is first!"])

Charenge_thief(15,True,16)

#story

make_all.make_ALL(mc,0,0,0,True,False,True,False,True,True,True)

Charenge_thief(14,True,15,True)

#story

make_all.make_ALL(mc,0,0,0,True,True,True,True,True,True,True)

Charenge_thief(46,True,46,True)

#story

make_all.make_ALL(mc,0,0,0,True,True,True,False,False,True,False)

Charenge_thief(56,True,56,True)