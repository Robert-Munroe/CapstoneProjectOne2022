import requests
import secrets
import sys


def get_top_250movie_data() -> list[dict]:
    api_query = f"https://imdb-api.com/en/API/Top250Movies/{secrets.secret_key}"
    response = requests.get(api_query)
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    # jsonresponse is a kinda useless dictionary, but the items element has what we need
    jsonresponse = response.json()
    movie_list = jsonresponse["items"]
    return movie_list


def prepare_top_250movie_data(top_movie_data: list[dict]) -> list[tuple]:
    data_for_database = []
    for movie_data in top_movie_data:
        movie_values = list(movie_data.values())  # dict values is now an object that is almost a list, lets make it one
        # now we have the values, but several of them are strings and I would like them to be numbers
        # since python 3.7 dictionaries are guaranteed to be in insertion order
        movie_values[1] = int(movie_values[1])  # convert rank to int
        movie_values[4] = int(movie_values[4])  # convert year to int
        movie_values[7] = float(movie_values[7])  # convert rating to float
        movie_values[8] = int(movie_values[8])  # convert rating count to int
        # now covert the list of values to a tuple to easy insertion into the database
        movie_values = tuple(movie_values)
        data_for_database.append(movie_values)
    return data_for_database