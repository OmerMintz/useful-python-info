import threading


def my_function(*args, **kwargs):
    print(args)
    print(kwargs)


my_thread = threading.Thread(target=my_function, args=("hello", "world"), kwargs={"hello": "world"})

my_thread.start()
