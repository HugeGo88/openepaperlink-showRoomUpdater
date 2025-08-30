from draw_image import draw_image
from send_image import send_image
from article import Article
from read_mapper import read_mapper
# read excel


# articles = [
#     {"article_name": "Hanny",
#         "price": "9.99 €", "mac": "00000272647F3E11"},
#     {"article_name": "Berni",
#         "price": "5.49 €", "mac": "00000272653D3E16"}
# ]

articles = [
    Article(
        "Sample Article 1", "9.99 €", "596bgj", "00:11:22:33:44:55"),
    Article(
        "Sample Article 2", "19.99 €", "5069r", "00:11:22:33:44:66")]

read_mapper('mapper.xlsx', articles)


for article in articles:

    image_path = draw_image(
        price=article["price"], article_name=article["article_name"])
    send_image(image_path, article["mac"])
