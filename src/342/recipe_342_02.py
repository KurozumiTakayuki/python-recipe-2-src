import smtplib
from email.message import EmailMessage


def send_email():
    """ メール送信関数 """

    # 1. EmailMessageオブジェクトの生成と設定
    msg = EmailMessage()
    msg['Subject'] = 'テストメールの件名'  # 件名
    msg['From'] = 'from_email@example.com'  # 送信元
    msg['To'] = 'to_email@example.com'  # 送信先
    msg.set_content("HTMLを表示できない場合に、このテキストが表示されます。")
    msg.add_alternative("""
    <html>
        <body>
            <h1>HTML形式のメール</h1>
            <p>これは<b>HTMLメール</b>です。</p>
        </body>
    </html>
    """, subtype='html')

    # 2. SMTPサーバーに接続、暗号化、認証
    try:
        with smtplib.SMTP('SMTPホスト', 587) as smtp:
            smtp.starttls()  # TLS暗号化を開始
            smtp.login('from_email@example.com', 'パスワード')  # ログイン

            # 3. メール送信
            smtp.send_message(msg)
            print("メールが送信されました。")
    except Exception as e:
        print(f"メールの送信に失敗しました: {e}")


# 実行
send_email()
