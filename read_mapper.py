import pandas as pd
from article import Article


def read_mapper(path, articles):
    # Load the Excel file
    df = pd.read_excel(path)
    print(df.head())
    mappings = df.to_dict(orient='records')

    for article in articles:
        for mapping in mappings:
            if article.article_id == mapping.get("Article"):
                article.mac = mapping.get("MAC")
                print(f"Updated article: {article}")

    return articles


if __name__ == "__main__":
    read_mapper('mapper.xlsx', articles=[
        Article(
            "Sample Article 1", "9.99 €", "596bgj", "00:11:22:33:44:55"),
        Article(
            "Sample Article 2", "19.99 €", "5069r", "00:11:22:33:44:66")])
