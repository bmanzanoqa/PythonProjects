# we are going to need our 'app OBJECT' and our 'db OBJECT' (because we are going to mess with our DB)
from application import app, db
# the file models in the folder application (application.models) contains our 'Games Table' (class Games)
from application.models import Games


@app.route('/add')  # every route must come with a function (line 6)
def add():
    # this creates a new game in our Games' table called "New Game"
    new_game = Games(name="New Game")
    # this is how we create something and we add a new game
    db.session.add(new_game)
    db.session.commit()  # to save
    # A message on the screen to let the user know I have added a new game
    return "Added new game to database"


''' Every single time someone goes to /add:
    1. it will execute the function 'add' (line 6)
        1. it will create a new game (line 7)
        2. add the game to our db (line 8)
        3. save it in our db (line 9)
        4. It will return the message "Added a new game to db" '''


@app.route('/read')
def read():
    # creates a variable ('all_games') that will store all the games. This gives us a list with every single game in there
    all_games = Games.query.all()
    games_string = ""  # creates an empty string
    for game in all_games:  # for loop; 'game' will be every game in the string list created in line 23
        # 'game' = to an entry; 'name' = the name of the game added
        games_string += "<br>" + game.name
    # once it has gone through all of them, the game_string will contain every single game
    return games_string


# '<name> is a variable, we want them to give a name
@app.route('/update/<new_name>')
def update(new_name):  # you have to enter the variable into the function as well
    first_game = Games.query.first()
    # so whatever new name are they passing in the url it is going to assign that to the first name in the list
    first_game.name = new_name
    db.session.commit()
    return first_game.name  # it will show in the screen what the new name is
