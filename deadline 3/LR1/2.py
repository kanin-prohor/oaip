def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper

@make_bold
def greet(name):
    return f"Привет, {name}!"

print(greet("Анна"))

def say_hello():
    return "Здравствуйте!"

bold_hello = make_bold(say_hello)
print(bold_hello())