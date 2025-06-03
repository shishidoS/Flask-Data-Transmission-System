Flask Data Transmission System
このプロジェクトは、Flaskを使用してデータを受信し、別の端末からデータを送信するシステムです。server_mojule.pyはFlaskサーバーとして動作し、send_mojule.pyはデータ送信を行うクライアントスクリプトです。

機能概要
Flaskサーバー (server_mojule.py)

/ エンドポイントで受信したメッセージを確認できます。
/receive エンドポイントでPOSTリクエストを受信し、データを処理します。
データ送信スクリプト (send_mojule.py)

ユーザーが入力したデータを指定されたエンドポイントに送信します。
1 または 2 の入力に基づいて「出勤」または「退勤」のステータスを送信します。
必要条件
Python 3.7以上
必要なPythonライブラリ:
Flask
requests
セットアップ手順
リポジトリをクローン
git clone https://github.com/your-username/your-repository.git
cd your-repository

必要なライブラリをインストール
pip install -r requirements.txt

Flaskサーバーを起動
python3 server_mojule.py

server_mojule.pyを実行してサーバーを起動します。
サーバーはデフォルトでhttp://0.0.0.0:5000で動作します。
データ送信スクリプトを実行

別の端末でsend_mojule.pyを実行します。

使用方法
Flaskサーバー
サーバーを起動すると、以下のエンドポイントが利用可能になります:

/: 受信したメッセージを確認するためのエンドポイント。
/receive: POSTリクエストを受信するエンドポイント。
/receiveエンドポイントにデータを送信すると、サーバーがデータを受信し、処理結果を返します。

データ送信スクリプト
スクリプトを実行すると、以下の入力を求められます:

送信データ: 任意のテキストを入力してください。
値入力: 1（出勤）または 2（退勤）を入力してください。
入力に基づいて、データがサーバーに送信されます。

サンプル実行


Flaskサーバーの起動
$ python server_mojule.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)


データ送信スクリプトの実行
$ python send_mojule.py
送信データ➡ 山田太郎
値入力（1で出勤2で退勤）: 1
結果: {"status": "success", "message": "Message received and saved."}

注意事項
サーバーのエンドポイントURL（https://9343-125-103-211-238.ngrok-free.app/receive）は、ngrokを使用してトンネリングされています。ngrokのセッションが切れるとURLが無効になるため、必要に応じて新しいURLを設定してください。
セキュリティのため、公開環境で使用する際はHTTPSを有効にしてください。
ディレクトリ構造
/flask_test
├── server_mojule.py   # Flaskサーバーコード
├── send_mojule.py     # データ送信スクリプト
├── requirements.txt   # 必要なライブラリ
└── README.md          # プロジェクトの説明