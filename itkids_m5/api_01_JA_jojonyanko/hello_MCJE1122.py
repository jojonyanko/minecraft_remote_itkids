# Hello World for Minecraft Java Edition 1.12.2 or earlier
from mcje.minecraft import Minecraft
import param_MCJE1122 as param
import mcpi.entity as entity

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello Minecraft Java Edition 1.12.2')
mc.setBlocks(-5, 63, 5,  -5, 127, 5,  param.GOLD_BLOCK)
mc.spawnEntity(0,0,0,entity.WITHER)