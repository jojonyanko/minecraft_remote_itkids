# from mcje.minecraft import Minecraft
# import param_MCJE as param

from mcpi.minecraft import Minecraft
import param_MCJE1122 as param

import make_kansito 
import make_kaidan
import make_insidekaidan
from time import sleep
import math

mc = Minecraft.create(port=param.PORT_MC)
def make_ALL(mc,x,y,z,make_hontow,make_utikaidann,make_naraku,make_kaidow,make_outkaidan,make_kansitow,make_box,
             Hontow_date=[10,100,10,param.GOLD_BLOCK],Utikaidann_date=[3,1,3,100,6,param.SEA_LANTERN_BLOCK],
             Kaidow_date=[49,1,4,20,param.GLASS],OutKaidan_date=[[48,4],1,[5,45,8,48],param.GLASS],
             Kanshitow_date=[[16,28,28,15],76,[16,28,15,28],["Shityu",param.GLOWSTONE,"Kahen",param.GLOWSTONE,"Zyouhen",param.GLOWSTONE]],
             Naraku_date=[49,100,49,300]):
    if make_naraku == True:
        if make_box == True:
            mc.setBlocks(x-50,y+1,z-50,x+50,y+111,z+50,param.GLASS)    
        mc.setBlocks(x-Naraku_date[0],y-Naraku_date[1],z-Naraku_date[2],x+Naraku_date[0],y+Naraku_date[3],z+Naraku_date[2],param.AIR)
    if make_hontow == True:
        make_kansito.make_honto(mc,x+Hontow_date[0],y+Hontow_date[1],z+Hontow_date[2],Hontow_date[3])
        if make_kaidow == True:
            make_kansito.make_kaidow(mc,x+Kaidow_date[0],y+Kaidow_date[1],z+Kaidow_date[2],y_plas=Kaidow_date[3],kaidowblock=Kaidow_date[4])
            if make_outkaidan ==True:
                make_kaidan.make_outkaidan_ES(mc,x+OutKaidan_date[0][0],y+OutKaidan_date[1],z-OutKaidan_date[2][0])
                make_kaidan.make_outkaidan_SW(mc,x-OutKaidan_date[0][1],y+OutKaidan_date[1],z-OutKaidan_date[2][1])
                make_kaidan.make_outkaidan_WN(mc,x+OutKaidan_date[0][0],y+OutKaidan_date[1],z+OutKaidan_date[2][2])
                make_kaidan.make_outkaidan_NE(mc,x-OutKaidan_date[0][1],y+OutKaidan_date[1],z+OutKaidan_date[2][3])
            if make_utikaidann == True:
                mc.setBlocks(x-Utikaidann_date[0],y+(Utikaidann_date[1]+1),z-Utikaidann_date[2],x+Utikaidann_date[0],y+Utikaidann_date[3],z+Utikaidann_date[2],param.AIR)
                mc.setBlocks(x-(Utikaidann_date[0]-1),y+Utikaidann_date[3],z-(Utikaidann_date[2]-1),x+(Utikaidann_date[0]-1),y+(Utikaidann_date[3]+1),z+(Utikaidann_date[2]-1),param.AIR)
                make_insidekaidan.make_insidekaidan_S(mc,x-Utikaidann_date[0],y+Utikaidann_date[1],z-Utikaidann_date[2],Utikaidann_date[4],Utikaidann_date[5])
                make_insidekaidan.make_insidekaidan_E(mc,x+Utikaidann_date[0],y+Utikaidann_date[1],z-Utikaidann_date[2],Utikaidann_date[4],Utikaidann_date[5])
                make_insidekaidan.make_insidekaidan_N(mc,x+Utikaidann_date[0],y+Utikaidann_date[1],z+Utikaidann_date[2],Utikaidann_date[4],Utikaidann_date[5])
                make_insidekaidan.make_insidekaidan_W(mc,x-Utikaidann_date[0],y+Utikaidann_date[1],z+Utikaidann_date[2],Utikaidann_date[4],Utikaidann_date[5])
    if make_kansitow == True:
        make_kansito.make_kannsito(mc, x-Kanshitow_date[0][0], z-Kanshitow_date[2][0],y=Kanshitow_date[1],
                                   sityuublock=Kanshitow_date[3][1],kahenblock=Kanshitow_date[3][3],zyouhenblock=Kanshitow_date[3][5])
        make_kansito.make_kannsito(mc, x+Kanshitow_date[0][1], z+Kanshitow_date[2][1], y=Kanshitow_date[1],
                                sityuublock=Kanshitow_date[3][1],kahenblock=Kanshitow_date[3][3],zyouhenblock=Kanshitow_date[3][5])
        make_kansito.make_kannsito(mc, x+Kanshitow_date[0][2], z-Kanshitow_date[2][2], y=Kanshitow_date[1],
                                sityuublock=Kanshitow_date[3][1],kahenblock=Kanshitow_date[3][3],zyouhenblock=Kanshitow_date[3][5])
        make_kansito.make_kannsito(mc, x-Kanshitow_date[0][3], z+Kanshitow_date[2][3], y=Kanshitow_date[1],
                                sityuublock=Kanshitow_date[3][1],kahenblock=Kanshitow_date[3][3],zyouhenblock=Kanshitow_date[3][5])

def make_tsuisekidan(dan_x,dan_y,dan_z):
    mc.setBlock(dan_x,dan_y,dan_z,46,0)
    x,y,z = mc.player.getPos()
    while dan_x != x and dan_y != y and dan_z != z:
        mc.setBlock(dan_x,dan_y,dan_z,0)
        if x > dan_x:
            dan_x += 1
        elif x < dan_x:
            dan_x -= 1
        else:
            dan_x = dan_x
        if y > dan_y:
            dan_y += 1
        elif y < dan_y:
            dan_y -= 1
        else:
            dan_y = dan_y
        if z > dan_z:
            dan_z += 1
        elif z < dan_z:
            dan_z -= 1
        else:
            dan_x = dan_x
        mc.setBlock(dan_x,dan_y,dan_z,46,0)
        sleep(0.5)

def make_BOSS_Head(x=0,y=5,z=0,Block_ID=[["aroundBlock",35,0],["insideBlock",42],["Hart",param.TNT,1]]):
    mc.setBlocks(x-4,y-4,z-4,x+4,y+4,z+4,Block_ID[0][1],Block_ID[0][2])#四角
    mc.setBlocks(x-3,y-4,z-5,x+3,y+4,z+5,Block_ID[0][1],Block_ID[0][2])#前
    mc.setBlocks(x-5,y-4,z-3,x+5,y+4,z+3,Block_ID[0][1],Block_ID[0][2])#横
    mc.setBlocks(x-5,y-3,z-4,x+5,y+3,z+4,Block_ID[0][1],Block_ID[0][2])#前
    mc.setBlocks(x-4,y-3,z-5,x+4,y+3,z+5,Block_ID[0][1],Block_ID[0][2])#横
    mc.setBlocks(x-3,y-5,z-4,x+3,y+5,z+4,Block_ID[0][1],Block_ID[0][2])#上
    mc.setBlocks(x-4,y-5,z-3,x+4,y+5,z+3,Block_ID[0][1],Block_ID[0][2])#上
    mc.setBlocks(x-3,y-3,z-3,x+3,y+3,z+3,Block_ID[1][1])#中心核
    mc.setBlock(x,y,z,Block_ID[2][1],Block_ID[2][2])
def make_BOSS_Fase(x=0,y=5,z=0):
    mc.setBlocks(x-6,y-3,z-5,x-6,y+3,z+5,35,7)
    mc.setBlocks(x-6,y-4,z-6,x-7,y+4,z+6,35,15)
    mc.setBlocks(x-7,y-3,z-5,x-7,y+3,z+5,0)

def make_Cercle(x=0,y=0,z=0,Scale=10,Block_ID=35):
    change_x = 0
    for j in range(0,(Scale*100)):
        Block_ID = Block_ID
        mc.setBlock(int(change_x)+x,y,int(math.sqrt(Scale*Scale-change_x*change_x))+z,Block_ID)
        mc.setBlock(int(change_x)+x,y,-int(math.sqrt(Scale*Scale-change_x*change_x))+z,Block_ID)
        mc.setBlock(-int(change_x)+x,y,int(math.sqrt(Scale*Scale-change_x*change_x))+z,Block_ID)
        mc.setBlock(-int(change_x)+x,y,-int(math.sqrt(Scale*Scale-change_x*change_x))+z,Block_ID)
        change_x += 0.01

def make_Cercle_Anime(x=0,y=0,z=0,Scale=10):
    Cercle_Scale=0
    x = 0
    for i in range(Scale):
        Cercle_Scale += 1
        x = 0
        for j in range(0,(Cercle_Scale*100)):
            Block_ID = 35
            mc.setBlock(int(x),y,int(math.sqrt(Cercle_Scale*Cercle_Scale-x*x))+z,Block_ID)
            mc.setBlock(int(x),y,-int(math.sqrt(Cercle_Scale*Cercle_Scale-x*x))+z,Block_ID)
            mc.setBlock(-int(x),y,int(math.sqrt(Cercle_Scale*Cercle_Scale-x*x))+z,Block_ID)
            mc.setBlock(-int(x),y,-int(math.sqrt(Cercle_Scale*Cercle_Scale-x*x))+z,Block_ID)
            x += 0.01
        sleep(0.01)
        x = 0
        for j in range(0,(Cercle_Scale*100)):
            Block_ID = 0
            mc.setBlock(int(x),y,int(math.sqrt(Cercle_Scale*Cercle_Scale-x*x))+z,Block_ID)
            mc.setBlock(int(x),y,-int(math.sqrt(Cercle_Scale*Cercle_Scale-x*x))+z,Block_ID)
            mc.setBlock(-int(x),y,int(math.sqrt(Cercle_Scale*Cercle_Scale-x*x))+z,Block_ID)
            mc.setBlock(-int(x),y,-int(math.sqrt(Cercle_Scale*Cercle_Scale-x*x))+z,Block_ID)
            x += 0.01
        sleep(0.01)

def make_Cercle_Anime_powerup(x=0,y=0,z=0,Scale=10,time=0.01,Block_ID=35):
    Cercle_Scale=0
    change_x = 0
    # zx= 0
    time = int(time)
    for i in range(Scale):
        Cercle_Scale += 1
        change_x = 0
        # zx = 0
        # for j in range(0,(Cercle_Scale*100)):
        #     Block_ID = 35
        #     mc.setBlock(int(change_x)+x,y,int(math.sqrt(Cercle_Scale*Cercle_Scale-change_x*change_x))+z,Block_ID)
        #     mc.setBlock(int(change_x)+x,y,-int(math.sqrt(Cercle_Scale*Cercle_Scale-change_x*change_x))+z,Block_ID)
        #     mc.setBlock(-int(change_x)+x,y,int(math.sqrt(Cercle_Scale*Cercle_Scale-change_x*change_x))+z,Block_ID)
        #     mc.setBlock(-int(change_x)+x,y,-int(math.sqrt(Cercle_Scale*Cercle_Scale-change_x*change_x))+z,Block_ID)
        #     change_x += 0.01
        make_Cercle(x,y,z,Scale=Cercle_Scale,Block_ID=Block_ID)
        sleep(time)
        change_x = 0
        # for j in range(0,(Cercle_Scale*100)):
        #     Block_ID = 0
        #     mc.setBlock(int(change_x)+x,y,int(math.sqrt(Cercle_Scale*Cercle_Scale-change_x*change_x))+z,Block_ID)
        #     mc.setBlock(int(change_x)+x,y,-int(math.sqrt(Cercle_Scale*Cercle_Scale-change_x*change_x))+z,Block_ID)
        #     mc.setBlock(-int(change_x)+x,y,int(math.sqrt(Cercle_Scale*Cercle_Scale-change_x*change_x))+z,Block_ID)
        #     mc.setBlock(-int(change_x)+x,y,-int(math.sqrt(Cercle_Scale*Cercle_Scale-change_x*change_x))+z,Block_ID)
        #     change_x += 0.01
        make_Cercle(x,y,z,Scale=Cercle_Scale,Block_ID=0)
        sleep(time)
        




# mc.postToChat("Crash PC!")
# mc.player.setPos(0,0,0)
# mc.setBlocks(-10,-10,-10,10,10,10,0)
# sleep(1)
# make_BOSS_Head(0,0,0)
# make_BOSS_Fase(0,0,0)
# make_ALL(mc,-100,0,-100,True,True,True,True,True,True,True)
# make_Cercle_Anime_powerup(-10,20,-10,10,0.05)
# make_Cercle(10,10,-10,10)