# ObservationHill
Twitterアカウントをツイート数とフォロワーの動向から不審指数を返すPythonアプリです

## インストール
1. pip install
```
pip install git+https://github.com/ikarostech/ObservationHill.git
```
2. .env fileをパッケージディレクトリに追加
ObservationHill/ObservationHill中にある.env環境設定ファイルをパッケージディレクトリに入れる

## 起動
```
$ ObservationHill
```

## 動かし方
1. 認証
起動後表示されるURLに従ってTwitterの認証を行ってください

2. 対象のTwitterユーザーIDを入力
ここで quit とタイプするとプログラムは終了します。

3. 不審指数が返ってくる

## 不審指数
不審指数は以下の式で算出されます
```
不審指数 =  フォロワー数^2 / (ツイート数 * フォロー数)
```

ObservationHillではこの不審指数を
- 対象のユーザー    (A)
- 対象のユーザーのフォロワー20名    (B)
- (A) / (B)
について算出します。

~~誰かいい算出方法とか教えて~~
