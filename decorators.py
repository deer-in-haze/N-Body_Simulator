def status_update(func):
    def wrapper(*args, **kwargs):
        if args:
            instance = args[0]
            print(f'Initiating class {instance.__class__.__name__} method {func.__name__}')
        else:
            print(f'Initiating {func.__name__}')

        func(*args, **kwargs)
        print('Done')

    return wrapper
