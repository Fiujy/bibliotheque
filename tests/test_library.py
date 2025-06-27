import pytest
from library import Library
from book import Book
from user import User

class TestLibraryOperations:
    """Tests des opérations de bibliothèque"""
    
    def setup_method(self):
        """Fixture complexe : bibliothèque avec livres et utilisateurs"""
        self.library = Library("Bibliothèque Municipale")
        
        # Création des livres
        self.book1 = Book("Le Seigneur des Anneaux", "J.R.R. Tolkien", "9782070612888")
        self.book2 = Book("Harry Potter", "J.K. Rowling", "9782070543519")
        self.book3 = Book("Dune", "Frank Herbert", "9782266063012")
        
        # Ajout des livres à la bibliothèque
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        
        # Création des utilisateurs
        self.user1 = User("Alice Martin", "alice@example.com")
        self.user2 = User("Bob Dupont", "bob@example.com")
    
    def test_add_book_to_library(self):
        """Test ajout livre à la bibliothèque"""
        new_book = Book("Nouveau Livre", "Nouvel Auteur", "9876543210123")
        self.library.add_book(new_book)
        assert new_book in self.library.books
    
    def test_find_book_by_isbn_existing(self):
        """Test recherche livre existant par ISBN"""
        found_book = self.library.find_book_by_isbn("9782070612888")
        assert found_book == self.book1
    
    def test_find_book_by_isbn_non_existing(self):
        """Test recherche livre inexistant par ISBN"""
        found_book = self.library.find_book_by_isbn("0000000000000")
        assert found_book is None
    
    def test_borrow_flow_success(self):
        """Test flux complet d'emprunt réussi"""
        result = self.library.borrow_book(self.user1, "9782070612888")
        assert result is True
        assert not self.book1.is_available()
        assert self.book1 in self.user1.borrowed_books
    
    def test_borrow_non_existing_book_fails(self):
        """Test emprunt livre inexistant échoue"""
        result = self.library.borrow_book(self.user1, "0000000000000")
        assert result is False
    
    def test_borrow_already_borrowed_book_fails(self):
        """Test emprunt livre déjà emprunté échoue"""
        self.library.borrow_book(self.user1, "9782070612888")
        result = self.library.borrow_book(self.user2, "9782070612888")
        assert result is False
    
    def test_user_cannot_borrow_more_than_limit(self):
        """Test limite d'emprunts par utilisateur"""
        # Emprunt de 3 livres (limite)
        self.library.borrow_book(self.user1, "9782070612888")
        self.library.borrow_book(self.user1, "9782070543519")
        self.library.borrow_book(self.user1, "9782266063012")
        
        # Tentative d'un 4ème emprunt
        new_book = Book("Quatrième Livre", "Auteur", "1111111111111")
        self.library.add_book(new_book)
        result = self.library.borrow_book(self.user1, "1111111111111")
        assert result is False
    
    def test_return_book_success(self):
        """Test retour de livre réussi"""
        # Emprunt puis retour
        self.library.borrow_book(self.user1, "9782070612888")
        result = self.library.return_book(self.user1, "9782070612888")
        assert result is True
        assert self.book1.is_available()
        assert self.book1 not in self.user1.borrowed_books