from mcpi.minecraft import Minecraft
import param_MCJE1122 as param

import make_all
import keyboard
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)

mc.postToChat("zで進める")

mc.player.setPos(0,-51,0)
story = 0
say = False
while story != 15:
    if keyboard.is_pressed('z'):
        story += 1
        say = False
        while keyboard.is_pressed("z") == True:
            if say == False:
                if story == 1:
                    mc.postToChat("???:ヤァヤァこんにちは")
                elif story == 2:
                    mc.postToChat("盗賊:俺の名前は盗賊。今からお前の師匠となるものだッ")
                elif story == 3:
                    mc.postToChat("盗賊:ちなみに盗が名字で賊が名前になってるぞ")
                elif story == 4:
                    mc.postToChat("盗賊:・・・・・")
                elif story == 5:
                    mc.postToChat("盗賊:ハイそこ‼警察に連絡しようとするんじゃあないこの汚らしい阿保がァ‼")
                elif story == 6:
                    mc.postToChat("盗賊:なにィ?口が悪いだとゥ?")
                elif story == 7:
                    mc.postToChat("盗賊:これはゲームなんだから細かいことを気にするんじゃあないッ‼")
                elif story == 8:
                    mc.postToChat("盗賊:さて、さっそくだが貴様には俺の技を伝授するッ‼")
                elif story == 9:
                    mc.postToChat("盗賊:何でかって?そりゃぁもちろん・・・")
                elif story == 10:
                    mc.postToChat("盗賊:暇つぶし")
                elif story == 11:
                    mc.postToChat("盗賊:そんなことはどうでもよいッ‼人の話を遮るんじゃあねぇこのスカタンがッ‼")
                elif story == 12:
                    mc.postToChat("盗賊:話に戻るが、最初から")
            say = True
            sleep(0.2)