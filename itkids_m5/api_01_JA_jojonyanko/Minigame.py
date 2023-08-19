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
playerx,playery,playerz=mc.player.getPos()

def move_block(x,y,z,Scale,Block_ID,time,up=True):
    mc.setBlock(x,y,z,Block_ID)
    block_position = 1
    sleep(time)
    for i in range(Scale//2):
        mc.setBlocks(x+block_position,y,z,x+block_position,y+(Scale//2),z,param.AIR)
        mc.setBlocks(x-block_position,y,z,x-block_position,y+(Scale//2),z,param.AIR)
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
        move_block(x=x,y=y,z=z+block_position,Scale=50,Block_ID=Block_ID,time=0.001)
        move_block(x=x,y=y,z=z-block_position,Scale=50,Block_ID=Block_ID,time=0.001)
        if i == 24:
            block_y = 1
            for j in range(25):
                move_block(x=x,y=y+block_y,z=z+block_position,Scale=50,Block_ID=Block_ID,time=0.001,up=False)
                move_block(x=x,y=y+block_y,z=z-block_position,Scale=50,Block_ID=Block_ID,time=0.001,up=False)
                block_y += 1
                sleep(0.5)
        block_position += 1
        sleep(0.1)

make_stage()
sleep(1)
block_y = playery + 56
for i in range(50):
    make_all.make_BOSS_Head(playerx+10,block_y,playerz+10)
    if(i != 49):
        sleep(0.25)
        make_all.make_BOSS_Head(playerx+10,block_y,playerz+10,Block_ID=[["a",0,0],["i",0],["h",0,0]])
    block_y -= 1

make_all.make_Cercle_Anime_powerup(playerx+10,playery+1,playerz+10)

sleep(0.25)
mc.postToChat("Keep moving or fell from this world.")

Time=0
randomx=playerx
randomy=playery
randomz=playerz
try_again = 1
TNT_times=0
TNT_positions = []
Breaked_Fase=[]
Look_blockx=playerx+17
Look_blocky=playery+7
Look_blockz=playerz+17
TNTx=0
TNTy=0
TNTz=0
TNT_count=0
Die_counter=0
while True:
    TNT_positions=[]
    Breaked_Fase=[]
    sleep(1)
    Time+=1
    if Time % 5 == 0:
        playerx,playery,playerz = mc.player.getPos()
        mc.setBlocks(playerx,playery-125,playerz,playerx,playery+125,playerz,0)
    if Time % 50 == 0:
        mc.postToChat("Werning werning")
        sleep(0.5)
        mc.postToChat("TNT time")
        Look_blockx,Look_blocky,Look_blockz = randomx+17,randomy+7,randomz+17
        for i in range(343):
            if mc.getBlock(Look_blockx,Look_blocky,Look_blockz) == 0:
                Breaked_Fase.append([Look_blockx,Look_blocky,Look_blockz])
            if i % 6 != 0:
                Look_blockx -= 1
            elif i % 6 == 0:
                if i % 49 != 0:
                    Look_blockz -= 1
                    Look_blockx = randomx + 20
                else:
                    Look_blocky -= 1
                    Look_blockx = randomx + 20
                    Look_blockz = randomz + 20
        print(Breaked_Fase)
        TNT_time=True
        TNT_times += 1
        TNT_count=0
        for i in range(5 + (TNT_times * 5)):
            while try_again != 0:
                TNTx=random.randint(int(randomx)-24,int(randomx)+24)
                TNTy=randomy+1
                TNTz=random.randint(int(randomz)-24,int(randomz)+24)
                if mc.getBlock(TNTx,TNTy,TNTz) == param.TNT:
                    try_again=1
                else:
                    try_again=0
            try_again=1
            mc.setBlock(TNTx,TNTy,TNTz,param.TNT,1)
            TNT_count += 1
            TNT_positions.append([TNTx,TNTy,TNTz])
            sleep(0.1)
        print(TNT_positions)
        print(TNT_count)
        make_all.make_BOSS_Head(randomx+10,randomy+7,randomz+10,Block_ID=[["a",49,0],["i",49],["h",49,1]])
        Lost_TNTs=TNT_count
        sleep(0.1)
        while True:
            Returned=0
            Lost_TNTs=TNT_count
            for i in range(5 + (TNT_times * 5)):
                Returned=i
                TNT_position_x,TNT_position_y,TNT_position_z=TNT_positions[Returned][0],TNT_positions[Returned][1],TNT_positions[Returned][2]
                if mc.getBlock(TNT_position_x,TNT_position_y,TNT_position_z) == 0:
                    Lost_TNTs -= 1
            if Lost_TNTs == 0:
                make_all.make_BOSS_Head(randomx+10,randomy+7,randomz+10)
                Returned=0
                for i in range(len(Breaked_Fase)):
                    Returned = i
                    Breaked_Fase_x,Breaked_Fase_y,Breaked_Fase_z=Breaked_Fase[Returned][0],Breaked_Fase[Returned][1],Breaked_Fase[Returned][2]
                    mc.setBlock(Breaked_Fase_x,Breaked_Fase_y,Breaked_Fase_z,0)
                break
    if mc.getBlock(randomx+10,randomy+7,randomz+10) == 0:
        break
    print(Time)
    if mc.player.getPos(y) <= randomy-145:
        Die_counter += 1
        mc.player.setPos(randomx,randomy+1,randomz)
mc.setBlocks(randomx+8,randomy+5,randomz+8,randomx+12,randomy+9,randomz+12,param.TNT)
sleep(1)
make_stage(x=randomx,y=randomy,z=randomz,Block_ID=0)
mc.postToChat("Your clear time is " + str(Time) + " seconds. Die:" + str(Die_counter))
