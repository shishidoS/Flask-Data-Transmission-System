以下は、あなたのプロジェクト用に整形した `README.md` にそのままコピペできる内容です：

---

````markdown
# Flask Data Transmission System

このプロジェクトは、Flaskを使用してデータを受信し、別の端末からデータを送信するシステムです。  
`server_mojule.py` はFlaskサーバーとして動作し、`send_mojule.py` はデータ送信を行うクライアントスクリプトです。

---

## 🛠 機能概要

### Flaskサーバー (`server_mojule.py`)
- `/` エンドポイントで受信したメッセージを確認できます。
- `/receive` エンドポイントで POST リクエストを受信し、データを処理します。

### データ送信スクリプト (`send_mojule.py`)
- ユーザーが入力したデータを指定されたエンドポイントに送信します。
- `1` または `2` の入力に基づいて、「出勤」または「退勤」のステータスを送信します。

---

## 📦 必要条件

- Python 3.7以上  
- 必要なPythonライブラリ:
  - Flask  
  - requests

---

## ⚙️ セットアップ手順

1. リポジトリをクローン
```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
````

2. 必要なライブラリをインストール

```bash
pip install -r requirements.txt
```

3. Flaskサーバーを起動

```bash
python3 server_mojule.py
```

> サーバーはデフォルトで [http://0.0.0.0:5000](http://0.0.0.0:5000) で動作します。

4. 別の端末でデータ送信スクリプトを実行

```bash
python3 send_mojule.py
```

---

## 🚀 使用方法

### Flaskサーバー

* `server_mojule.py` を実行すると以下のエンドポイントが利用可能になります:

| エンドポイント    | 説明                    |
| ---------- | --------------------- |
| `/`        | 受信したメッセージの確認画面        |
| `/receive` | POSTリクエストを受信して処理するAPI |

---

### データ送信スクリプト

* スクリプト実行時、以下の入力が求められます:

  1. `送信データ`（任意のテキスト）
  2. `値入力`（`1`: 出勤、`2`: 退勤）

* 入力された内容が `/receive` に送信され、サーバー側で処理されます。

---

## 🧪 サンプル実行

### サーバー起動

```bash
$ python server_mojule.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

### クライアント送信

```bash
$ python send_mojule.py
送信データ➡ 山田太郎  
値入力（1で出勤2で退勤）: 1  
結果: {"status": "success", "message": "Message received and saved."}
```

---

## ⚠️ 注意事項

* サーバーの `/receive` エンドポイントは ngrok を使って公開されています。
  例: `https://9343-125-103-211-238.ngrok-free.app/receive`

  ngrokのセッションが切れるとURLは無効になるため、必要に応じて新しいURLを `send_mojule.py` に設定してください。

* セキュリティのため、**公開環境での運用時はHTTPS対応を推奨**します。

---

## 📁 ディレクトリ構成

```
/project-root
├── server_mojule.py      # Flaskサーバースクリプト
├── send_mojule.py        # データ送信スクリプト
├── requirements.txt      # 必要なライブラリ
└── README.md             # このファイル
