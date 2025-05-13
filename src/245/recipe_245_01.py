import pickle


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"ユーザー情報  名前:{self.name} 年齢:{self.age}"


# インスタンスを作成
user = User('鈴木', 30)

# 生成したデータを確認
print("生成したデータ　", user)

# インスタンスをシリアライズして保存
with open('user.pkl', 'wb') as f1:
    pickle.dump(user, f1)

# ファイルからインスタンスをデシリアライズして読み込み
with open('user.pkl', 'rb') as f2:
    load_data = pickle.load(f2)

# 読み込んだデータを確認
print("読み込んだデータ", load_data)
