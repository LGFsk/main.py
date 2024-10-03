import time


class UrTube:
    # Инициализация
    def __init__(self):
        self.users = []
        self.password = []
        self.videos = []
        self.current_user = None

    # Метод авторизации
    def log_in(self, nickname, password):
        if nickname in self.users and hash(password) == hash(self.password[self.users.index(nickname)]):
            self.current_user = nickname
            print(f"Вы успешно залогинились: {self.current_user}")
        else:
            print(f"Пароль не соответсвует логину: {nickname} или введен не верно")

    # Метод выхода из аккаунта
    def log_out(self):
        self.current_user = None

    # Метод регистрации
    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Не удалось зарегистрироваться, пользователь {nickname} уже существует")
        else:
            self.users.append(nickname)
            self.password.append(password)
            self.age = age
            self.log_in(nickname, password)

    # Метод добавления видео
    def add(self, *Video):
        for i in Video:
            if i.title in (self.videos[j].title for j in range(len(self.videos))):
                print(f"Видео не добавлено, уже есть видео с таким названием: {i.title}")
            else:
                self.videos.append(i)
                print(f"Добавлено новое видео: {i.title}")

    # Метод поиск видео
    def get_videos(self, search):
        result_search = []
        for i in self.videos:
            if search.lower() in str(i.title).lower():
                result_search.append(i.title)
        if result_search == []:
            return (f'По поисковому запросу: "{search}", не найдены видео')
        return (f'По поисковому запросу: "{search}", нейдены следующие видео: {result_search}')

    # Метод просмотра видео
    def watch_video(self, title):
        result_search = []
        if self.current_user == None:
            print(f"Войдите в аккаунт, чтобы смотреть видео")
        elif self.age > 18:
            for i in self.videos:
                if title.lower() in str(i.title.lower()):
                    result_title = i.title
                    result_duration = i.duration
            if result_title == []:
                print(f"Не найдено видео: {title}")
            else:
                print(f"Воспроизведение видео: {title}: ", end=" ")
                for i in range(result_duration):
                    if result_duration > 20:
                        time.sleep(0.02)
                        print(i + 1, end=" ")
                    else:
                        time.sleep(0.3)
                        print(i + 1, end=" ")
                print("Конец видео")
                time.sleep(2)
        else:
            print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
            self.log_out()


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __hash__(self):
        return hash(self.password)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.watch_video('Лучший язык программирования 2024 года')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
