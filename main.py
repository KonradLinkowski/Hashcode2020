from Book import Book
from Library import Library

# load

books_num, libraries_num, days_num = [int(x) for x in input().split(' ')]

books = [Book(i, int(x)) for i, x in enumerate(input().split(' '))]
libraries = []

for l in range(libraries_num):
    books_count, signup, bpd = [int(x) for x in input().split(' ')]
    l_books = [int(x) for x in input().split(' ')]
    libraries.append(Library(l, signup, bpd, l_books))


print(libraries)
print(books)
# solve


