from draw_image import draw_image
from send_image import send_image
# read excel

# map article to tag

articles = [
    {"article_name": "Sample Article 1",
        "price": "9.99 €", "mac": "00000272647F3E11"},
    {"article_name": "Sample Article 2",
        "price": "5.49 €", "mac": "00000272653D3E16"},
    #    {"article_name": "Sample Article 3", "price": "12.00 €", "mac": "AA:BB:CC:DD:EE:03"},
]

for article in articles:

    image_path = draw_image(
        price=article["price"], article_name=article["article_name"])
    send_image(image_path, article["mac"])
