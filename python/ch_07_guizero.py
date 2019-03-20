from guizero import *

def say_hello():
    info("An Alert", "Please don't press this button again")

app = App(title="Pi Cookbook Example", height=200)
button = PushButton(app, text="Don't Press Me", command=say_hello)

app.display()
