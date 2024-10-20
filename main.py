import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

DATA = "./dataset/raw/raw_data.csv"

data = pd.read_csv(DATA)
data_info = data.info()
data_described = data.describe()

if data is None:
    print("Could not load data file {}".format(DATA), file=sys.stderr)
    sys.exit(1)


def get_albums_by_year():
    albums_by_year = data[["release_year", "album"]]
    albums_by_year.drop_duplicates(subset=["album"], inplace=True)
    albums_by_year.to_csv("./dataset/processed/albums_by_year.csv", index=False)
    return albums_by_year


def get_songs_by_year():
    songs_by_year = data[["release_year", "title"]]
    songs_by_year.drop_duplicates(subset=["title"], inplace=True)
    songs_by_year.to_csv("./dataset/processed/songs_by_year.csv", index=False)
    return songs_by_year


def album_release_by_decade_density(source):
    """
    https://www.data-to-viz.com/graph/histogram.html
    """
    sns.set_theme(style="darkgrid")
    sns.displot(
        source["release_year"],
        kde=True,
        rug=True,
        rug_kws={"alpha": 0.2, "linewidth": 4, "height": 0.2},
        fill=True,
    )
    plt.title("Album Release Distribution")
    plt.xlabel("Decade")
    plt.ylabel("Album Count")
    plt.show()


def create_word_cloud():
    # Create a list of word
    text = data[["lyrics"]].to_string()

    # Create the wordcloud object
    wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()


def main():
    albums = get_albums_by_year()
    # album_release_by_decade_density(albums)
    songs = get_songs_by_year()
    create_word_cloud()


if __name__ == "__main__":
    main()
