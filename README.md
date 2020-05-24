# Ipl-squad_builder
Finding best team composition on a particular ground and making a team based on statistics obtained from the dataset.
## Pre-Requisites
Install Selenium in your working environment using- pip install Selenium
Download the Chrome driver attached
Install pyfpgrowth package using- pip install pyfpgrowth

## Description
* Using the datasetyears.py file, team compositions of winning teams at Wankhede Stadium were imported into a csv file:teamcomposition.csv. The data was scrapped from the [Cricbuzz](https://www.cricbuzz.com/).
* Using the fp growth algorithm, the combination of -batsmen, bowlers, batting-allrounders and bowling-allrounders was found
* Web scraping was also used to find the current squad of MUmbai Indians from [howstat.com](http://www.howstat.com/cricket/home.asp) 
* Ball by ball data available in deliveries.csv was used. 
* To find player statistics only last 2019, 2018, 2017 seasons were considered.
* Players were clustered into categories-Batsman, Bowler, Bating-allrounder, Bowling-allrounder
* By keeping in mind the winning combination, team was constructed.

## Future scope 
* Players that have not played a single match were not considered as data is not available. Getting data of domestic matches and using a factor to adjust the difficulty can be done.
* The clusters formed could be improved.
* Different approaches to filling the 11 can be employed.
