<html>
    <head>
    </head>
    <body>
       <% for ime_img in my_memes: %> 
       
       <a href="/converter?img={{ ime_img }}">{{ ime_img }}</a>
        <% end %>  
    </body>
</html>