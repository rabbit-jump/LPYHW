from sys import argv

# 在cli运行此文件时，输入命令：python e12.py 1 2 3
# 输出
#The script is called: e13.py
#Your first variable is: 1
#Your second variable is: 2
#Your third variable is: 3
#如果输入的参数不足或超过4个，则运行报错ValueError: not enough values to unpack (expected 4, got 1)

script, first, second, third = argv
#argv保存着运行python脚本时传递给python脚本的参数。
#11行的代码将argv收到的参数解包，分别赋值给script, first, second, third
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)