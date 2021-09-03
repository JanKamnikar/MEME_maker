<html>
    <head>
        <link rel="stylesheet" href="stili/stili.css">
    </head>
    <body>
        <h1>Izbira svoje slike</h1>
        <img src="slika/{{ image_name }}">
        
        <form class="new-image" method="post">
            <p>Prenesi svojo sliko </p>
            <input name="url_slike" type="text" value="" />
            <input type="submit" value="Končano" />
        </form>
       
        <a href="/converter">Naprej na urejevalnik slike</a>
        <a href="/">Nazaj na naslovno stran</a>
    </body>
</html>