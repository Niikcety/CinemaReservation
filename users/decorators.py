def login_check(func):

    def wrapper(*args, **kwargs):

        user_id = args[0].id
        if user_id == 0:
            print('You need to be logged in to complete this task.')
            user_info = login()
            
        else:
            return func(*args)

    return wrapper

def tp_is_admin(func):

    def wrapper(*args, **kwargs):

        user_tp = args[0].tp
        if user_tp is None:
            pass

        else:
            return func(*args)

    return wrapper
