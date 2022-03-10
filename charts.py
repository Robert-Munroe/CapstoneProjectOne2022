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


def build_graph(data):
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    axes.bar(
        range(len(data)),
        [data[1] for data in data],
        tick_label=[data[0] for data in data]
    )
    plt.show()
