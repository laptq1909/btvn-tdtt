s = input("Ex27: ")
count = 0
in_word = False
i = 0
for c in s:
    if c != ' ' and not in_word:
        count += 1
        in_word = True
    elif c == ' ':
        in_word = False
    i += 1    
print("Series word count: ", count)