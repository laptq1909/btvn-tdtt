try:
    filename = input("Nhap ten file: ")
    if not (filename.endswith(".txt") or filename.endswith(".zip")):
        raise ValueError("Sai dinh dang file")
    print("Doc file thanh cong")
except ValueError:
    print("File khong hop le")