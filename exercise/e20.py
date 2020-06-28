from sys import argv

script, input_file = argv
def print_all(f):#传入一个文件对象
    print(f.read())#输出文件内容

def rewind(f):
    f.seek(0)#将文件读写指针指向第1个字节

def print_a_line(line_count, f):#第一个参数是一行的内容，第二个参数是文件对象
    #print(line_count, f.readline())
	#readline函数返回的内容中包含文件本身就有的\n，而print在打印的时候又会添加一个\n。所以输出会多处一个空行
	print(line_count,f.readline(),end='')#这样就不会多出空行了

current_file = open(input_file,encoding = 'utf-8')
print("First let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)