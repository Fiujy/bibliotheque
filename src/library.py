from book import Book
from user import User

class Library:
    """Gestionnaire de bibliothèque"""
    
    def __init__(self, name):
        if not name or not name.strip():
            raise ValueError("Le nom de la bibliothèque ne peut pas être vide")
        
        self.name = name.strip()
        self.books = []
    
    def add_book(self, book):
        """Ajoute un livre à la collection"""
        if not isinstance(book, Book):
            raise ValueError("L'objet doit être une instance de Book")
        self.books.append(book)
    
    def find_book_by_isbn(self, isbn):
        """Trouve un livre par ISBN"""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def borrow_book(self, user, isbn):
        """Gère l'emprunt complet"""
        # 1. Trouver le livre
        book = self.find_book_by_isbn(isbn)
        if not book:
            return False
        
        # 2. Vérifier que l'utilisateur peut emprunter
        if not user.can_borrow():
            return False
        
        # 3. Vérifier que le livre est disponible
        if not book.is_available():
            return False
        
        # 4. Effectuer l'emprunt
        if book.borrow():
            user.add_borrowed_book(book)
            return True
        
        return False
    
    def return_book(self, user, isbn):
        """Gère le retour complet d'un livre"""
        book = self.find_book_by_isbn(isbn)
        if not book:
            return False
        
        if book in user.borrowed_books:
            if book.return_book():
                user.remove_borrowed_book(book)
                return True
        
        return False