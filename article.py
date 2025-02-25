class Article:
    all_articles = []
    
    def __init__(self, author, magazine, title):
        from lib.author import Author
        from lib.magazine import Magazine
        
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        
        self._title = title
        self._author = author
        self._magazine = magazine
        Article.all_articles.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not hasattr(self, '_title'):
            if not isinstance(value, str):
                raise ValueError("Title must be a string")
            if not (5 <= len(value) <= 50):
                raise ValueError("Title must be between 5 and 50 characters")
            self._title = value
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        from lib.author import Author
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        from lib.magazine import Magazine
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine = value