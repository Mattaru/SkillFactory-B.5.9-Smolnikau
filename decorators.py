import time

# Функция декоратор
def time_this(num_runs = 1):
    """
    Функция-декоратор, все функции помещенные в данный декоратор будут пропускаться через него и возвращать
    среднее время на выполнение обернутой функции.
    В качестве аргументо можно задать кол-во выполнений обернутой функции.
    """
    def timer_wrap(func):
        def timer_wrapper(*args, **kwargs):
            av_time = 0
            for i in range(num_runs):
                time_one = time.time()
                func(*args, **kwargs)
                time_two = time.time()
                av_time += (time_two - time_one)
            av_time /= num_runs
            return print("Среднее время выполнения - %s. Проверка через декоратор." % av_time)
        return timer_wrapper
    return timer_wrap

# Класс таймера с встроенным декоратором
class Timer:
    def __init__(self, num_runs = 10):
        self.num_runs = num_runs

    def __call__(self, func):
        def time_wrapper(*args, **kwargs):
            """
            Класс Timer() и объекты этого класса можно использовать, как декораторы.
            Можно задавать аргумент с кол-вом выполнений обернутой функции.
            """
            avg_time = 0
            for _ in range(self.num_runs):
                str_time = time.time()
                func(*args, **kwargs)
                ed_time = time.time()
                avg_time += (ed_time - str_time)
            avg_time /= self.num_runs
            return print("Среднее время выполнения - %s. Проверка через декоратор класса." % avg_time)
        return time_wrapper

    def __enter__(self):
        """
        При использовании Timer() как контекстный менеджер, отмечает время запуска кода.
        """
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        При использовании Timer() как контекстный менеджер, отмечает время окончания работы кода и делает
        рассчет времени, затраченного на выполнение кода внутри контекстного менеджера.
        """
        self.end_time = time.time()
        run_time = self.end_time - self.start_time
        print("Общая продолжительность кода - %s. Проверка через контекстный менеджер." % run_time)

# Проверяем функцию декоратор
@time_this(num_runs=10)
def fd():
    for j in range(1000000):
        pass

fd()

# Проверяем объект-декоратор класса Таймер
@Timer(num_runs=20)
def f():
    for j in range(1000000):
        pass

f()

# Проверяем объект-декоратор класса Таймер, как контекстный менеджер
def fb():
    for j in range(1000000):
        pass

with Timer():
    fb()