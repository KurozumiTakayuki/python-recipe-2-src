from email.message import EmailMessage
import mimetypes

# メールの作成
msg = EmailMessage()
msg['Subject'] = 'ファイル添付テスト'
msg['From'] = 'sender@example.com'
msg['To'] = 'recipient@example.com'
msg.set_content('添付ファイルを送信します。')

# 添付ファイルのパス
file_path = 'example.pdf'

# ファイルを添付
with open(file_path, 'rb') as f:

    # MIMEタイプを自動的に取得
    mime_type, encoding = mimetypes.guess_type(file_path)
    print(mime_type, encoding)
    if mime_type is None:
        mime_type = 'application/octet-stream'  # 不明な場合は汎用バイナリとして扱う
    main_type, sub_type = mime_type.split('/')

    # 添付ファイルを追加
    msg.add_attachment(f.read(), maintype=main_type, subtype=sub_type, filename=f.name, params={'charset': 'utf-8'})

# 送信処理は前項と同様なので省略
