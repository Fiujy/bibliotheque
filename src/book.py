class Book:
    """Représente un livre dans la bibliothèque"""
    
    def __init__(self, title, author, isbn):
        # Validation du titre
        if not title or not title.strip():
            raise ValueError("Le titre ne peut pas être vide")
        
        # Validation de l'auteur
        if not author or not author.strip():
            raise ValueError("L'auteur ne peut pas être vide")
        
        # Validation de l'ISBN
        if not isbn or len(isbn) != 13:
            raise ValueError("L'ISBN doit contenir exactement 13 caractères")
        
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn
        self.borrowed = False
    
    def is_available(self):
        """Retourne True si le livre n'est pas emprunté"""
        return not self.borrowed
    
    def borrow(self):
        """Marque le livre comme emprunté"""
        if self.borrowed:
            return False
        self.borrowed = True
        return True
    
    def return_book(self):
        """Marque le livre comme disponible"""
        if not self.borrowed:
            return False
        self.borrowed = False
        return True
    
    def __str__(self):
        return f"{self.title} par {self.author} (ISBN: {self.isbn})"