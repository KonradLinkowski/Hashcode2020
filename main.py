from Book import Book
from Library import Library

books_num, libraries_num, days_num = [int(x) for x in input().split(' ')]

books = [Book(i, int(x)) for i, x in enumerate(input().split(' '))]
libraries = []

for l in range(libraries_num):
    books_count, signup, bpd = [int(x) for x in input().split(' ')]
    l_books = [books[int(x)] for x in input().split(' ')]
    libraries.append(Library(l, signup, bpd, l_books))


def calc_prob():
    prob = [0 for x in books]
    for l in libraries:
        for b in l.books:
            prob[b.id] += 1
    return prob

# libraries.sort(key=lambda l: l.signup)
probs = calc_prob()
max_prob = max(probs)
max_sign = max([x.signup for x in libraries])
max_bpd = max([x.bpd for x in libraries])

# print(max_sign)
# d = [0 for x in range(max(xd))]
# for x in xd:
#     # print(x)
#     d[x - 1] += 1
# print(max_prob)

for l in libraries:
    l.norm_bpd(max_bpd)
    l.norm_sign(max_sign)
    l.calc_sum(probs, max_prob)
    l.calc_fitness()
    l.sort_books()


libraries.sort(key=lambda l: (l.fitness, -l.signup), reverse=True)
# print([(x.signup, x.fitness, x.books) for x in libraries][:2])

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
