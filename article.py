class Article:
    def __init__(self, article_name: str, price: str, article_id: str, mac: str = ""):
        self.article_name = article_name
        self.price = price
        self.mac = mac
        self.article_id = article_id

    def __repr__(self):
        return f"Article(name='{self.article_name}', price='{self.price}', mac='{self.mac}')"
