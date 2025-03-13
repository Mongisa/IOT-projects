class Libro:
    def __init__(self,titolo,autore,anno,genere,disponibile=True):
        self.titolo=titolo
        self.autore=autore
        self.anno=anno
        self.genere=genere
        self.disponibile=disponibile
    
    def __str__(self):
        return "%s di %s (%d) [%s] - %s" % (self.titolo,self.autore,self.anno,self.genere,"Disponibile" if self.disponibile else "Non Disponibile")
    
class Biblioteca:
    catalogo=[]

    def addBook(self, book):
        self.catalogo.append(book)

    def searchBookByAuthor(self, author):
        for book in self.catalogo:
            if book.autore.lower() == author.lower():
                return book
        else:
            return None

    def searchBookByTitle(self, title):
        for book in self.catalogo:
            if book.titolo.lower() == title.lower():
                return book
        else:
            return None
    
    def borrowBook(self, book):
        if(book.disponibile == True):
            book.disponibile=False
            return True
        else:
            return False
    
    def returnBook(self, book):
        if(book.disponibile == False):
            book.disponibile = True
            return True
        else:
            return False
        
    def __str__(self):
        s="--- Libri ---\n"

        if self.catalogo.__len__() == 0:
            return "Libreria vuota!"
        for book in self.catalogo:
            s+=book.__str__()+"\n"
        return s
    
######################

def printMenu():
    print("--- Biblioteca ---")
    print("1. Mostra catalogo")
    print("2. Cerca per autore")
    print("3. Cerca per titolo")
    print("4. Prendi in prestito un libro")
    print("5. Restituisci un libro")
    print("6. Aggiungi un nuovo libro")
    print("7. Esci")

def searchByAuthor(b):
    author=input("Inserisci autore: ")

    res=b.searchBookByAuthor(author)

    if(res == None):
        print("Nessun libro scritto da %s" % author)
    else:
        print(res.__str__())

def searchByTitle(b):
    title=input("Inserisci titolo: ")

    res=b.searchBookByTitle(title)

    if(res == None):
        print("Nessun libro con titolo: %s" % title)
    else:
        print(res.__str__())

def borrowBook(b):
    title=input("Inserisci titolo: ")

    book=b.searchBookByTitle(title)

    if book == None:
        print("Libro non trovato")
    else:
        res=b.borrowBook(book)
        if res:
            print("Operazione confermata!")
        else:
            print("Il libro non è al momento disponibile!")

def returnBook(b):
    title=input("Inserisci titolo: ")

    book=b.searchBookByTitle(title)

    if book==None:
        print("Libro non trovato")
    else:
        res=b.returnBook(book)
        if res:
            print("Operazione confermata!")
        else:
            print("Il libro è già disponibile!")

def createAndAddBook(b):
    titolo=input("Inserisci titolo: ")
    autore=input("Inserisci autore: ")
    anno=int(input("Inserisci anno: "))
    genere=input("Inserisci genere: ")

    b.addBook(Libro(titolo,autore,anno,genere,True))
    print("Libro aggiunto con successo!")

def interfaccia_utente(b):
    printMenu()
    sel=input("Inserisci un numero da 1 a 7: ")

    while(not(sel in ["1","2","3","4","5","6","7"])):
        printMenu()
        sel=input("Inserisci un numero da 1 a 7: ")

    match sel:
        case "1": #MOSTRA CATALOGO
            print(b.__str__())
        case "2": #CERCA PER AUTORE
            searchByAuthor(b)
        case "3": #CERCA PER TITOLO
            searchByTitle(b)
        case "4": #PRENDERE IN PRESTITO UN LIBRO
            borrowBook(b)
        case "5": #RESTUIRE LIBRO
            returnBook(b)
        case "6": #AGGIUNGI LIBRO
            createAndAddBook(b)
        case "7": #USCITA
            print("Alla prossima!")
            exit()

### MAIN ###
b=Biblioteca()

b.addBook(Libro("Il Signore degli Anelli","J.R.R. Tolkien", 1954, "Fantasy"))
b.addBook(Libro("1984","George Orwell",1949,"Distopia"))
b.addBook(Libro("Il gattopardo","Giuseppe Tomasi di Lampedusa",1958,"Romanzo Storico"))
b.addBook(Libro("Harry Potter e la Pietra Filosofale","J.K. Rowling",1997,"Fantasy"))

while(True):
    interfaccia_utente(b)