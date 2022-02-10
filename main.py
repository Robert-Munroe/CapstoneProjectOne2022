import sys

import requests

import secrets

import sqlite3

from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS top250tvshows(
    title_code TEXT NOT NULL,
    tv_show_title TEXT NOT NULL,
    tv_show_full_title TEXT NOT NULL,
    tv_show_year INTEGER NOT NULL,
    crew_members TEXT NOT NULL,
    imbd_ranking INTEGER DEFAULT 0,
    imbrating_count INTEGER DEFAULT 0,
    PRIMARY KEY(title_code)
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS user_rankings(
    imbdId TEXT NOT NULL,
    total_rankins INTEGER DEFAULT 0,
    total_ranking_votes INTEGER DEFAULT 0,
    ten_rankings INTEGER DEFAULT 0,
    ten_ranking_votes INTEGER DEFAULT 0,
    nine_rankings INTEGER DEFAULT 0,
    nine_ranking_votes INTEGER DEFAULT 0,
    eight_rankings INTEGER DEFAULT 0,
    eight_ranking_votes INTEGER DEFAULT 0,
    seven_rankings INTEGER DEFAULT 0,
    seven_ranking_votes INTEGER DEFAULT 0,
    six_rankings INTEGER DEFAULT 0,
    six_ranking_votes INTEGER DEFAULT 0,
    five_rankings INTEGER DEFAULT 0,
    five_ranking_votes INTEGER DEFAULT 0,
    four_rankings INTEGER DEFAULT 0,
    four_ranking_votes INTEGER DEFAULT 0,
    three_rankings INTEGER DEFAULT 0,
    three_ranking_votes INTEGER DEFAULT 0,
    two_rankings INTEGER DEFAULT 0,
    two_ranking_votes INTEGER DEFAULT 0,
    one_rankings INTEGER DEFAULT 0,
    one_ranking_votes INTEGER DEFAULT 0,
    PRIMARY KEY(imbdId)
    );''')


def add_250_show_data(cursor: sqlite3.Cursor, data):
    for i in range(len(data)):
        temp_tuple = data[i]['id'], data[i]['title'], data[i]['fullTitle'], data[i]['year'], data[i]['crew'], \
               data[i]['imDbRating'], data[i]['imDbRatingCount']
        cursor.execute('INSERT INTO top250tvshows VALUES(?, ?, ?, ?, ?, ?, ?);', temp_tuple)


def get_top_250_data() -> list[dict]:
    api_query = f"https://imdb-api.com/en/API/Top250TVs/{secrets.api_key}"
    response = requests.get(api_query)
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    # jsonresponse is a kinda useless dictionary, but the items element has what we need
    jsonresponse = response.json()
    show_list = jsonresponse["items"]
    return show_list


def report_results(data_to_write: list[dict]):
    with open("Output.txt", mode='a') as outputFile:  # open the output file for appending
        for show in data_to_write:
            print(show, file=outputFile)  # write each data item to file
            print("\n", file=outputFile)
            print("===================================================================", file=outputFile)


def get_ratings(top_show_data: list[dict]) -> list[dict]:
    results = []
    api_queries = []
    base_query = f"https://imdb-api.com/en/API/UserRatings/{secrets.api_key}/"
    wheel_of_time_query = f"{base_query}tt7462410"
    api_queries.append(wheel_of_time_query)
    first_query = f"{base_query}{top_show_data[0]['id']}"
    api_queries.append(first_query)
    fifty_query = f"{base_query}{top_show_data[49]['id']}"
    api_queries.append(fifty_query)
    hundred_query = f"{base_query}{top_show_data[99]['id']}"
    api_queries.append(hundred_query)
    two_hundred = f"{base_query}{top_show_data[199]['id']}"
    api_queries.append(two_hundred)
    for query in api_queries:
        response = requests.get(query)
        if response.status_code != 200:  # if we don't get an ok response we have trouble, skip it
            print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
            continue
        rating_data = response.json()
        results.append(rating_data)
    return results


def main():

    top_show_data = get_top_250_data()
    # ratings_data = get_ratings(top_show_data)
    # report_results(ratings_data)
    # report_results(top_show_data)
    conn, cursor = open_db("250_TV_Show_Table.sqlite")
    print(type(conn))
    setup_db(cursor)
    add_250_show_data(cursor, top_show_data)
    close_db(conn)


if __name__ == '__main__':
    main()
