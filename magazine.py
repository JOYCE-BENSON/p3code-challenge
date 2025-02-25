class Magazine:
    all_magazines = []
    
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if len(category) <= 0:
            raise ValueError("Category must be longer than 0 characters")
        
        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value) <= 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value
    
    def articles(self):
        from lib.article import Article
        return [article for article in Article.all_articles if article.magazine == self]
    
    def contributors(self):
        return list(set(article.author for article in self.articles()))
    
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
    
    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self.articles())
        authors_with_multiple = [author for author, count in author_counts.items() if count > 2]
        return authors_with_multiple if authors_with_multiple else None
    
    @classmethod
    def top_publisher(cls):
        if not Magazine.all_magazines:
            return None
        
        from lib.article import Article
        if not Article.all_articles:
            return None
        
        magazine_article_counts = {magazine: len(magazine.articles()) for magazine in Magazine.all_magazines}
        return max(magazine_article_counts.items(), key=lambda x: x[1])[0] if magazine_article_counts else None