<html>
    <head>
        <link rel="stylesheet" href="stili/stili.css">
    </head>
    <body>
        <p style="color:red;"> samo klikni na ime slike in meme,
         ki si ga shranil pod sliko se bo prikazal </p>
       <% for ime_img in my_memes: %> 
       
       <a href="/converter?img={{ ime_img }}">{{ ime_img }}</a>
        <% end %>  
    </body>
</html>