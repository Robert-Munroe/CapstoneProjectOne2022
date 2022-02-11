# CapstoneProjectOne2022

1. Robert Munroe
2. json should be imported, but no install needed. You will need to install pytest.
3. This project pulls the top 250 shows from IMBD's api. 
it then gets the user rankings for the top 1, 50, 100, and 200th
ranked show. It also pulls the user rankings for The Wheel of Time
show. Once it has this data it will create and populate a database with this data.

250tvshows' database is broken down into 7 columns: tv show id, title, full title,
year it came out the crew that worked on the show, the imdb rating, and the
amount of ratings. 

userdata table has many more columns. it has an imbdId code, total ratings, the number of votes.
Then the table has columns for ratings 1-10 which has two parts.
The total amount of people who voted X rating and the % of people who voted X ratings. 

4. I am only missing a test to ensure i've put the data into the database properly
5. I also lost the ability to use github actions somewhere along the way even
after copying and pasting the file posted in slack