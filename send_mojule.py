import requests
import sys
from datetime import datetime

day = datetime.now().strftime('%Y-%m-%d')#dayは年度と月、日にち取得
times = datetime.now().strftime('%H:%M') #timesは時間と分取得
names = input("送信データ➡")#送信する任意のテキストを格納可能
status=input("値入力（1で出勤2で退勤）:") #入力テキスト次第で分岐する用の変数1,2で分岐は仮置きなので変更推奨

def send_message(status):  # statusは入力テキストで内容でどちらか判断する
    # statusを「1」または「2」に応じて「出勤」または「退勤」にエラー時は再処理用にテキストか例外処理を適応する
    if status == "1":
        status_text = "出勤"
    elif status == "2":
        status_text = "退勤"
    else:
        status_text = "エラー: 1または2で選択してください"
    try:
        res = requests.post(
            "https://9343-125-103-211-238.ngrok-free.app/receive",  # 送り先URL（Flask動作アドレス）設定,現在はngrokのトンネリングアドレスを使用
            json={"送信データ": f"日＝{day},時間＝{times}, 入力テキスト＝{names}, status={status_text}"}# 送信するデータをJson形式で指定
        )
        print("結果:", res.text) # 成功レスポンスをラズパイ側に返す、読み取り失敗時、失敗メッセージが表示される
    except Exception as e:
        print("送信失敗:", e) # 例外処理で送信失敗


send_message(status) #動作関数