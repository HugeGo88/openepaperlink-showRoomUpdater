from draw_image import draw_image
from send_image import send_image
from read_mapper import read_mapper
from article import Article
from logger_setup import setup_logging
import logging

setup_logging()
logger = logging.getLogger()

logger.info("*** Starting the tag update process. ***")
# read excel

articles = [
    Article(
        "Sample Article 1", "9.99 €", "596bgj"),
    Article(
        "Sample Article 2", "19.99 €", "5069r")]

read_mapper('mapper.xlsx', articles)


for article in articles:
    if article.mac == "":
        logger.debug(f"Skipping article without MAC: {article}")
        continue
    image_path = draw_image(
        price=article.price, article_name=article.article_name)
    send_image(image_path, article.mac)

logging.info("*** Tag update process completed. ***")
