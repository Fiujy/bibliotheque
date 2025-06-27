class User:
    """Représente un utilisateur de la bibliothèque"""
    
    def __init__(self, name, email):
        # Validation du nom
        if not name or not name.strip():
            raise ValueError("Le nom ne peut pas être vide")
        
        # Validation de l'email
        if not email or "@" not in email:
            raise ValueError("L'email doit contenir le caractère @")
        
        self.name = name.strip()
        self.email = email.strip()
        self.borrowed_books = []
    
    def can_borrow(self, max_books=3):
        """Vérifie si l'utilisateur peut emprunter"""
        return len(self.borrowed_books) < max_books
    
    def add_borrowed_book(self, book):
        """Ajoute un livre à la liste des emprunts"""
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
    
    def remove_borrowed_book(self, book):
        """Retire un livre de la liste des emprunts"""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
    
    def __str__(self):
        return f"{self.name} ({self.email})"