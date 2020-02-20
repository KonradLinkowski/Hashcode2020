from Book import Book
from Library import Library

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

sums = [sum_for_lib(l) for l in libraries]
for i, l in enumerate(libraries):
    l.sum = sums[i]

    l.fitness = sums[i] / l.signup * l.bpd

libraries.sort(key=lambda l: l.fitness, reverse=True)

ind = 0
signup_sum = 0
for l in libraries:
    signup_sum += l.signup
    ind += 1
    if (signup_sum > days_num):
        break

print(ind)
for l in libraries[:ind]:
    print(f'{l.id} {len(l.books)}')
    print(' '.join(str(b.id) for b in l.books))
