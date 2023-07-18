# from mcje.minecraft import Minecraft
# import param_MCJE as param

from mcpi.minecraft import Minecraft
import param_MCJE1122 as param

import make_kansito 
import make_kaidan
import make_insidekaidan
import time

mc = Minecraft.create(port=param.PORT_MC)
def make_ALL(mc,x,y,z,make_hontow,make_utikaidann,make_naraku,make_kaidow,make_outkaidan,make_kansitow,make_box):
    if make_naraku == True:
        if make_box == True:
            mc.setBlocks(-50,1,-50,50,111,50,param.GLASS)    
        mc.setBlocks(-49,-100,-49,49,300,49,param.AIR)
    if make_hontow == True:
        make_kansito.make_honto(mc)
        if make_kaidow == True:
            make_kansito.make_kaidow(mc)
            if make_outkaidan ==True:
                make_kaidan.make_outkaidan_ES(mc)
                make_kaidan.make_outkaidan_SW(mc)
                make_kaidan.make_outkaidan_WN(mc)
                make_kaidan.make_outkaidan_NE(mc)
            if make_utikaidann == True:
                mc.setBlocks(-3,2,-3,3,100,3,param.AIR)
                mc.setBlocks(-2,100,-2,2,101,2,param.AIR)
                make_insidekaidan.make_insidekaidan_S(mc,)
                make_insidekaidan.make_insidekaidan_E(mc,)
                make_insidekaidan.make_insidekaidan_N(mc,)
                make_insidekaidan.make_insidekaidan_W(mc,)
    if make_kansito == True:
        make_kansito.make_kannsito(mc, x= -16, z= -16)
        make_kansito.make_kannsito(mc, x=28, z=28)
        make_kansito.make_kannsito(mc, x= 28, z= -15)
        make_kansito.make_kannsito(mc, x= -15, z= 28)

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
        time.sleep(0.5)

def make_BOSS_Head(x=0,y=5,z=0):
    mc.setBlocks(x-4,y-4,z-4,x+4,y+4,z+4,35,0)#四角
    mc.setBlocks(x-3,y-4,z-5,x+3,y+4,z+5,35,0)#前
    mc.setBlocks(x-5,y-4,z-3,x+5,y+4,z+3,35,0)#横
    mc.setBlocks(x-5,y-3,z-3,x+5,y+3,z+3,35,0)#前
    mc.setBlocks(x-3,y-3,z-5,x+3,y+3,z+5,35,0)#横
    mc.setBlocks(x-3,y-3,z-3,x+3,y+3,z+3,42)#中心核
    mc.setBlock(x,y,z,param.TNT,1)
