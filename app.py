from flask import Flask
app = Flask(__name__)

from ProductionCode import *
from ProductionCode.command_line import *
from ProductionCode.top_species_command_line import *
from Data import *
from Data.psqlConfig import *
from Data.datasource import *
from werkzeug.wrappers import Request, Response
from flask import Flask

@app.route("/")
def homepage():
    """This function displays the default instructions on the basic / HTTP page. """
    
    return "Hi please enter /city/city-name/prefered-search-radius/number of species members/ or /leaderboard/common name of animal/."



@app.route("/leaderboard_db/<common_name_of_animal>/")
def return_leaders_db(common_name_of_animal):
    """This function displays a list of the top 10 leaderboard for a species sighting.
        The Leaderboard calls for this function and the passed through variable is common_name_of_animal.
    
    args:
        common_name_of_animal (string): the HTTPS leads into the commandline leaderboard function.

    Return (string): THe top 100 leaders for the species sightings.
    """
    connection = connect()
    total_output = get_animal(connection, common_name_of_animal)

    #SELECT common_name,COUNT(*) FROM birds WHERE latitude BETWEEN 45.01 AND 49 AND longitude BETWEEN -90 AND -92 GROUP BY common_name ORDER BY COUNT(*) DESC;
    
    return total_output

@app.route("/leaderboard/<common_name_of_animal>/")
def return_leaders(common_name_of_animal):
    """This function displays a list of the top 100 leaderboard for a species sighting.
        The Leaderboard calls for this function and the passed through variable is common_name_of_animal.
    
    args:
        common_name_of_animal (string): the HTTPS leads into the commandline leaderboard function.

    Return (string): THe top 100 leaders for the species sightings.
    """
   
    total_output = cmd_leaderboard(common_name_of_animal)
    
    return total_output


@app.route("/city/<city>/<radius>/<top>/")
def species(city, radius = 5, top = 3):
    """Using /city/ routes to the cmd_species function in the commandline arguement(cmd_species), this function outputs the
    top found species around a city
    
    args: city (string): The HTTP city request.
        radius (int): How far from the city location should the search look for.
        top (int): How many of each type of species does the user want to have displayed.
    
    return: The top sightings around a city in each species catagory.
    """

    species_output = cmd_species(city, radius, top)

    return species_output


@app.errorhandler(404)
def page_not_found(e):
    """This routes a errant HTTP input to this error. It then outputs that the HTTP was entered incorrectly. """

    return "The URL input is incorrectly formatted, /city/city-name/prefered search radius/number of species members/ or /leaderboard/common name of animal/ is needed."


if __name__ == "__main__":
    app.run(port = 8001, debug = True)
