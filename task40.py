# Базовый класс NotificationSender с методом send(message, user)
class NotificationSender:
    def send(self, message, user):
        raise NotImplementedError ("Этот метод должен быть реализовани в дочерних классах")

# Дочерний класс EmailSender отправляет email с темой "Образовательная платформа":
class EmailSender(NotificationSender):
    def send(self, message, user):
        print(f"Отправляем email пользователю {user.name}: Образовательная платформа - {message}")

# Дочерний класс SMSSender отправляет SMS (первые 50 символов сообщения):
class SMSSender(NotificationSender):
    def send(self, message, user):
        sms_limit = message[:50]
        print(f"Отправляем SMS пользователю {user.name}: {sms_limit}")

# Дочерний класс отправляет push-уведомление с иконкой "🎓"
class PushSender(NotificationSender):
    def send(self, message, user):
        print(f"Отправляем push-уведомление пользователю {user.name}: 🎓 {message}")

# Класс пользователя User:
class User:
    # Свойства: name, preferred_notifications (список объектов NotificationSender)
    def __init__(self, name, preferred_notifications):
        self.name = name
        self.preferred_notifications = preferred_notifications

def notify_user(user, message):
    for sender in user.preferred_notifications:
        sender.send(message, user)

# Этот код должен работать после релизации:
        user = User("Мария", [EmailSender(), PushSender()])
        notify_user(user, "Блок аналитики начинается с 27 октября!")

