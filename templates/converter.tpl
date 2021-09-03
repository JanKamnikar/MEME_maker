<html>
    <head>
        <link rel="stylesheet" href="stili/stili.css">
    </head>
    <body>
        <img src="slika/{{ image_name }}">

        <form method="post">
            <p>Tekst: </p>
            <input name="tip_obrazca_tekst" type="text" value="{{ i_tekst }}" />
            <p>Vertikalni odmik</p>
            <input name="tip_obrazca_x_coord" type="number" value="{{ i_x_coord }}" />
            <p>Horizontalni odmik</p>
            <input name="tip_obrazca_y_coord" type="number" value="{{ i_y_coord }}" />
            <input type="submit" value="Končano" />
        
        </form>
        
        <p class="plavajoci-tekst" style="top: {{ str(i_x_coord+20) }}px; left: {{ str(i_y_coord+20) }}px; max-width: {{ str(500-i_y_coord) }};" >{{ i_tekst }}</p>
        
        <p class="watermark" style="position: absolute; top: 480px; left: 350; font-size: 15px; background-color:white;" >Avtor slike: {{ username }}</p>

        <a href="/choose_image">Nazaj na izbiro slike</a>

         <a href="/all_memes">seznam vseh memov</a>
    </body>
</html>