# README: Individual database Project.

## No instructions yet, I got stuck on the data cleaning for many hours. Thus my submission is absent the rest of the requirements.

## Eventually I would have shaped out like this:
\copy birds FROM 'birds.csv' DELIMITER ',' CSV 
\copy reptiles FROM 'reptiles.csv' DELIMITER ',' CSV 
\copy mammals FROM 'mammals.csv' DELIMITER ',' CSV 
\copy insects FROM 'insects.csv' DELIMITER ',' CSV 
\copy amphibians FROM 'amphibians.csv' DELIMITER ',' CSV 

# README: Individual Flask project.

## Leaderboard Function:
### When called this function presents the top 100 sighters of a given animal.
### Enter: /leaderboard/the common name of animal/
### /leaderbaord/ calls the function 
### /the common name of animal/ Serves as the user input. Note: For names greater than 1 word quotes are required


## Top Species Function
### Enter: /city/city-name/prefered-search-radius/number of species members/
### /city/ is used to call the function for routing.
### /city-name/ is where one can put the city they want to get sightings from.
### /prefered-search-radius/ is how far around from the center of the city would they like sightings to draw from.
### //number of species members/ is the number of each sort of animal, Insects, Birds, Reptiles, Amphibians, and Mammals, in their respective top sightings. 

