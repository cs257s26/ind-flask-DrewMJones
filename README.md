# README: Individual database Project.

## WRITE UP

**design**
My design development process for this database starts in the database. I decided to remove all columns that were not pertinent to the data set. I kept only longitude, latitude, scientific name, common name, taxon, location, and user name. I used the primary keys:  latitude, longitude, taxon_name, common_name, iconic_taxon, place_geuss,  and observer.

These were all kept because they are necessary for the leaderboard and top species (city) functions. Also, I decided to create a separate data set for each taxon rather than a single large data set. I did this because it allows for the search of the data set to provide information about each taxon more easily. Instead of searching all of the way through one database, this structured system allows us to go to each taxon specifically. As for my data types: I selected the real and text data types because that is what the utf-8 encoding allows for, and it well represents the data types: latitude, longitude, taxon_name, common_name, and iconic_taxon. I used varchar on the variables that allowed user input, which were not always UTF-8: place_geuss, and observer. This allowed me to put it in a database, which required UTF-8 encoding, so turning the information into bytes was a solid workaround. 

**User Stories**
My queries: the city and leaderboard queries represent the user stories of User Story 1 and User Story 2.

The leaderboard query spits out the top 100 spotters of a given animal in the dataset. User story 1 is:  I am an avid and competitive user of INaturalist. I want to know if I am a top contributor in a certain species sighting in Minnesota. I would really like it if the top 100 contributors for a species, of my choosing, was printed out onto a leaderboard, so I could see how I stack up to the top contributors.
This query meets the acceptance criteria and tests are satisfied: Acceptance criteria: Giving the name of an animal returns the top 100 contributors, and Acceptance tests: Common loon -> 1. Katrina 2. Justin 3. Drew etc.

User story 2 is met by the city query, which returns a list of the top species around a given area. The user story is: As a hiker in Minnesota, I want to select a city and see the most commonly observed species across major taxonomic groups so that I can quickly know what wildlife I might see. This provides access congruent with the user’s needs and meets the acceptance criteria: When I input a city, radius, and number of results, I get a list of top species.




## Copy these to create the database:
\copy birds FROM 'birds.csv' DELIMITER ',' CSV 
\copy reptiles FROM 'reptiles.csv' DELIMITER ',' CSV 
\copy mammals FROM 'mammals.csv' DELIMITER ',' CSV 
\copy insects FROM 'insects.csv' DELIMITER ',' CSV 
\copy amphibians FROM 'amphibians.csv' DELIMITER ',' CSV 



## Leaderboard Function:
### When called this function presents the top 100 sighters of a given animal.
### Enter: /leaderboard/the common name of animal/
### /leaderboard/ calls the function 
### /the common name of animal/ Serves as the user input. Note: For names greater than 1 word quotes are required


## Top Species Function
### Enter: /city/city-name/prefered-search-radius/number of species members/
### /city/ is used to call the function for routing.
### /city-name/ is where one can put the city they want to get sightings from.
### /prefered-search-radius/ is how far around from the center of the city would they like sightings to draw from.
### //number of species members/ is the number of each sort of animal, Insects, Birds, Reptiles, Amphibians, and Mammals, in their respective top sightings. 

