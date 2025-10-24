class User:
    def __init__(self, email, password):
        self.email = email
        self._password_hash = self._hash_password(password)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
         # Базово проверяем, что в строке есть @
        if "@" not in value:
            raise ValueError("Email должен содержать @")
        self._email = value

    def _hash_password(self, password):
        # Используем hash
        return hash(password)

    def check_password(self, password):
        # Сверяем хеш переданного пароля с хешем пароля пользователя
        return self._password_hash == self._hash_password(password)

user = User("test@example.com", "secret")
print(user.email)  # test@example.com
# print(user.password) # AttributeError
print(user.check_password("secret"))  # True
print(user.check_password("wrong"))   # False