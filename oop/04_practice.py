#  create a class notes
#  add parameterized constructor with task, desc and priority
#  add method called get_task() which return dict with task desc and priority
# create two object and call get_task with each object


class Notes:
    def __init__(self, task, desc, priority):
        self.task = task
        self.desc = desc
        self.priority = priority

    def get_task(self):
       return {"task":self.task, "desc":self.desc, "priority":self.priority}

    def add_task(self):
        print("add task cval")

t1 = Notes("Learn Python", "Python is fun", "High")
t2 = Notes("Learn Javascript", "Js is awesome", "Medium")

print(t1.get_task())
print(t2.get_task())
