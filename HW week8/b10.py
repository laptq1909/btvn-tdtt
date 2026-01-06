class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
class library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def count_by_author(self, name):
        return sum(1 for b in self.books if b.author == name)
    def find_by_year(self, y):
        return sum(1 for b in self.books if b.year == y)
n = int(input())
lib = library()
for _ in range(n):
    line = input().strip()
    if line.startswith("ADD"):
        _, data = line.split(" ", 1)
        title, author, year = data.split(";")
        Book = book(title, author, int(year))
        lib.add_book(Book)
    elif line.startswith("COUNTYEAR"):
        _, year = line.split()
        print(lib.find_by_year(int(year)))
    elif line.startswith("COUNT"):
        _, author = line.split(" ", 1)
        print(lib.count_by_author(author))