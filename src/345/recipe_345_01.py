from email import message_from_bytes, policy

# :
# 中略
# :
msg = message_from_bytes(raw_email, policy=policy.default)
print("件名:", msg.get("Subject"))
print("送信元:", msg.get("From"))
print("宛先:", msg.get("To"))