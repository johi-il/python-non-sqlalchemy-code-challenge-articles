class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if isinstance(value,str) and 5<=len(value)<=50:
            self._title=value
        elif hasattr(self,'_title'):
            pass
        else:
            raise ValueError("ensure input is a string with 5-50 characters")


    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = value


        
class Author:
    def __init__(self, name):
        self.name = name  # This uses the setter for validation
        self._articles=[]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            pass
        elif len(value) <= 0:
            pass
        elif hasattr(self, '_name'):
            pass
        else:
            self._name = value

    



    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})

class Magazine:
    def __init__(self, name, category):
        self._name = name #uses setter for validation
        self.category = category
        self._articles = []
    @property
    def name(self):
        return self._name
    @property
    def category (self):
        return self._category

    @name.setter
    def name(self,value):
        if isinstance(value, str) and (2<=len(value)<=16):
            self._name=value
        else:
            pass
        
    @category.setter
    def category (self,value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        
    

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        from collections import Counter
        if not self._articles:
            return None
        author_counts = Counter(article.author for article in self._articles)
        contributing = [author for author, count in author_counts.items() if count > 2]
        if not contributing:
            return None
        return contributing



# magazine = Magazine("politics monday", "internal affairs")
# print(magazine.magazine_name)
# print(magazine.category)

# article = Article("lewis","The Irungu's","40 under 40")
# print(article.title)
