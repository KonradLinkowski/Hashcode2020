from Book import Book
from Library import Library

# load

books_num, libraries_num, days_num = [int(x) for x in input().split(' ')]

books = [Book(i, int(x)) for i, x in enumerate(input().split(' '))]
libraries = []

for l in range(libraries_num):
    books_count, signup, bpd = [int(x) for x in input().split(' ')]
    l_books = [books[int(x)] for x in input().split(' ')]
    libraries.append(Library(l, signup, bpd, l_books))


def sum_for_lib(lib):
    s = 0
    for book in lib.books:
        s += book.score
    return s


# print('\n'.join([str(x) for x in libraries]))
sums = [sum_for_lib(l) for l in libraries]
for s in sums:
    print(s)

# print(books)
# solve


