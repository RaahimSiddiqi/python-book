


value = 10   # global

def func():
    global value
    value = 20

print("before function call:", value)
func()   
print("after function call:", value)