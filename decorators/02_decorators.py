# decorators extends the functionality of function

def demo(fn):
    def test():
        print("hello test")
        fn()
    return test

@demo # say_hello =  demo(say_hello)
def say_hello():
    print("hello python")


# say_hello =  demo(say_hello) # decorator same as @demo
# say_hello()

# x = demo(say_hello)
# print(x)