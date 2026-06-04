isLogin = True

def reuired_login(fn):
    def wrapper():
        if isLogin == True:
            return fn()
        else:
            print("please Login First")
            return
    return wrapper

@reuired_login # dashboard = required_login(dashboard)
def dashboard():
    print("show dashboard")

# @reuired_login
def home():
    print("show home")

dashboard()
home()