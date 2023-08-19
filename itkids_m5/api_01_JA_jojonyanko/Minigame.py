from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
mc = Minecraft.create(port=param.PORT_MC)
import make_all
import make_story
from time import sleep
import random

make_story.Storys(["You really want to do this game?",
                   "I think it's not good idea.",
                   "You can't do this! You will die.",
                   "....",
                   "Ok...",
                   "Let's fight"])

# 黒曜石　49
playerx,playery,playerz=mc.player.getPos

def move_block(x,y,z,Scale,Block_ID,time,up=True):
    mc.setBlock(x,y,z,Block_ID)
    block_position = 1
    sleep(time)
    for i in range(Scale//2):
        mc.setBlocks(x+block_position,y,z,Block_ID,x+block_position,y+(Scale//2),z,Block_ID,param.AIR)
        mc.setBlocks(x-block_position,y,z,Block_ID,x-block_position,y+(Scale//2),z,Block_ID,param.AIR)
        mc.setBlock(x+block_position,y,z,Block_ID)
        mc.setBlock(x-block_position,y,z,Block_ID)
        block_position += 1
        sleep(time)
    if up==True:
        block_y = 1
        for i in range(Scale//2):
            mc.setBlock(x+block_position,y+block_y,z,Block_ID)
            mc.setBlock(x-block_position,y+block_y,z,Block_ID)
            block_y += 1


def make_stage(x=playerx,y=playery,z=playerz,Block_ID=49):
    block_position=0
    for i in range(25):
        move_block(x=x,y=y,z=z+block_position,Scale=50,Block_ID=Block_ID,time=0.1)
        move_block(x=x,y=y,z=z-block_position,Scale=50,Block_ID=Block_ID,time=0.1)
        if i == 24:
            block_y = 1
            for j in range(25):
                move_block(x=x,y=y+block_y,z=z+block_position,Scale=50,Block_ID=Block_ID,time=0.1,up=False)
                move_block(x=x,y=y+block_y,z=z-block_position,Scale=50,Block_ID=Block_ID,time=0.1,up=False)
                block_y += 1
                sleep(0.1)
        block_position += 1
        sleep(0.1)

make_stage()
block_y = playery + 52
for i in range(50):
    make_all.make_BOSS_Head(playerx+15,block_y,playerz+15)
    if(i != 49):
        sleep(0.1)
        make_all.make_BOSS_Head(playerx+15,block_y,playerz+15,Block_ID=[["a",0,0],["i",0],["h",0,0]])
    playery -= 1

make_all.make_Cercle_Anime_powerup(playerx+15,playery+1,playerz+15)

make_story.Story("Keep moving or fell from this world.")

Time=0
randomx=playerx
randomy=playery
randomz=playerz
try_again = 1
TNT_times=0
TNT_positions = []
Breaked_Fase=[]
Look_blockx=playerx+20
Look_blocky=playery+7
Look_blockz=playerz+20
while True:
    sleep(0.1)
    Time+=0.1
    if(Time % 3 == 0):
        playerx,playery,playerz = mc.player.getPos()
        mc.setBlocks(playerx,-125,playerz,playerx,125,playerz,40)
    if(Time % 10):
        mc.postToChat("Werning werning")
        sleep(0.5)
        mc.postToChat("TNT time")
        Look_blockx,Look_blocky,Look_blockz = randomx+20,randomy+7,randomz+20
        for i in range(125):
            if mc.getBlock(Look_blockx,Look_blocky,Look_blockz) == 0:
                Breaked_Fase += [Look_blockx,Look_blocky,Look_blockz]
            if i % 4 != 0:
                Look_blockx -= 1
            elif i % 4 == 0:
                if i % 20 != 0:
                    Look_blockz -= 1
                    Look_blockx = randomx + 20
                else:
                    Look_blocky -= 1
                    Look_blockx = randomx + 20
                    Look_blockz = randomz + 20
        TNT_time=True
        TNT_times += 1
        for i in range(5 + (TNT_times * 5)):
            while try_again == 0:
                x,y,z=random.randrange(randomx-50,randomx+50),randomy+1,random.randrange(randomz-50,randomz+50)
                if mc.getBlock(x,y,z) == param.TNT:
                    try_again=1
            mc.setBlock(x,y,z,param.TNT,1)
            TNT_positions += [x,y,z]
        make_all.make_BOSS_Head(randomx+15,randomy+2,randomz+15,Block_ID=[["a",49,0],["i",49],["h",49,1]])
        Lost_TNTs=5+(TNT_times * 5)
        while True:
            for i in range(5 + (TNT_times * 5)):
                if mc.getBlock(TNT_positions[i][0],TNT_positions[i][1],TNT_positions[i][2]) == 0:
                    Lost_TNTs -= 1
            if Lost_TNTs == 0:
                make_all.make_BOSS_Head(randomx+15,randomy+2,randomz+15)
                for i in len(Breaked_Fase):
                    mc.setBlock(Breaked_Fase[i][0],Breaked_Fase[i][1],Breaked_Fase[i][2],0)
                break
    if mc.getBlock(randomx+15,randomy+2,randomz+15) == 0:
        break
make_stage(x=randomx,y=randomy,z=randomz,Block_ID=0)
sleep(1)
mc.postToChat("Your clear time is " + Time + " seconds")
