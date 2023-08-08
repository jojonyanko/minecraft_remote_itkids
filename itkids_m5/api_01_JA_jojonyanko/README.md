# <<Minecraftで学ぶ!!>>　財宝の奪い方　(ストーリーあり‼)

やぁみんな、みんなは小さいころには盗賊とか怪盗とかにあこがれたことはないかい？現実ではできないとか、なんか楽しそうとかの理由で憧れる人も多いよね。そんないい歳になっても盗賊になりたい君へ‼現実でできないならMinecraftでやってしまえばいいんだ。**ないものは作るしかないからね**

## 本編に移動する前に:

このサイトはMinecraftに[Naohiro2gさん](https://github.com/jojonyanko/minecraft_remote/blob/main/README_ja.md)作のremotecontrollermod-1.16.5_0.05というMODをいれることで、PythonとMinecraftを連結させ、Minecraftの世界を操作できるようにした状態で使うことが出来る物です。こうやって書くと使うまでに随分と複雑なことをしなければならないように感じますが、あなたがやる動作はただ5つ！
### 1: Minecraftを購入して、MODを入れることが出来るようにする
- MODを使えるようにする方法

1. Javaをインストールする  
2. 使いたいMinecraftのバージョンと同じバージョンのForgeをインストールする  
3. Forgeをダブルクリックし起動させ、ダウンロードする  
4. Minecraftを起動し、「起動構成」に進み、「新規作成」を押すとバージョンを選ぶことが出来、その中にForgeと書かれたものがあるので、先ほど入れたForgeと同じバージョンのものを選択して作成する。このとき「ゲームディレクトリ」に空のフォルダ―を選択するとMODのバージョンの違うやつやバニラを遊ぶ時に変更が楽になるのでやった方がよい   
5. 「プレイ」に戻り、先ほど作った起動構成を選択してMinecraftを立ち上げる。（起動構成は左下から変更することが出来る）  
6. 起動したら画面に「MOD」または「mod」、「Mod」と書かれたボタンがあるかを確認する。本来ならそのボタンを押して中にForgeがあるかを確認した方が確実なのだが、ボタンさえあれば大体成功しているのでそのままMinecraftを閉じてもよい（もしボタンがなかったら1からやり直す）
7. 起動構成で選択したゲームディレクトリに指定したフォルダにMODなどのフォルダが追加されていると思うが、そこに入れたいMODを入れる。起動構成は新しく作ってもいいし、先ほど作ったものでもよい（しかしゲームディレクトリは同じものを選択しないといけない。）

- その方法が通用しなかったら

[!["JAVAの暴走をなきものとするMODの入れ方"](/itkids_m5/api_01_JA_jojonyanko/images/MOD.PNG)](https://www.youtube.com/embed/B-ffqFeUJxE)

<!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/B-ffqFeUJxE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> -->

### 2: remotecontrollermodを入手し、MODフォルダにぶち込む
|[remotecontrollermod 1.16.5](https://www.curseforge.com/minecraft/mc-mods/remote-controller/files/3363255)|[remotecontrollermod 1.12.2](https://www.curseforge.com/minecraft/mc-mods/remote-controller/files/3242375)|
|:--:|:--:|
### 3: VScodeなどのプログラムを実行することのできるアプリをインストールする
### 4: このリポジトリをフォークし、フォークしたものをさっきインストールしたアプリにぶち込む(VScodeなら「Clone git repositry...」というところでできる)　
※そのままこのリポジトリを使ってしまうと作品が上書きされてしまうからなし
　ちゃんとフォークしてください
### 5:Minecraftで世界に入った後にフォークしたものをぶち込んだアプリを開き、MinecraftとPythonを接続させる

これらのことをやれば、きっと使えるはず

また、本来は僕が作った[MY_REAL_API](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/MY_REAL_API.py)という物がこの作品のメインとなるものだけど、せっかくこのリポジトリをクローンして、君たちもプログラムをここで書くことが出来るので、この作品でできる機能も紹介するよ。

## ストーリー編

## 機能紹介編
### 1. チャット機能
[make_story](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/make_story.py)という部分に追加されており、二つの機能があります

**注意：Minecraftのバージョンが1.12.2の場合、日本語で書くと文字がバグる可能性があります！！**

- 1.　**story**:
    
    ここではMinecraft上のチャットをあるボタンを打った後に打つことが出来ます。storyの後に()がついており、そこに`story`と`botton="z"`というものがあると思いますが、使用する際には`story=`の後に打ちたい内容を入力し、`botton=`の後に使いたいボタンを入れてください（ボタンの名前は半角で）  
    使用例：
    ~~~Python
    from mcpi.minecraft import Minecraft
    import param_MCJE1122 as param
    mc = mc = Minecraft.create(port=param.PORT_MC)
    import make_story

    make_story.story("こんにちは！")
    #　↑　ｚキーが押された後にMinecraftのチャットで「こんにちは！」と出る

    make_story.story("さようなら！",botton="a")
    #　↑　Aキーが押された後にMinecraftのチャットで「さようなら！」と出る
    ~~~
※別に`botton`の部分は変えなくても自動でZキーが使われるようになっている

- 2.　**storys**:

    **story**では一文しかチャットを打つことが出来なかったが、こちらでは連続して複数個の文をあるボタンを打った後に打つことが出来ます。storysの後に()があり、そこに`storys=[]`と`botton="z"`というものがあると思いますが、使用するときには`storys=[]`の`[]`中に打ちたい文、`botton=`の後に使いたいボタンを入れてください（ボタンの名前は半角で）

    使用例：
    ~~~Python
    from mcpi.minecraft import Minecraft
    import param_MCJE1122 as param
    mc = mc = Minecraft.create(port=param.PORT_MC)
    import make_story

    make_story.storys(["チィース！","サイナラ～！"])
    #　↑　ｚキーを2回押すとMinecraftのチャットで最初に「チィース！」、二回目に「サイナラ～！」と出てくる

    make_story.storys(["ゴッツァンです！","もう一杯ようどすか！？","あいざいました！"],botton="a")
    #　↑　Aキーを2回押すと、Minecraftのチャットで最初に「ゴッツァンです！」、二回目に「もう一杯ようどすか！？」、三回目に「あいざいました！」と出てくる
    ~~~

### 2. 謎の施設

[make_all](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/make_all.py)にざっくりとした物、[make_insidekaidan](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/make_insidekaidan.py)、[make_kaidan](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/make_kaidan.py)、[make_kansito](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/make_kansito.py)に細かい設定のできるものが追加されています。

- 1.　**make_ALL**　（in [make_all](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/make_all.py)）

    ここではこの作品で追加された建造物のすべてを一気に作り出すことが出来ます。make_allの後に()があり、その中に`x`,`y`,`z`,`make_hontow`,`make_utikaidan`,`make_naraku`,`make_kaidow`,`make_outkaidan`,`make_kansitow`,`make_box`,
    `Hontow_date=[10,100,10,param.GOLD_BLOCK]`,`Utikaidan_date=[3,1,3,100,6,param.SEA_LANTERN_BLOCK]`,
    `Kaidow_date=[49,1,4,20,param.GLASS]`,`Outkaidan_date=[[48,4],1,[5,45,8,48],param.GLASS]`,
    `Kanshitow_date=[[16,28,28,15],76,[16,28,15,28],["Shityu",param.GLOWSTONE,"Kahen",param.GLOWSTONE,"Zyouhen",param.GLOWSTONE]]`,
    `Naraku_date=[49,100,49,300]`などなどといろいろなものがありますが、`x`,`y`,`z`はもちろんその建造物の座標を表しており、`make_hontow`～`make_box`まではその建造物を立てるかどうかを`True`と`False`で区別しています。`Hontow_date`～`Naraku_date`まではそれらの建造物のある程度の細かな設定を行うことが出来ますが、一つ一つ説明していると長くなりすぎてしまうので、make_allのコードなどを読んでどこがどこだかを自分で判断してください（つまり上級者向けです）

    使用例：
    ~~~Python
    from mcpi.minecraft import Minecraft
    import param_MCJE1122 as param
    mc = mc = Minecraft.create(port=param.PORT_MC)
    import make_all

    make_all.make_ALL(mc,x,y,z,True,True,True,True,True,True,True)
    #　↑　座標0,0,0のところにすべての建造物を作成する

    make_all.make_ALL(mc,x,y,z,True,False,False,False,False,False,False)
    #　↑　座標0,0,0のところに本棟だけを作成する

    make_all.make_ALL(mc,x+10,y,z+10,True,True,True,True,True,True,True)
    #　↑　座標10,0,10のところにすべての建造物を作成する
    ~~~
    ※ちなみに`x`,`y`,`z`を変更した状態で建造物を作成すると、本棟などはバグった物ができるのだが、逆にそちらの方が建造物としてすごい場合が多いので、よかったら自分の気に入ったバグの建造物を見つけてTwitterとかで公開してみたらどうでしょうか？（Xなんてものは知りません）

- 2 **make_insidekaidan_S/E/N/W** (in [make_insidekaidan](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/make_insidekaidan.py))

    ここでは本棟の中に作成される階段を作ることが出来ます。最後の文字がS,E,N,Wになる四つの種類のものがあり、それぞれ階段の進む方向が違います。S,E,N,Wは方位のsouth,east,north,westの頭文字ではありますが、本当にそうなっているのかはわからない（作っているときに適当な方向を北として作ったから）ので、いったんすべて試してみてから使うとよいと思います。どのmake_insidekaidanの()にも`x`,`y`,`z`,`dansu`,`insideblock`の四つがあると思いますが、`x`,`y`,`z`は建造物の座標を表しており、`dansu`は階段の段数、`insideblock`は階段を構成するブロックの種類をコントロールすることが出来ます

    使用例：
    ~~~Python
    from mcpi.minecraft import Minecraft
    import param_MCJE1122 as param
    mc = mc = Minecraft.create(port=param.PORT_MC)
    import make_insidekaidan

    make_insidekaidan.make_insidekaidan_S(mc)
    make_insidekaidan.make_insidekaidan_E(mc)
    make_insidekaidan.make_insidekaidan_N(mc)
    make_insidekaidan.make_insidekaidan_W(mc)
    #　↑　初期設定の階段をそれぞれ作成する

    make_insidekaidan.make_insidekaidan_S(mc,x=0,y=0,z=0)
    make_insidekaidan.make_insidekaidan_E(mc,x=0,y=0,z=0)
    make_insidekaidan.make_insidekaidan_N(mc,x=0,y=0,z=0)
    make_insidekaidan.make_insidekaidan_W(mc,x=0,y=0,z=0)
    #　↑　階段を座標0,0,0のところに作成する

    make_insidekaidan.make_insidekaidan_S(mc,dansu=10)
    make_insidekaidan.make_insidekaidan_E(mc,dansu=10)
    make_insidekaidan.make_insidekaidan_N(mc,dansu=10)
    make_insidekaidan.make_insidekaidan_W(mc,dansu=10)
    #　↑　階段の段数を10にし、初期設定で示されている場所に生成する

    make_insidekaidan.make_insidekaidan_S(mc,insidekaidan=param.GOLD_BLOCK)
    make_insidekaidan.make_insidekaidan_E(mc,insidekaidan=param.GOLD_BLOCK)
    make_insidekaidan.make_insidekaidan_N(mc,insidekaidan=param.GOLD_BLOCK)
    make_insidekaidan.make_insidekaidan_W(mc,insidekaidan=param.GOLD_BLOCK)
    #　↑　階段を生成するブロックを金ブロックにし、初期設定で示されている場所に初期設定で示されている段数で生成する。
    ~~~

- 3.　**make_outkaidan_ES/SW/WN/NE** (in [make_kaidan](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/make_kaidan.py))

    ここでは本棟の中の階段ではなく、本棟の外側にあった階段を作ることが出来ます。ここでもES,SW,WN,NEの四つの種類があり、ES,SW,WN,NEは方向のnorth,south,west,eastからきているのですが、やはり方向が正しくない可能性がありますので、こちらも一回すべて試してみた方がよいと思います。どのmake_outkaidanの()にも`x`,`y`,`z`,`outkaidanblock`があると思いますが、`x`,`y`,`z`は階段を作成する座標、`outkaidanblock`は階段を構成するブロックの種類をコントロールすることが出来ます。

    使用例：
    ~~~python
    from mcpi.minecraft import Minecraft
    import param_MCJE1122 as param
    mc = mc = Minecraft.create(port=param.PORT_MC)
    import make_kaidan

    make_kaidan.make_outkaidan_ES(mc,)
    make_kaidan.make_outkaidan_SW(mc,)
    make_kaidan.make_outkaidan_WN(mc,)
    make_kaidan.make_outkaidan_NE(mc,)
    #　↑　初期設定の階段をそれぞれ作成する

    make_kaidan.make_outkaidan_ES(mc,x+10,y,z+10)
    make_kaidan.make_outkaidan_SW(mc,x+10,y,z+10)
    make_kaidan.make_outkaidan_WN(mc,x+10,y,z+10)
    make_kaidan.make_outkaidan_NE(mc,x+10,y,z+10)
    #　↑　座標10,1,10のところに階段を作成する

    make_kaidan.make_outkaidan_ES(mc,outkaidanblock=param.GOLD_BLOCK)
    make_kaidan.make_outkaidan_SW(mc,outkaidanblock=param.GOLD_BLOCK)
    make_kaidan.make_outkaidan_WN(mc,outkaidanblock=param.GOLD_BLOCK)
    make_kaidan.make_outkaidan_NE(mc,outkaidanblock=param.GOLD_BLOCK)
    #　↑　初期設定の位置に金ブロックで構成された階段を作成する
    ~~~
    
- 4.　**make_insidekaidan_seihoukei_zyouhen/migi/kahen/hidari** (in [make_kaidan](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/make_kaidan.py))

    ここでは本棟の中に作成される階段を作ることが出来ます。・・・って同じようなセリフをどこかで聞いたことがありますね？
    >いや本棟の中の階段はmake_outsidekaidanで作られるんじゃないんかい  
    
    などという風に受け取った人も少なからずいると思いますが、こちらでは本棟の中の階段のおり曲がる前までのものを作り出すことが出来ます。こちらにも四っつほどの種類がありますが、もちろんすべて試した後に使った方がよいと思います。どのmake_insidekaidan_seihoukeiの()の中にも`x`,`y`,`z`,`dansu`があると思いますが、`x`,`y`,`z`は階段の作成する座標、`dansu`は階段の段数をコントロールすることが出来ます。また、`insideblock_seihoukei_zyouhen/migi/kahen/hidari`という種類によって違う名前の物があると思いますが、これらの働きはすべて同じで、階段を構成するブロックをコントロールすることが出来ます。

    使用例：
    ~~~python
    from mcpi.minecraft import Minecraft
    import param_MCJE1122 as param
    mc = mc = Minecraft.create(port=param.PORT_MC)
    import make_kaidan

    make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,)
    make_kaidan.make_insidekaidan_seihoukei_migi(mc,)    
    make_kaidan.make_insidekaidan_seihoukei_kahen(mc,)
    make_kaidan.make_insidekaidan_seihoukei_hidari(mc,)
    #　↑　初期設定の階段をそれぞれ作成する

    make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,x=10,y=0,z=10)
    make_kaidan.make_insidekaidan_seihoukei_migi(mc,x=10,y=0,z=10)
    make_kaidan.make_insidekaidan_seihoukei_kahen(mc,x=10,y=0,z=10)
    make_kaidan.make_insidekaidan_seihoukei_hidari(mc,x=10,y=0,z=10)
    #　↑　座標10,0,10の所に階段を作成する

    make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,dansu=10)
    make_kaidan.make_insidekaidan_seihoukei_migi(mc,dansu=10)    
    make_kaidan.make_insidekaidan_seihoukei_kahen(mc,dansu=10)
    make_kaidan.make_insidekaidan_seihoukei_hidari(mc,dansu=10)
    #　↑　段数が10の階段を初期設定の位置に作成する

    make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,insideblock_seihoukei_zyouhen=param.GOLD_BLOCK)
    make_kaidan.make_insidekaidan_seihoukei_migi(mc,insideblock_seihoukei_migi=param.GOLD_BLOCK)
    make_kaidan.make_insidekaidan_seihoukei_kahen(mc,insideblock_seihoukei_kahen=param.GOLD_BLOCK)
    make_kaidan.make_insidekaidan_seihoukei_hidari(mc,insideblock_seihoukei_hidari=param.GOLD_BLOCK)
    #　↑　初期設定の位置で初期設定の段数分の階段を金ブロックで作成する
    ~~~

- 5.　**make_kannsito** (in [make_kansito](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/make_kansito.py))
    
    ここでは監視塔のような建造物を作ることが出来ます。make_kannsitoの()の中には`x`,`z`,`y`,`sityuublock`,`kahenblock`,`zyouhenblock`の五つがあると思いますが、`x`,`z`,はその建造物を作成する座標、`y`は監視塔の高さ、`sityuublock`は監視塔の支柱のような部分を構成するブロック、`kahenblock`は監視塔の人のいそうな部分の下半分を構成するブロック、`zyouhenblock`は監視塔の人のいそうな部分の上半分を構成するブロックをコントロールすることが出来ます。

    使用例：
    ~~~python
    from mcpi.minecraft import Minecraft
    import param_MCJE1122 as param
    mc = mc = Minecraft.create(port=param.PORT_MC)
    import make_kansito

    make_kansito.make_kannsito(mc,)
    #　↑　初期設定の監視塔を作成する

    make_kansito.make_kannsito(mc,x=10,z=10)
    #　↑　座標10,1,10に監視塔を作成する

    make_kansito.make_kannsito(mc,y=100)
    #　↑　y座標が1から100までの高さの監視塔を作成する

    make_kansito.make_kannsito(mc,sityuublock=param.GOLD_BLOCK,kahenblock=param.SEA_LANTERN_BLOCK,zyouhenblock=param.GLASS)
    #　↑　初期設定の位置と高さの、支柱のような部分が金ブロックで人がいそうな場所の下半分がシーランタンブロック、上半分がガラスブロックで構成されていいる監視塔を作成する
    ~~~
- 6.　**make_honto** (in [make_kansito](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/make_kansito.py))

    ここでは本棟を作成することが出来ます。make_hontoの()の中には`x`,`y`,`z`,`tyusinblock`の四つがあると思いますが、`x`,`z`は本棟のスケール（幅）、`y`は高さ、`tyusinblock`は本棟のガラスに囲まれているブロック（初期だと金ブロック）をコントロールすることが出来ます。

    ~~~python
    from mcpi.minecraft import Minecraft
    import param_MCJE1122 as param
    mc = mc = Minecraft.create(port=param.PORT_MC)
    import make_kansito

    make_kansito.make_honto(mc,)
    #　↑　初期設定の本棟を作る

    make_kansito.make_honto(mc,x=13,z=13)
    #　↑　x,z座標ともに-13~13までの幅の本棟を作る

    make_kansito.make_honto(mc,y=100)
    #　↑　y座標0～100までの高さの本棟を作る

    make_kansito.make_honto(mc,tyusinblock=param.GLASS)
    #　↑　ガラスに囲まれているブロックがガラス、つまりガラスの本棟を作る
    ~~~

- 7.　**make_kaidow** (in [make_kansito](https://github.com/jojonyanko/minecraft_remote_itkids/blob/main/itkids_m5/api_01_JA_jojonyanko/make_kansito.py))

    ここでは街道（ガラスの通路）を作成することが出来ます。make_kaidowの()の中に、`x`,`y`,`z`,`y_plas`,`kaidowblock`の四つがあると思いますが、`x`は街道の長さ、`z`は街道の幅（街道の内側の長さ）、`y`は街道のy座標、`y_plas`は街道を上方向に複製していくときの街道と街道との間の長さ、`kaidowblock`は街道を構成するブロックをコントロールすることが出来ます。

    使用例：
    ~~~python
    from mcpi.minecraft import Minecraft
    import param_MCJE1122 as param
    mc = mc = Minecraft.create(port=param.PORT_MC)
    import make_kansito

    make_kansito.make_kaidow(mc,)
    #　↑　初期設定の街道を作成する

    make_kansito.make_kaidow(mc,x=100,z=10)
    #　↑　-100～100までの長さの、内側の幅が-10～10ある街道を作成する

    make_kansito.make_kaidow(mc,y=10)
    #　↑　y座標が10のところに初期設定の街道を作成する

    make_kansito.make_kaidow(mc,x_plas=50)
    #　↑　50ごとの間隔をあけて街道が上に複製されていく

    make_kansito.make_kaidow(mc,x_plas=0)
    #　↑　街道が一つ（一クロス）作成される

    make_kansito.make_kaidow(mc,kaidowblock=param.GOLD_BLOCK)
    #　↑　金ブロックで構成されている初期設定の街道ができる
    ~~~