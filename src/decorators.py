from functools import wraps


def log(filename=None):
    """добавляет логи о правильности работы функции или о возникающих ошибках"""

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__} function - ok. Result - {res}")
                else:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} function - ok. Result - {res}")
            except Exception as err:
                if filename is None:
                    print(f"{func.__name__} function error: {err}. Inputs: ({args}),{kwargs}")
                else:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} function error: {err}. Inputs: ({args}),{kwargs}")

        return wrapper

    return my_decorator
