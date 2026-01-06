class shoppingcart:
    def __init__(self):
        self.items = []
    def add_item(self, item, price):
        self.items.append({"name": item, "price": price})
    def remove_item(self, item):
        self.items = [i for i in self.items if i["name"] != item]
    def view_cart(self):
        for item in self.items:
            print(f"{item['name']}: {item['price']}")
    def total_price(self):
        return sum(item['price'] for item in self.items)
    def clear_cart(self):
        self.items = []
cart = shoppingcart()
while True:
    print("\n----- MENU -----")
    print("1. Thoát")
    print("2. Thêm sản phẩm")
    print("3. Xóa sản phẩm theo tên")
    print("4. Tính tổng tiền")
    print("5. Hiển thị giỏ hàng")
    print("6. Xóa toàn bộ giỏ hàng")
    choice = input("Nhập lựa chọn của bạn (1-6): ")
    if choice == "1":
        print("Thoát chương trình.")
        break
    elif choice == "2":
        name = input("Nhập tên sản phẩm: ")
        price = float(input("Nhập giá sản phẩm: "))
        cart.add_item(name, price)
    elif choice == "3":
        name = input("Nhập tên sản phẩm cần xóa: ")
        cart.remove_item(name)
    elif choice == "4":
        print("Tổng tiền giỏ hàng:", cart.total_price())
    elif choice == "5":
        cart.view_cart()
    elif choice == "6":
        cart.clear_cart()
    else:
        print("Lựa chọn không hợp lệ!")