from mcje.minecraft import Minecraft
import param_MCJE as param

import make_kansito 
import make_kaidan
import make_insidekaidan

mc = Minecraft.create(port=param.PORT_MC)
def make_ALL(mc,x,y,z,make_hontow,make_utikaidann,make_naraku,make_kaidow,make_outkaidan,make_kansitow,make_box):
    if make_naraku == True:
        if make_box == True:
            mc.setBlocks(-50,1,-50,50,111,50,param.GLASS)    
        mc.setBlocks(-49,0,-49,49,300,49,param.AIR)
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