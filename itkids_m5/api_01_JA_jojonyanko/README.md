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
<iframe width="560" height="315" src="https://www.youtube.com/embed/B-ffqFeUJxE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

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
    ※ちなみに`x`,`y`,`z`を変更した状態で建造物を作成すると、本棟などはバグった物ができるのだが、逆にそちらの方が建造物としてすごい場合が多いので、よかったら自分の気に入ったバグの建造物を見つけてTwitterとかで公開してみたらどうだろうか？



