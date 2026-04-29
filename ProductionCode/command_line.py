#in this file we'll call our 3 teammate's files
import argparse
import sys

from ProductionCode.top_species_command_line import (
    forward_geocode,
    filter_by_radius,
    top_species_by_taxon,
)
from ProductionCode.game_command_line import game

from ProductionCode.top_species_command_line import load_data as load_species_data
from ProductionCode.game_command_line import load_data as load_game_data

from ProductionCode.leaderboard_command_line import load_data as load_leaderboard_data
from ProductionCode.leaderboard_command_line import create_leaderboard
from ProductionCode.leaderboard_command_line import check_for_improper_request

def cmd_leaderboard(args):
    """Displays the top 100 species-specific contributors to INaturalist in Minnesota for a given animal. 
    
    Args:
        args: Parsed command-line arguments. Expects args.animal (str).
        
    Return:
    total_output (str of strs): This is what the out would be line by line returned as a string of strings."""

    username_key_storage = []
    username_counts = {}
    total_output = []

    creature_of_interest = args
    data = load_leaderboard_data()
    if check_for_improper_request(creature_of_interest):
        username_key_storage, username_counts, total_output = create_leaderboard(creature_of_interest, data)
        return total_output
    else: 
        return "The common_name species does not exist, please try again."
    

def cmd_species(city, radius = 5, top = 3):
    """Finds most observed species near a location in Minnesota.
    
    Args:
        args: Parsed command-line arguments. Expects args.city (str), optional args.radius (float), and optional args.top (int).
    """

    total_output_species = []
    data = load_species_data()
    coords = forward_geocode(city)
    if coords is None:
        return f"Could not geocode '{city}'."
        sys.exit(1)
    lat, lon = coords
    observations = filter_by_radius(data, lat, lon, radius)
    if len(observations) == 0:
        return f"No observations found near '{city}'. Make sure your location is in Minnesota."
        sys.exit(1)

    total_output_species.append(f"Found {len(observations)} observations within {radius} miles of {city}:")

    top_by_taxon = top_species_by_taxon(observations, int(top))
    for taxon_group, species_list in top_by_taxon.items():
        total_output_species.append(f"{taxon_group.capitalize()}:")
        for taxon_name, common_name, count in species_list:
            total_output_species.append(f"{common_name} ({taxon_name}): {count} observations")

    return total_output_species


def cmd_game(args):
    """Starts the mammal guessing game.
    
    Args:
        args: Parsed command-line arguments. No additional arguments expected.
    """
    game(load_game_data())


def main():
    parser = argparse.ArgumentParser(prog="command_line.py")
    sub = parser.add_subparsers(dest="command", required=True)

    p_species = sub.add_parser("species", help="Find commonly observed species near a MN location")
    p_species.add_argument("city", type=str, help="e.g. 'Northfield, Minnesota'")
    p_species.add_argument("--radius", type=float, default=10)
    p_species.add_argument("--top", type=int, default=3)
    p_species.set_defaults(func=cmd_species)

    p_game = sub.add_parser("game", help="Run the mammal guessing game")
    p_game.set_defaults(func=cmd_game)

    p_leaderboard = sub.add_parser("leaderboard", help="Find the top 100 species-specific contributors to INaturalist in Minnesota")
    p_leaderboard.add_argument("animal", type=str, help="e.g. 'Muskrat'")
    p_leaderboard.set_defaults(func=cmd_leaderboard)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

