import sys
import pandas as pd

DATA_FILE = "./dataset/lyrics.csv"


class Data:
    def __init__(self, name="Bob Dylan"):
        """_summary_ Get data from csv file.

        Args:
            name (str, optional): _description_. Defaults to "Bob Dylan".
        """
        self.name = name
        self.data = pd.read_csv(DATA_FILE)
        if self.data is None:
            print("Could not load data file {}".format(DATA_FILE), file=sys.stderr)
            sys.exit(1)

        self.data_info = self.data.info()
        self.data_described = self.data.describe()
        # print(self.data_info)
        # print(self.data_describe)

    def album(self):
        album_song_counts = self.data.groupby("album")["title"].count()
        album_total = (
            self.data["album"].value_counts().shape[0]
        )  # == 39 (data does not include 'Shadow Kingdom')
        print(album_song_counts)
        print("Album total: ", album_total)

    def year(self):
        yearly_song_counts = self.data.groupby("release_year")["title"].count()
        print("yearly_song_counts:\n", yearly_song_counts)

    def song(self):
        song_total = (
            self.data["title"].value_counts().shape[0]
        )  # 39 (data does not include 'Shadow Kingdom')
        print("Song total: ", song_total)

    def lyrics(self):
        all_lyrics = self.data["lyrics"]
        print(all_lyrics)


def main():
    app = Data()
    app.album()
    app.song()
    app.year()
    app.lyrics()


if __name__ == "__main__":
    main()
