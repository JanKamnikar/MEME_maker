from prenasalec_slik import prenesi_sliko
import bottle

s_tekst = "Ko se ti ne da pisati seminarse naloge za UVP"
x_coord = 20
y_coord = 30
image_name = "test.jpg"
username = "uporabnik123"

@bottle.route("/slika/<name>")
def serve_pictures(name):
    return bottle.static_file(name, "slike")

@bottle.route("/stili/<name>")
def serve_pictures(name):
    return bottle.static_file(name,"stili" )


@bottle.get("/")
def naslovna_stran():
    return bottle.template("templates/naslovna_stran.tpl", username=username)

@bottle.post("/")
def nastavi_ime():
    global username
    username = bottle.request.forms.get("username")
    bottle.response.set_cookie('Username', username)
    return bottle.redirect("/")

@bottle.get("/converter")
def converter():
    global username
    username = bottle.request.get_cookie('Username')
    return bottle.template("templates/converter.tpl", i_tekst=s_tekst, i_x_coord=x_coord, i_y_coord=y_coord, image_name=image_name, username=username)

@bottle.get("/error")
def napaka():
    return bottle.template("templates/error.tpl")

@bottle.post("/converter")
def spremeni_tekst():
    global s_tekst, x_coord, y_coord
    s_tekst = bottle.request.forms.get("tip_obrazca_tekst")
    x_coord = int(bottle.request.forms.get("tip_obrazca_x_coord"))
    y_coord = int(bottle.request.forms.get("tip_obrazca_y_coord"))

    if x_coord > 400:
        x_coord = 30
        return bottle.redirect("/error")
    if y_coord > 400:
        y_coord = 20
        return bottle.redirect("/error")
    
    return bottle.redirect("/converter")

@bottle.get("/choose_image")
def choose_image():
    return bottle.template("templates/izberi_sliko.tpl", image_name=image_name)

@bottle.post("/choose_image")
def download_image():
    global image_name
    url = bottle.request.forms.get("url_slike")
    url = url.split("?")[0]
    prenesi_sliko(url)
    image_name = url.split("/")[-1]
    print("prenesel_sliko", image_name)
    return bottle.redirect("/choose_image")

bottle.run(debug=True, reloader=True)