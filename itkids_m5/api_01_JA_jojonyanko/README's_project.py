from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
mc = mc = Minecraft.create(port=param.PORT_MC)
import make_story
import make_all
import make_insidekaidan
import make_kaidan
import make_kansito

def one_story():
    make_story.Story("こんにちは！")
    #　↑　ｚキーが押された後にMinecraftのチャットで「こんにちは！」と出る

    make_story.Story("さようなら！",botton="a")
    #　↑　Aキーが押された後にMinecraftのチャットで「さようなら！」と出る

def two_storys():
    make_story.Storys(["チィース！","サイナラ～！"])
    #　↑　ｚキーを2回押すとMinecraftのチャットで最初に「チィース！」、二回目に「サイナラ～！」と出てくる

    make_story.Storys(["ゴッツァンです！","もう一杯ようどすか！？","あいざいました！"],botton="a")
    #　↑　Aキーを2回押すと、Minecraftのチャットで最初に「ゴッツァンです！」、二回目に「もう一杯ようどすか！？」、三回目に「あいざいました！」と出てくる

def three_make_ALL(select):
    if(select==1):
        make_all.make_ALL(mc,0,0,0,True,True,True,True,True,True,True)
        #　↑　座標0,0,0のところにすべての建造物を作成する

    elif (select==2):
        make_all.make_ALL(mc,0,0,0,True,False,False,False,False,False,False)
        #　↑　座標0,0,0のところに本棟だけを作成する

    elif(select==3):
        make_all.make_ALL(mc,10,0,10,True,True,True,True,True,True,True)
        #　↑　座標10,0,10のところにすべての建造物を作成する

    else:
        mc.postToChat("You must select 1 or 2 or 3 in program")

def four_make_insidekaidan_S_E_M_N(select):
    if(select == 1):
        make_insidekaidan.make_insidekaidan_S(mc)
        make_insidekaidan.make_insidekaidan_E(mc)
        make_insidekaidan.make_insidekaidan_N(mc)
        make_insidekaidan.make_insidekaidan_W(mc)
        #　↑　初期設定の階段をそれぞれ作成する

    elif(select == 2):
        make_insidekaidan.make_insidekaidan_S(mc,x=0,y=0,z=0)
        make_insidekaidan.make_insidekaidan_E(mc,x=0,y=0,z=0)
        make_insidekaidan.make_insidekaidan_N(mc,x=0,y=0,z=0)
        make_insidekaidan.make_insidekaidan_W(mc,x=0,y=0,z=0)
        #　↑　階段を座標0,0,0のところに作成する

    elif(select == 3):
        make_insidekaidan.make_insidekaidan_S(mc,dansu=10)
        make_insidekaidan.make_insidekaidan_E(mc,dansu=10)
        make_insidekaidan.make_insidekaidan_N(mc,dansu=10)
        make_insidekaidan.make_insidekaidan_W(mc,dansu=10)
        #　↑　階段の段数を10にし、初期設定で示されている場所に生成する

    elif(select == 4):
        make_insidekaidan.make_insidekaidan_S(mc,insideblock=param.GOLD_BLOCK)
        make_insidekaidan.make_insidekaidan_E(mc,insideblock=param.GOLD_BLOCK)
        make_insidekaidan.make_insidekaidan_N(mc,insideblock=param.GOLD_BLOCK)
        make_insidekaidan.make_insidekaidan_W(mc,insideblock=param.GOLD_BLOCK)
        #　↑　階段を生成するブロックを金ブロックにし、初期設定で示されている場所に初期設定で示されている段数で生成する。

    else:
        mc.postToChat("You must select 1 or 2 or 3 or 4 in program")

def five_make_outkaidan_SE_EW_WN_NS(select):
    if(select == 1):
        make_kaidan.make_outkaidan_ES(mc,)
        make_kaidan.make_outkaidan_SW(mc,)
        make_kaidan.make_outkaidan_WN(mc,)
        make_kaidan.make_outkaidan_NE(mc,)
        #　↑　初期設定の階段をそれぞれ作成する

    elif(select == 2):
        make_kaidan.make_outkaidan_ES(mc,10,1,10)
        make_kaidan.make_outkaidan_SW(mc,10,1,10)
        make_kaidan.make_outkaidan_WN(mc,10,1,10)
        make_kaidan.make_outkaidan_NE(mc,10,1,10)
        #　↑　座標10,1,10のところに階段を作成する

    elif(select == 3):
        make_kaidan.make_outkaidan_ES(mc,outkaidanblock=param.GOLD_BLOCK)
        make_kaidan.make_outkaidan_SW(mc,outkaidanblock=param.GOLD_BLOCK)
        make_kaidan.make_outkaidan_WN(mc,outkaidanblock=param.GOLD_BLOCK)
        make_kaidan.make_outkaidan_NE(mc,outkaidanblock=param.GOLD_BLOCK)
        #　↑　初期設定の位置に金ブロックで構成された階段を作成する

    else:
        mc.postToChat("You must select 1 or 2 or 3 in program")

def six_make_insidekaidan_seihoukei_zyouhen_migi_kahen_hidari(select):
    if(select == 1):
        make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,)
        make_kaidan.make_insidekaidan_seihoukei_migi(mc,)    
        make_kaidan.make_insidekaidan_seihoukei_kahen(mc,)
        make_kaidan.make_insidekaidan_seihoukei_hidari(mc,)
        #　↑　初期設定の階段をそれぞれ作成する

    elif(select == 2):
        make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,x=10,y=0,z=10)
        make_kaidan.make_insidekaidan_seihoukei_migi(mc,x=10,y=0,z=10)
        make_kaidan.make_insidekaidan_seihoukei_kahen(mc,x=10,y=0,z=10)
        make_kaidan.make_insidekaidan_seihoukei_hidari(mc,x=10,y=0,z=10)
        #　↑　座標10,0,10の所に階段を作成する

    elif(select == 3):
        make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,dansu=10)
        make_kaidan.make_insidekaidan_seihoukei_migi(mc,dansu=10)    
        make_kaidan.make_insidekaidan_seihoukei_kahen(mc,dansu=10)
        make_kaidan.make_insidekaidan_seihoukei_hidari(mc,dansu=10)
        #　↑　段数が10の階段を初期設定の位置に作成する

    elif(select == 4):
        make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,insideblock_seihoukei_zyouhen=param.GOLD_BLOCK)
        make_kaidan.make_insidekaidan_seihoukei_migi(mc,insideblock_seihoukei_migi=param.GOLD_BLOCK)
        make_kaidan.make_insidekaidan_seihoukei_kahen(mc,insideblock_seihoukei_kahen=param.GOLD_BLOCK)
        make_kaidan.make_insidekaidan_seihoukei_hidari(mc,insideblock_seihoukei_hidari=param.GOLD_BLOCK)
        #　↑　初期設定の位置で初期設定の段数分の階段を金ブロックで作成する

    else:
        mc.postToChat("You must select 1 or 2 or 3 or 4 in program")

def seven_make_kansito(select):
    if(select == 1):
        make_kansito.make_kannsito(mc,)
        #　↑　初期設定の監視塔を作成する

    elif(select == 2):
        make_kansito.make_kannsito(mc,x=10,z=10)
        #　↑　座標10,1,10に監視塔を作成する

    elif(select == 3):
        make_kansito.make_kannsito(mc,y=100)
        #　↑　y座標が1から100までの高さの監視塔を作成する

    elif(select == 4):
        make_kansito.make_kannsito(mc,sityuublock=param.GOLD_BLOCK,kahenblock=param.SEA_LANTERN_BLOCK,zyouhenblock=param.GLASS)
        #　↑　初期設定の位置と高さの、支柱のような部分が金ブロックで人がいそうな場所の下半分がシーランタンブロック、上半分がガラスブロックで構成されていいる監視塔を作成する

    else:
        mc.postToChat("You must select 1 or 2 or 3 or 4 in program.")

def eight_make_hontow(select):
    if(select == 1):
        make_kansito.make_honto(mc,)
        #　↑　初期設定の本棟を作る

    elif(select == 2):
        make_kansito.make_honto(mc,x=13,z=13)
        #　↑　x,z座標ともに-13~13までの幅の本棟を作る

    elif(select == 3):
        make_kansito.make_honto(mc,y=100)
        #　↑　y座標0～100までの高さの本棟を作る

    elif(select == 4):
        make_kansito.make_honto(mc,tyusinblock=param.GLASS)
        #　↑　ガラスに囲まれているブロックがガラス、つまりガラスの本棟を作る

    else:
        mc.postToChat("You must select 1 or 2 or 3 or 4 in program")

def nine_make_kaidow(select):
    if(select == 1):
        make_kansito.make_kaidow(mc,)
        #　↑　初期設定の街道を作成する

    elif(select == 2):
        make_kansito.make_kaidow(mc,x=100,z=10)
        #　↑　-100～100までの長さの、内側の幅が-10～10ある街道を作成する

    elif(select == 3):
        make_kansito.make_kaidow(mc,y=10)
        #　↑　y座標が10のところに初期設定の街道を作成する

    elif(select == 4):
        make_kansito.make_kaidow(mc,y_plas=50)
        #　↑　50ごとの間隔をあけて街道が上に複製されていく

    elif(select == 5):
        make_kansito.make_kaidow(mc,y_plas=0)
        #　↑　街道が一つ（一クロス）作成される

    elif(select == 6):
        make_kansito.make_kaidow(mc,kaidowblock=param.GOLD_BLOCK)
        #　↑　金ブロックで構成されている初期設定の街道ができる

    else:
        mc.postToChat("You must select number from 1 to 6 in program.")

# mc.setBlocks(-125,-125,-125,150,125,125,0)
# one_story
# two_storys
# three_make_ALL(select=1)
# three_make_ALL(select=2)
# three_make_ALL(select=3)
# four_make_insidekaidan_S_E_M_N(select=1)
# four_make_insidekaidan_S_E_M_N(select=2)
# four_make_insidekaidan_S_E_M_N(select=3)
# four_make_insidekaidan_S_E_M_N(select=4)
# five_make_outkaidan_SE_EW_WN_NS(select=1)
# five_make_outkaidan_SE_EW_WN_NS(select=2)
# five_make_outkaidan_SE_EW_WN_NS(select=3)
# six_make_insidekaidan_seihoukei_zyouhen_migi_kahen_hidari(select=1)
# six_make_insidekaidan_seihoukei_zyouhen_migi_kahen_hidari(select=2)
# six_make_insidekaidan_seihoukei_zyouhen_migi_kahen_hidari(select=3)
# six_make_insidekaidan_seihoukei_zyouhen_migi_kahen_hidari(select=4)
# seven_make_kansito(select=1)
# seven_make_kansito(select=2)
# seven_make_kansito(select=3)
# seven_make_kansito(select=4)
# eight_make_hontow(select=1)
# eight_make_hontow(select=2)
# eight_make_hontow(select=3)
# eight_make_hontow(select=4)
# nine_make_kaidow(select=1)
# nine_make_kaidow(select=2)
# nine_make_kaidow(select=3)
# nine_make_kaidow(select=4)
# nine_make_kaidow(select=5)
# nine_make_kaidow(select=6)

make_story.Storys(["Hello","Hi","Good morning","How aｚre you?"])

make_story.Storys(["Goodbye","Thank you","See you again"],"a")

# make_story.Story("You can try this program!","a")