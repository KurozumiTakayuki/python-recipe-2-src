import imaplib
from email import message_from_bytes, policy

# IMAPサーバーに接続
imap = imaplib.IMAP4_SSL("IMAPサーバーホスト")
imap.login("myname@example.com", "パスワード")

# INBOXを選択
imap.select("INBOX")

# 最新のメールIDを取得
status, messages = imap.search(None, "ALL")
latest_email_id = messages[0].split()[-1]  # 最新のメールID（最後尾のメッセージシーケンス番号を取得）

# メールを取得
status, msg_data = imap.fetch(latest_email_id, "(RFC822)")

# バイナリデータを取得し、EmailMessage に変換
raw_email = msg_data[0][1]
msg = message_from_bytes(raw_email, policy=policy.default)

# ログアウト
imap.logout()
