import pytest
from user import User
from book import Book

class TestUserCreation:
    """Tests de création d'utilisateur"""
    
    def test_create_valid_user(self):
        """Test création utilisateur valide"""
        user = User("John Doe", "john@example.com")
        assert user.name == "John Doe"
        assert user.email == "john@example.com"
        assert user.borrowed_books == []
    
    def test_create_user_empty_name_raises_error(self):
        """Test nom vide lève une erreur"""
        with pytest.raises(ValueError, match="Le nom ne peut pas être vide"):
            User("", "john@example.com")
    
    def test_create_user_invalid_email_raises_error(self):
        """Test email invalide lève une erreur"""
        with pytest.raises(ValueError, match="L'email doit contenir le caractère @"):
            User("John Doe", "invalid-email")

class TestUserBorrowing:
    """Tests d'emprunt utilisateur"""
    
    def setup_method(self):
        """Fixture : prépare un utilisateur pour chaque test"""
        self.user = User("Jane Smith", "jane@example.com")
        self.book1 = Book("Livre 1", "Auteur 1", "1234567890123")
        self.book2 = Book("Livre 2", "Auteur 2", "1234567890124")
        self.book3 = Book("Livre 3", "Auteur 3", "1234567890125")
        self.book4 = Book("Livre 4", "Auteur 4", "1234567890126")
    
    def test_user_can_borrow_initially(self):
        """Test utilisateur peut emprunter initialement"""
        assert self.user.can_borrow()
    
    def test_user_can_borrow_up_to_limit(self):
        """Test utilisateur peut emprunter jusqu'à la limite"""
        self.user.add_borrowed_book(self.book1)
        self.user.add_borrowed_book(self.book2)
        assert self.user.can_borrow()
        
        self.user.add_borrowed_book(self.book3)
        assert not self.user.can_borrow()
    
    def test_add_borrowed_book(self):
        """Test ajout livre emprunté"""
        self.user.add_borrowed_book(self.book1)
        assert self.book1 in self.user.borrowed_books
        assert len(self.user.borrowed_books) == 1
    
    def test_remove_borrowed_book(self):
        """Test retrait livre emprunté"""
        self.user.add_borrowed_book(self.book1)
        self.user.remove_borrowed_book(self.book1)
        assert self.book1 not in self.user.borrowed_books
        assert len(self.user.borrowed_books) == 0
