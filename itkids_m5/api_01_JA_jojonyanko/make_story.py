from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
import keyboard
import time

mc = Minecraft.create(port=param.PORT_MC)

def Story(story,botton="z"):
        while True:
            if keyboard.is_pressed(botton):
                mc.postToChat(story)
                time.sleep(1)
                break

def Storys(storys=[],botton="z"):
     story=0
     while story != len(storys):
          if keyboard.is_pressed(botton):
               mc.postToChat(storys[story])
               story += 1
               while keyboard.is_pressed(botton):
                    True

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
        elif (y < -125):
            mc.postToChat("Oh, are youu all right? (z)")
            mc.setBlock(-51,99,-51,8)
            Story("Please respown and try again!!")
            mc.player.setPos(-51,100,-51)
            mc.setBlock(-51,99,-51,0)
        if Kanshi == True:
            if(( x and y )or( x and y )or( x and y )or( x and y )):
                x,y,z = int(x),int(y),int(z)
                mc.setBlocks(x-1,y+2,z-1,x+1,y-100,z+1,param.AIR)