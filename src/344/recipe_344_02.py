from email import message_from_bytes, policy
:
中略
:
raw_email = msg_data[0][1]
msg = email.message_from_bytes(raw_email, policy=policy.default)