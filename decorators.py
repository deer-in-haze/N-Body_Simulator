def status_update(func):
    def wrapper(*args, **kwargs):
        if args:
            instance = args[0]
            print(f'Initiating class {instance.__class__.__name__} method {func.__name__}')
        else:
            print(f'Initiating {func.__name__}')

        result = func(*args, **kwargs)
        print('Done')
        return result

    return wrapper


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
