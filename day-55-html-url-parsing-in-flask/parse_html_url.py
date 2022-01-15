from flask import Flask

app = Flask(__name__)


# def make_bold(function):
#     def wrapper():
#         return "<b>" + function() + "</b>"
#
#     return wrapper
#
#
# def make_underline(function):
#     def wrapper():
#         return "<u>" + function() + "</u>"
#
#     return wrapper
#
#
# def make_emphasis(function):
#     def wrapper():
#         return "<em>" + function() + "</em>"
#
#     return wrapper
#
#
# @app.route("/")
# @make_bold
# @make_underline
# @make_emphasis
# def greet_world():
#     return "Hello world 2.0!"
#
#
# @app.route("/username/<name>/<int:age>")
# def greet_user(name, age):
#     return f'Hello {name}, you are {age} years old!'
# Create the logging_decorator() function 👇
# def logging_decorator(function):
#     def wrapper(*args, **kwargs):
#         print(function.__name__)
#         for n in args:
#             print(n)
#         r = function(args[0], args[1])
#         print(f'Result: {r}')
#
#     return wrapper
#
#
# # Use the decorator 👇
# @logging_decorator
# def addition(n1, n2):
#     return n1 + n2
#
#
# addition()



if __name__ == "__main__":
    app.run(debug=True)
