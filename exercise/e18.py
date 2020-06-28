# this one is like your scripts with argv
def print_two(*args):#*的功能是告诉python把函数的所有参数都接受进来，存放在一个args的列表中
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()