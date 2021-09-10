
import json

class Memes:
    def __init__(self):
        """memes = {
            "jan": {
                "img1.jpg": {
                    "opis": "blabla1",
                    "x": 1,
                    "y": 1,
                },
                "img2.jpg": {
                    "opis": "blabla1",
                    "x": 1,
                    "y": 1,
                },
            },
            "user2": {

            }
        }
        """
        self.memes = {}
        self.uporabniki = {}

    def add_user(self, user, geslo):
        if user not in self.uporabniki:
            self.uporabniki["user"] = geslo

    def add_meme(self, user, ime, opis, x, y):
        if user not in self.memes:
            self.memes[user] = {}
        if ime not in self.memes[user]:
            self.memes[user][ime] = {}
        self.memes[user][ime]["opis"] = opis
        self.memes[user][ime]["x"] = x
        self.memes[user][ime]["y"] = y

    def save(self):
        with open("memes.json", "w") as f:
            f.write(json.dumps(self.memes))

        with open("uporabniki.json", "w") as dat:
            dat.write(json.dumps(self.uporabniki))


    def load(self):
        with open("memes.json", "r") as f:
            self.memes = json.load(f)

        with open("uporabniki.json", "r") as dat:
            self.uporabniki = json.load(dat)
    
    def get_memes(self, user):
        return self.memes.get(user)

    def get_meme(self, user, ime):
        return self.memes.get(user, {}).get(ime)
