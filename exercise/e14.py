from sys import argv

script, user_name = argv

prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)#将用户输入提示设置为变量prompt，就不需要每次都重写用户输入提示
#而且当需要修改用户输入提示的时候，只需要修改一处地方，即第5行即可。

print(f"Where do you live {user_name}?")

lives = input(prompt)

print("What kind of computer do you have?")

computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")