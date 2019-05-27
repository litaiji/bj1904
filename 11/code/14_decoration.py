# def wrap(func):
#     def inner():
#         func()
#         print("*"*50)
#     return inner
#
# @wrap
# def hello():
#     print(hello.__name__)
#

class App:
    def __call__(self, *args, **kwargs):
        print("----"*50)
    def wrapper(self):
        def inner(f):
            print("*"*50)
            f()
        return inner
app = App()

# @app.wrapper()
# def hello():
#     print("hello")
#
# 对象能不能调用
app()