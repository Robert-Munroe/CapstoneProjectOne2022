# import numpy as np
import matplotlib.pyplot as plt


def basic_bar_graph():
    x = ['a', 'b', 'c', 'd']
    value = [1, 4, 7, 1]
    plt.bar(x, value)
    plt.show()


def prepare_most_popular_movies_trending_pos(connection):
    return connection.execute('SELECT title, rankchange FROM most_popular_movies WHERE rankchange >= 0 GROUP BY title;'
                              '').fetchall()


def prepare_most_popular_tv_shows_trending_pos(connection):
    return connection.execute('SELECT title, rankchange FROM most_popular_shows WHERE rankchange >= 0 GROUP BY title;'
                              '').fetchall()


def prepare_most_popular_movies_trending_neg(connection):
    return connection.execute('SELECT title, rankchange FROM most_popular_movies WHERE rankchange < 0 GROUP BY title;'
                              '').fetchall()


def prepare_most_popular_tv_shows_trending_neg(connection):
    return connection.execute('SELECT title, rankchange FROM most_popular_shows WHERE rankchange < 0 GROUP BY title;'
                              '').fetchall()


def prepare_most_popular_movies_table(connection):
    return connection.execute('SELECT title, rank FROM most_popular_movies GROUP BY title').fetchall()


def prepare_most_popular_shows_table(connection):
    return connection.execute('SELECT title, rank FROM most_popular_shows GROUP BY title').fetchall()


def prepare_most_popular_movies_in_top_250(connection):
    most_popular_movies_title_ttid = connection.execute('SELECT title FROM most_popular_movies '
                                                        'GROUP BY title').fetchall()
    top_250_movies_title_ttid = connection.execute('SELECT title FROM top_movie_data GROUP BY title').fetchall()
    set_of_popular = set(most_popular_movies_title_ttid)
    set_of_top = set(top_250_movies_title_ttid)
    data = set_of_popular.intersection(set_of_top)
    data = list(data)
    return data


def prepare_most_popular_shows_in_top_250(connection):
    most_popular_movies_title_ttid = connection.execute('SELECT title FROM most_popular_shows '
                                                        'GROUP BY title').fetchall()
    top_250_movies_title_ttid = connection.execute('SELECT title FROM top_show_data GROUP BY title').fetchall()
    set_of_popular = set(most_popular_movies_title_ttid)
    set_of_top = set(top_250_movies_title_ttid)
    data = set_of_popular.intersection(set_of_top)
    data = list(data)
    return data


def build_graph(data):
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    axes.bar(
        range(len(data)),
        [data[1] for data in data],
        tick_label=[data[0] for data in data]
    )
    plt.show()


def build_table(data):
    fig, ax = plt.subplots()
    table_data = data
    table = ax.table(cellText=table_data, loc='center')
    table.set_fontsize(14)
    ax.axis('off')
    plt.show()
