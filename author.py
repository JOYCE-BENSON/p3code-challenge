class Author:
    all_authors = []
    
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) <= 0:
            raise ValueError("Name must be longer than 0 characters")
        
        self._name = name
        Author.all_authors.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, '_name'):
            if not isinstance(value, str):
                raise ValueError("Name must be a string")
            if len(value) <= 0:
                raise ValueError("Name must be longer than 0 characters")
            self._name = value
    
    def articles(self):
        from article import Article
        return [article for article in Article.all_articles if article.author == self]
    
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))
    
    def add_article(self, magazine, title):
        from article import Article
        return Article(self, magazine, title)
    
    def topic_areas(self):
        topics = list(set(article.magazine.category for article in self.articles()))
        return topics if topics else None
