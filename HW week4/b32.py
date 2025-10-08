s = input("Ex32: ")
has_upper = False
has_lower = False
has_digit = False
has_special = False
special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"
for i in range(len(s)):
    ch = s[i]
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True
if len(s) > 6 and has_upper and has_lower and has_digit and has_special:
    print(" Mật khẩu mạnh!")