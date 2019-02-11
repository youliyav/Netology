from datetime import datetime


def logging(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(path, 'w', encoding='utf-8') as f:
                start = datetime.now()
                data = func(*args, **kwargs)
                res = data
                f.write('{}\n{}\n{}\n{}\n{}\n'.format(start, func.__name__, args, kwargs, res))
            return data
        return wrapper
    return decorator