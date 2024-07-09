class Article():
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.include_article(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        if (type(title) == str) and ( 5 <= len(title) <= 50) and (not(hasattr(self, '_title'))):
            self._title = title
        else:
            print("Title has to be a string gretaer than 5 and less 50 characters. Once created it cannot be changed.")
    
    @classmethod
    def include_article(cls,article):
        cls.all.append(article)    

class Author():
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if (type(name) == str) and (len(name) > 0) and (not(hasattr(self, '_name'))):
            self._name = name
        else:
            print("Name has to be a string greater than 0 characters. Once created it cannot be changed.")

    def articles(self):
        articles_list = []
        for article in Article.all:
            if article.author == self:
                articles_list.append(article)
        return articles_list

    def magazines(self):
        magazines_set = set()
        authors_articles = Author.articles(self)
        for article in authors_articles:
            magazines_set.add(article.magazine)
        return list(magazines_set)

    def add_article(self, magazine, title):
        new_article = Article(self,magazine,title)
        return new_article

    def topic_areas(self):
        topics = set()
        authors_magazines = Author.magazines(self)
        if len(authors_magazines) == 0:
            return None
        else:
            for magazine in authors_magazines:
                topics.add(magazine.category)
        return list(topics)   

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if (type(name) == str) and (2 <= len(name) <= 16):
            self._name = name
        else:
            print("Name has to be a string greater than 2 and less than 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self,category):
        if (type(category) == str) and (len(category) > 0):
            self._category = category
        else:
            print("Category has to be a string greater than 0 characters.") 

    def articles(self):
        articles_list = []
        for article in Article.all:
            if article.magazine == self:
                articles_list.append(article)
        return articles_list

    def contributors(self):
        authors_list = set()
        for article in self.articles():
            authors_list.add(article.author)
        return list(authors_list)

    def article_titles(self):
        titles = []
        articles = Magazine.articles(self)
        if len(articles) == 0:
            return None
        else:
            for article in articles:
                titles.append(article.title)
        return titles

    def contributing_authors(self):
        authors = []
        articles = Magazine.articles(self)
        for article in articles:
            authors.append(article.author)
        checked = []
        contributors = set()
        for author in authors:
            if author in checked:
                contributors.add(author)
            else:
                checked.append(author)
        return None if len(contributors) == 0 else list(contributors)
