import time


class User:

    def __init__(self, nickname, password: str, age: int):
        self.nickname = nickname
        self.password = hash(str(password))
        self.age = age


class Video:

    def __init__(self, title, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class Engine:
    users = []
    videos = []
    current_user = None
    current_user_age = 0

    def log_in(self, nickname, password):

        # Проверка имени пользователя → пароля С ВХОДОМ!

        for i in Engine.users:
            if i.nickname == nickname:
                if i.password == hash(password):
                    Engine.current_user = nickname
                    Engine.current_user_age = i.age

    def register(self, nickname, password, age):

        # Регистрация пользователя

        for i in Engine.users:
            if i.nickname == nickname:
                return print(f'Пользователь {nickname} уже существует')
        else:
            Engine.users.append(User(nickname, password, age))
            return self.log_in(nickname, password)

    def log_out(self):

        # Выход из аккаунта

        Engine.current_user = None

    def add(self, *video_add):

        # Добавление видео

        for i in video_add:
            for j in Engine.videos:
                if i.title == j.title:
                    break
            else:
                Engine.videos.append(i)

    def get_videos(self, main_word):

        # Поиск видео по слову

        list_of_videos = []
        for i in Engine.videos:
            if main_word.lower() in i.title.lower():
                list_of_videos.append(i.title)
        return list_of_videos

    def watch_video(self, name_of_video):

        # Запуск видео по полному совпадению + проверка на возраст

        if Engine.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in Engine.videos:
                if name_of_video == i.title:
                    if i.adult_mode == True and Engine.current_user_age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for j in range(1, i.duration + 1):
                            print(j, end=' ')
                            time.sleep(0.5)
                        print('Конец видео')


ur = Engine()
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

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
