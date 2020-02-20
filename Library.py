class Library:
    def __init__(self, id, signup, bpd, books):
        self.id = id
        self.signup = signup
        self.bpd = bpd
        self.books = books

    def __str__(self):
        return f'Library {self.id} signup: {self.signup} bpd: {self.bpd}'
