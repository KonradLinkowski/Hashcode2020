class Library:
    def __init__(self, id, signup, bpd, books):
        self.id = id
        self.signup = signup
        self.bpd = bpd
        self.books = books

    def __str__(self):
        books_joined = ' , '.join([str(x) for x in self.books])
        return f'Library {self.id} signup: {self.signup} bpd: {self.bpd} books: [{books_joined}]'
    
    def __repr__(self):
        return self.__str__()
