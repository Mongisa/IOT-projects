class Book:
    title=""
    author=""
    pages=0

    def __init__(self, title="",author="",pages=0):
        self.title = title
        self.author = author
        self.pages = pages

    def info1(self):
        print("Author: %s, Title: %s, Pages: %d" % (self.author,self.title,self.pages))

    def info2(self):
        print(f"Author: {self.author}, Title: {self.title}, Pages: {self.pages}")

    def info3(self):
        print("Author: {0}, Title: {1}, Pages: {2}".format(self.author,self.title,self.pages))

b1 = Book(title="Promessi Sposi",author="Manzoni",pages=500)

b1.info1()
b1.info2()
b1.info3()