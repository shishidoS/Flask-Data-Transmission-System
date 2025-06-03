from flask import Flask, request


app = Flask(__name__)
received_message = ""  # 受信したメッセージ格納用変数

@app.route('/receive', methods=['POST'])#ページの定義のため登録ページにて適応してください
def receive():
    global received_message # グローバル変数として受信メッセージを使用
    data = request.get_json() # JSON形式でデータを受信をして変数に格納
    if data and "送信データ" in data: # 受信データが存在するか確認入っていたらTrueで動作する
        received_message = data["送信データ"]  # 変数に受信メッセージ保存
        return "データ受信完了", 200 # 成功時レスポンスメッセージをラズパイ側に返す
    else:
        return "メッセージエラー", 400 #ない場合リクエストエラーを返す

@app.route('/')
def home():  # エラー確認用　データ送受信の確認を返すためのもの
    if received_message:
        msg = received_message  #msgにメッセージを格納して返り値に
    else:
        msg = "まだメッセージはありません"
    return f"メッセージ: {msg}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)# Flaskサーバーを起動した際のローカル指定ポート（トンネリングorサーバー化するため初期設定用）
