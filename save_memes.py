
import json

class Meme:
    '''en sam meme'''
    def __init__(self, opis,x,y, ime):
        self.nastavi(opis,x,y,ime)
    def nastavi(self,opis,x,y,ime):
        self.s_tekst = opis
        self.x_coord = x
        self.y_coord = y
        self.image_name = ime

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

    def load(self):
        with open("memes.json", "r") as f:
            self.memes = json.load(f)
    
    def get_memes(self, user):
        return self.memes.get(user)

    def get_meme(self, user, ime):
        return self.memes.get(user, {}).get(ime)
