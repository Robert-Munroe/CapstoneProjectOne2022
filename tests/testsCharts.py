import charts
import dataBaseStuff


def test_most_popular_movies_in_top_is_list():
    connection, db_cursor = dataBaseStuff.open_db("project1db.sqlite")
    data = charts.prepare_most_popular_movies_in_top_250(connection)
    boolean = type(data) is list
    assert boolean is True
