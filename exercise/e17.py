from os.path import exists
from sys import argv

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line too, how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()#合并为一行的操作
print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()
out_file = open(to_file, 'w')
out_file.write(indata)
print("Alright, all done.")
out_file.close()

#in_file.close()
open(from_file).close()#打开的文件必须关闭