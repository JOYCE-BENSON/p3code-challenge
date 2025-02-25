#!/usr/bin/env python3

import ipdb

from lib.article import Article
from lib.author import Author
from lib.magazine import Magazine

if __name__ == '__main__':
    # Sample test data
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    
    magazine1 = Magazine("Tech Review", "Technology")
    magazine2 = Magazine("Science Today", "Science")
    magazine3 = Magazine("Art World", "Art")
    
    article1 = author1.add_article(magazine1, "The Future of AI")
    article2 = author1.add_article(magazine2, "Quantum Computing Explained")
    article3 = author2.add_article(magazine1, "Programming in Python")
    article4 = author2.add_article(magazine1, "Web Development Trends")
    article5 = author2.add_article(magazine1, "Mobile App Design")
    
    # Debug here
    ipdb.set_trace()
    
    # Example debugging statements
    # print(f"Author1's name: {author1.name}")
    # print(f"Author1's articles: {[a.title for a in author1.articles()]}")
    # print(f"Author1's magazines: {[m.name for m in author1.magazines()]}")
    # print(f"Author1's topic areas: {author1.topic_areas()}")
    # print(f"Magazine1's articles: {[a.title for a in magazine1.articles()]}")
    # print(f"Magazine1's contributors: {[a.name for a in magazine1.contributors()]}")
    # print(f"Magazine1's article titles: {magazine1.article_titles()}")
    # print(f"Magazine1's contributing authors: {[a.name for a in magazine1.contributing_authors() or []]}")
    # print(f"Top publisher: {Magazine.top_publisher().name if Magazine.top_publisher() else None}")