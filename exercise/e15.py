from sys import argv

script, filename = argv
#txt = open(filename)
txt = open(filename,encoding='utf-8')#注意这个编码设定，如果直接使用第4行代码的形式，不一定能执行成功，这和终端使用的编码有关。
print(f"Here's your file {filename}:")
print(txt.read())
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again,encoding='utf-8')
print(txt_again.read())