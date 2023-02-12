def greet_user():
    """Display a simple greeting"""
    print('Hello')

greet_user()

def greet_user_name(username):
    """Display a greeting to a username"""
    print(f"Hello, {username.title()}")

greet_user_name('jessie')