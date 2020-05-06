def signup():
    print('Sign up!')
    email = input('Enter an email address: ')
    pw = input('Enter a password: ')
    hash_salt = salt_shaker()
    hashed_pw = pw_hasher(pw + hash_salt)

    with db.conn:
        db.c.execute(USER_SIGNUP, (email, hash_salt, hashed_pw))


def login():
    print('Log in!')
    email = input('Enter your email address: ')
    supplied_pw = input('Enter your password: ')

    with db.conn:
        db.c.execute('SELECT hash_salt, hashed_pw FROM USERS WHERE email = (?)', (email,))
        result = db.c.fetchone()
        salt = result[0]
        target_pw = result[1]

    pw_to_check = pw_hasher(supplied_pw + salt)

    return pw_to_check == target_pw