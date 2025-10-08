s = input("Ex28: ")
first_word = ""
found_word = False
for i in range(len(s)):
    if s[i] != ' ':
        first_word += s[i]
        found_word = True
    elif found_word: # gặp khoảng trắng sau khi đã bắt đầu từ => dừng lại
        break
print("Từ đầu tiên là:", first_word)