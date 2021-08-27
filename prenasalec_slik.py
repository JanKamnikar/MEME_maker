import requests

def prenesi_sliko(url):
    response = requests.get(url)
    
    ime_slike = url.split("/")[-1]

    file = open("slike/" + ime_slike, "wb")
    file.write(response.content)
    file.close()

prenesi_sliko("https://ichef.bbci.co.uk/news/976/cpsprodpb/F1F2/production/_118283916_b19c5a1f-162b-410b-8169-f58f0d153752.jpg")