class cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def pow(self):
        return self.a ** self.b
    def mod(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a % self.b
    def set_numbers(self, a, b):
        self.a = a
        self.b = b
a,b = map(int, input("Enter two numbers: ").split())
calc = cal(a, b)
while True:
    print("\n===== MENU =====")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Lũy thừa")
    print("6. Chia lấy dư")
    print("7. Nhập 2 số mới")
    choice = input("Chọn phép toán (1-7): ")
    if choice == "1":
        print("Kết quả:", calc.add())
    elif choice == "2":
        print("Kết quả:", calc.sub())
    elif choice == "3":
        print("Kết quả:", calc.mul())
    elif choice == "4":
        print("Kết quả:", calc.div())
    elif choice == "5":
        print("Kết quả:", calc.pow())
    elif choice == "6":
        print("Kết quả:", calc.mod())
    elif choice == "7":
        a, b = map(float, input("Nhập hai số mới: ").split())
        calc.set_numbers(a, b)
    exit_choice = input("Quit? (yes/no): ")
    if exit_choice.lower() == "yes":
        break