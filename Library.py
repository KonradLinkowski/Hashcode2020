class Library:
    def __init__(self, id, signup, bpd, books):
        self.id = id
        self.signup = signup
        self.bpd = bpd
        self.books = books

    def norm_bpd(self, mx):
        self.norm_bpd = self.bpd / mx

    def norm_sign(self, mx):
        self.norm_signup = self.signup / mx

    def calc_sum(self, probs, max_prob):
        s = 0
        mx = max_prob
        for book in self.books:
            p = probs[book.id]
            s += book.score / p / mx
        self.score_sum = s
        return s

    def sort_books(self):
        self.books.sort(key=lambda b: b.score, reverse=True)

    def calc_fitness(self):
        if self.bpd > len(self.books):
            self.fitness = self.score_sum / self.norm_signup
        else:
            self.fitness = self.score_sum  / self.norm_signup * self.norm_bpd
        return self.fitness

    def __str__(self):
        books_joined = ' , '.join([str(x) for x in self.books])
        return f'Library {self.id} signup: {self.signup} bpd: {self.bpd} books: [{books_joined}]'
    
    def __repr__(self):
        return self.__str__()
