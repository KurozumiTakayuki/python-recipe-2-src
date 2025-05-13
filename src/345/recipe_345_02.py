body_part = msg.get_body(preferencelist=('html', 'plain'))
body_text = body_part.get_content()
print(body_text)
