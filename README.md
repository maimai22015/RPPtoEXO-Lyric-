<!-- wp:paragraph -->
<p>皆さんごきげんよう。まいまいです。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>今回は、人力系音MADで多用する表現のリップシンク（歌声に合わせて口の形を変える表現)を一部自動化するPythonスクリプトを作ったので公開します。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>今回作ったスクリプトは、Pythonの実行環境が必要になります。GUIとか作って使いやすいようにすることもできましたが、面倒なのでパスです。sry</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>概要</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>今回作ったスクリプトは、REAPERのプロジェクトファイル内の歌詞情報を参照し、歌詞の母音に対応した動画ファイルをタイミングを合わせて配置したEXOファイル(Aviutlで利用できる形式)を生成するものです。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>ダウンロードは私のGithubページから可能です。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://github.com/maimai22015/RPPtoEXO-Lyric-">https://github.com/maimai22015/RPPtoEXO-Lyric-</a></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>事前準備</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>まず前提としてPythonの実行環境を用意してください。追加で導入が必要なライブラリは無いはずです。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Python実行環境が無い人向けにGoogle collabのノートを作るかも知れませんが期待しないでください。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>REAPER上での準備</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>まず、MIDIを用意します。</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":1229,"width":580,"height":312,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://ytpmv.info/wp-content/uploads/2022/01/image.png" alt="" class="wp-image-1229" width="580" height="312"/><figcaption>テーマ適用してるのでちょっと画面違います</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>矢印で記したボタンを押して楽譜エディタを開きます。</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":1230,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://ytpmv.info/wp-content/uploads/2022/01/image-1-1024x485.png" alt="" class="wp-image-1230"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>適当な音符を選択し、右クリックから歌詞を選び、音符ごとに歌詞をひらがなで入力します。</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":1231,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://ytpmv.info/wp-content/uploads/2022/01/image-2-1024x249.png" alt="" class="wp-image-1231"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>音符ごと、ひらがなの入力じゃないと生成に失敗します。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>次に、MIDIを選択して、midi2itemスクリプトを実行し、メディアオブジェクトを生成します。</p>
<!-- /wp:paragraph -->

<!-- wp:embed {"url":"https://ytpmv.info/ReaScript-midi2item/","type":"wp-embed","providerNameSlug":"ytpmv-info","className":""} -->
<figure class="wp-block-embed is-type-wp-embed is-provider-ytpmv-info wp-block-embed-ytpmv-info"><div class="wp-block-embed__wrapper">
https://ytpmv.info/ReaScript-midi2item/
</div></figure>
<!-- /wp:embed -->

<!-- wp:image {"id":1232,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://ytpmv.info/wp-content/uploads/2022/01/image-3-1024x274.png" alt="" class="wp-image-1232"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>ここまでできたらREAPER上での準備は完了です。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>ちなみに、スクリプトで見ているのは歌詞のテキストと、メディアオブジェクトの開始・終了タイミングだけなので、MIDIの音程や音符の位置はどうでもいいです。MIDIなんて作ってないよって人は、空のMIDIアイテムを一番上のトラックに配置し、メディアオブジェクトの数だけ適当な長さの音符を配置して歌詞を入力してください。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>スクリプトの設定</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>現時点で一般公開向けに親切な設計にしていないので、実行の前にスクリプトを直接弄ることが必須になります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>GithubからDLしたファイル群のうち、setting.pyをテキストエディタで開きます。</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":1233,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://ytpmv.info/wp-content/uploads/2022/01/image-4.png" alt="" class="wp-image-1233"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>次のように書き換えてください。</p>
<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock -->
<pre class="EnlighterJSRAW" data-enlighter-language="generic" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">RPPpath = r"RPPファイルのあるパス"
TEMPLATEPath = r"template.exoのパス"
LIPPath = r"あ、い、う、え、お、んの形の口パクの動画ファイルのパス。フォルダのパス\*.aviと設定。"
ExportPath = "書き出す先のexoファイル"
FPS = 60
</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->
<p>これで準備完了です。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>実行</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>script.pyを実行してください。setting.pyで設定したexoファイルが生成されるはずです。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>細々した説明</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>透過avi以外で実行しようとするとエラーが出るので、templete.exoを編集して、二箇所の「アルファチャンネルを読み込む=1」を「アルファチャンネルを読み込む=0」に書き換えてください。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>他にもtemplete.exo編集すると好きなようにできます。書かれてる内容から察して編集してください。</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>なんか他に書くべきことがあった気がするけど思い出せないので終わります。思い出したら追記する。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>ノシ</p>
<!-- /wp:paragraph -->
