<html>
    <head>

    </head>
    <body>
        <h1>Dobrodosli v meme generatorju</h1>

        <p>Izberi svoje uporabnisko ime: (trenutno ime je {{ username }})</p>

        <form method="post">
            <input name="username" type="text" value="{{username}}"/>
            <input name="geslo" type="text"/>
            <input type="submit" />
        </form>

        % if pravilnost == True:
        <a href="/choose_image">Izberi sliko</a>

    </body>
</html>