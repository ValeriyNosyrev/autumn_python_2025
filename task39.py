 # Задаём базовый класс LearningMaterial cо св-вами title, author, duration_min
class LearningMaterial:
    def __init__(self, title, author, duration_min):
        self.title = title
        self.author = author
        self.duration_min = duration_min

    # Задаём методы display_info и get_difficulty
    def display_info(self):
        return f"Название: {self.title}, Автор: ({self.author}), Длительность - {self.duration_min} мин."

    def get_difficulty(self):
        raise NotImplementedError("Этот метод должен быть реализован в дочерних классах")

# Первый дочерний класс VideoLesson
class VideoLesson(LearningMaterial):
    def __init__(self, title, author, duration_min, video_quality, subtitles_availible):
        super().__init__(title, author, duration_min)
        # Задаём доп св-ва
        self.video_quality = video_quality
        self.subtitles_availible = subtitles_availible

    # Сложность: "Средняя"
    def get_difficulty(self):
        return "Средняя"

# Второй дочерний класс Article
class Article(LearningMaterial):
    def __init__(self, title, author, word_count, reading_level):
        super().__init__(title, author, None)
        # Дополнительные свойства: word_count, reading_level
        self.word_count = word_count
        self.reading_level = reading_level

    # (легкая если < 1, средняя 1-3, сложная > 3)
    def get_difficulty(self):
        words_thousands = self.word_count / 1000
        if words_thousands < 1:
            return "Легкая"
        elif words_thousands < 5:
            return "Средняя"
        else:
            return "Сложная"

# Третий дочерний класс Quiz
class Quiz(LearningMaterial):
    def __init__(self, title, author, duration_min, questions_count, passing_score):
        super().__init__(title, author, duration_min)
        # Дополнительные свойства: questions_count, passing_score
        self.questions_count = questions_count
        self.passing_score = passing_score

    # Сложность: "Высокая" если passing_score > 80, иначе "Средняя"
    def get_difficulty(self):
        if self.passing_score > 80:
            return "Высокая"
        else:
            return "Средняя"

# Этот код должен работать после реализации:
materials = [
    VideoLesson("Python ООП", "Иван Иванов", 45, "1080p", True),
    Article("Глубокое обучение", "Анна Петрова", 1200, "advanced"),
    Quiz("Проверка знаний", "Платформа", 20, 75, 10)
]

for material in materials:
    print(f"{material.title}: {material.get_difficulty()}")