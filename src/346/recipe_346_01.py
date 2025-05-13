for attachment in msg.iter_attachments():
    filename = attachment.get_filename()
    content = attachment.get_content()
    with open("at_" + filename, "wb") as f:
        # 文字列の場合はエンコード
        if isinstance(content, str):
            f.write(content.encode(attachment.get_content_charset() or 'utf-8'))
        else:
            f.write(content)
