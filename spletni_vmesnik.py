from prenasalec_slik import prenesi_sliko
import bottle
import save_memes
from save_memes import Memes

privzeto_s_tekst = "Vpiši tekst"
privzeto_x_coord = 20
privzeto_y_coord = 30
privzeto_ime = "neprijavljen_uporabnik"
privzeto_image_name = "test.jpg"

memes = Memes()

@bottle.route("/slika/<name>")
def serve_pictures(name):
    return bottle.static_file(name, "slike")

@bottle.route("/stili/<name>")
def serve_pictures(name):
    return bottle.static_file(name,"stili" )

@bottle.get("/")
def naslovna_stran():
    username = bottle.request.get_cookie("Username") or privzeto_ime
    return bottle.template("templates/naslovna_stran.tpl", username=username)

@bottle.post("/")
def nastavi_ime():
    username = bottle.request.forms.get("username") or privzeto_ime
    bottle.response.set_cookie('Username', username)
    return bottle.redirect("/")

@bottle.get("/converter")
def converter():
    username = bottle.request.get_cookie('Username') or privzeto_ime
    qimage_name = bottle.request.query.img
    if qimage_name:
        image_name = qimage_name
        meme = memes.get_meme(username, qimage_name)
        if meme:
            s_tekst = meme["opis"]
            x_coord = meme["x"]
            y_coord = meme["y"]

    else:
        image_name = bottle.request.get_cookie('image_name') or privzeto_image_name
        s_tekst = bottle.request.get_cookie('s_tekst') or privzeto_s_tekst
        x_coord = int(bottle.request.get_cookie('x_coord') or privzeto_x_coord)
        y_coord = int(bottle.request.get_cookie('y_coord') or privzeto_y_coord)

    return bottle.template("templates/converter.tpl", 
                           i_tekst=s_tekst, 
                           i_x_coord=x_coord, 
                           i_y_coord=y_coord, 
                           image_name=image_name, 
                           username=username)

@bottle.get("/error")
def napaka():
    return bottle.template("templates/error.tpl")

@bottle.post("/converter")
def spremeni_tekst():
    global memes
    #global s_tekst, x_coord, y_coord
    username = bottle.request.get_cookie('Username') or privzeto_ime
    image_name = bottle.request.get_cookie('image_name') or privzeto_image_name
    s_tekst = bottle.request.forms.get("tip_obrazca_tekst")
    x_coord = int(bottle.request.forms.get("tip_obrazca_x_coord"))
    y_coord = int(bottle.request.forms.get("tip_obrazca_y_coord"))

    bottle.response.set_cookie('s_tekst', s_tekst)
    bottle.response.set_cookie('x_coord', str(x_coord))
    bottle.response.set_cookie('y_coord', str(y_coord))

    memes.add_meme(username, image_name, s_tekst, x_coord, y_coord)
    memes.save()

    if x_coord > 400:
        x_coord = 30
        return bottle.redirect("/error")
    if y_coord > 400:
        y_coord = 20
        return bottle.redirect("/error")
    
    return bottle.redirect("/converter")

@bottle.get("/choose_image")
def choose_image():
    #image_name = bottle.request.forms.get("image_name") or privzeto_image_name
    image_name = bottle.request.get_cookie('image_name') or privzeto_image_name
    return bottle.template("templates/izberi_sliko.tpl", image_name=image_name)

@bottle.get("/all_memes")
def choose_image():
    username = bottle.request.get_cookie('Username') or privzeto_ime
    memes.load()
    my_memes = memes.get_memes(username)
    #image_name = bottle.request.forms.get("image_name") or privzeto_image_name
    #image_name = bottle.request.get_cookie('image_name') or privzeto_image_name
    return bottle.template("templates/all_memes.tpl", my_memes=my_memes)


@bottle.post("/choose_image")
def download_image():
    url = bottle.request.forms.get("url_slike")
    url = url.split("?")[0]
    prenesi_sliko(url)
    image_name = url.split("/")[-1]
    print("prenesel_sliko", image_name)
    '''shranis url slike v cookie'''
    bottle.response.set_cookie('image_name', image_name)
    return bottle.redirect("/choose_image")
    
bottle.run(debug=True, reloader=True)