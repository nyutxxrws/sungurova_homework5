import random
import json
import string
name = random.choice(["Anna Sungurova", "Nastya Ivanova", "Kate Smirnova", "Victor Semenov", "Elena Fedorova"])
age = random.randint(18, 80)
email = name.lower().replace(" ", ".") + "@example.com"
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
user_data = {
    "name": name,
    "age": age,
    "email": email,
    "password": password
}
with open("user.json", "w") as file:
    json.dump(user_data, file, indent=4)
with open("user.json", "r") as file:
    loaded_data = json.load(file)
    print(json.dumps(loaded_data, indent=4))
