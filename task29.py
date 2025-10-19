users = [
    {"name": "alice", "email": "alice@example.com", "age": 25, "active": True},
    {"name": "bob", "email": "bob@example.com", "age": 17, "active": True},
    {"name": "charlie", "email": "charlie@example.com", "age": 30, "active": False},
    {"name": "diana", "email": "diana@example.com", "age": 16, "active": True}
]

# Способ получения списка email-адресов активных пользователей старше 18 лет:

active_adult_email = [
    user["email"]
    for user in users
    if user["active"] and user["age"] >= 18
]

print(active_adult_email)