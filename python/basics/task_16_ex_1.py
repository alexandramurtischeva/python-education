
f = open('file.txt')

for line in f.readlines():
    print(line)

f.close()

text = """ 
There are many variations of passages of Lorem Ipsum available, 
but the majority have suffered alteration in some form, 
by injected humour, or randomised words which don't look even 
slightly believable. If you are going to use a passage of Lorem Ipsum, 
you need to be sure there isn't anything embarrassing hidden in the middle of text. 
"""

with open('file.txt', 'a') as f:
    f.writelines(text)


with open('file.txt', 'r') as f:
    for line in f.readlines():
        print(line)

