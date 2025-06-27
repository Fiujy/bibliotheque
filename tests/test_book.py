import pytest
from book import Book

class TestBookCreation:
    """Tests de création de livre"""
    
    def test_create_valid_book(self):
        """Test création livre valide"""
        book = Book("Le Petit Prince", "Antoine de Saint-Exupéry", "9782070408504")
        assert book.title == "Le Petit Prince"
        assert book.author == "Antoine de Saint-Exupéry"
        assert book.isbn == "9782070408504"
        assert not book.borrowed
    
    def test_create_book_empty_title_raises_error(self):
        """Test titre vide lève une erreur"""
        with pytest.raises(ValueError, match="Le titre ne peut pas être vide"):
            Book("", "Auteur", "1234567890123")
        
        with pytest.raises(ValueError, match="Le titre ne peut pas être vide"):
            Book("   ", "Auteur", "1234567890123")
    
    def test_create_book_empty_author_raises_error(self):
        """Test auteur vide lève une erreur"""
        with pytest.raises(ValueError, match="L'auteur ne peut pas être vide"):
            Book("Titre", "", "1234567890123")
    
    def test_create_book_invalid_isbn_raises_error(self):
        """Test ISBN invalide lève une erreur"""
        with pytest.raises(ValueError, match="L'ISBN doit contenir exactement 13 caractères"):
            Book("Titre", "Auteur", "123")  # Trop court
        
        with pytest.raises(ValueError, match="L'ISBN doit contenir exactement 13 caractères"):
            Book("Titre", "Auteur", "12345678901234")  # Trop long

class TestBookBorrowing:
    """Tests d'emprunt de livre"""
    
    def setup_method(self):
        """Fixture : prépare un livre pour chaque test"""
        self.book = Book("1984", "George Orwell", "9780451524935")
    
    def test_new_book_is_available(self):
        """Test livre neuf disponible"""
        assert self.book.is_available()
    
    def test_borrow_available_book_success(self):
        """Test emprunt livre disponible"""
        result = self.book.borrow()
        assert result is True
        assert not self.book.is_available()
    
    def test_borrow_already_borrowed_book_fails(self):
        """Test emprunt livre déjà emprunté"""
        self.book.borrow()  # Premier emprunt
        result = self.book.borrow()  # Tentative de second emprunt
        assert result is False
        assert not self.book.is_available()
    
    def test_return_book_not_borrowed_fails(self):
        """Test retour livre non emprunté"""
        result = self.book.return_book()
        assert result is False
        assert self.book.is_available()
    
    def test_return_borrowed_book_success(self):
        """Test retour livre emprunté"""
        self.book.borrow()
        result = self.book.return_book()
        assert result is True
        assert self.book.is_available()