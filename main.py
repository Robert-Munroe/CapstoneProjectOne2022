from tkinter import messagebox
import api_data
import dataBaseStuff
from tkinter import *
import charts
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def report_results(data_to_write: list):
    with open("Output.txt", mode='a') as outputFile:  # open the output file for appending
        for show in data_to_write:
            print(show, file=outputFile)  # write each data item to file
            print("\n", file=outputFile)
            print("===================================================================", file=outputFile)


def get_data_and_put_in_db():
    messagebox.showinfo('Message', 'You clicked the update button!')
    connection, db_cursor = dataBaseStuff.open_db("project1db.sqlite")
    dataBaseStuff.delete_tables(db_cursor)  # smelly way to update tables, look for alternative way after
    dataBaseStuff.create_all_tables(db_cursor)
    top_show_data = api_data.get_top_250_data("TV")
    top_movie_data = api_data.get_top_250_data("Movie")
    top_show_data_for_db = api_data.prepare_top_250_data(top_show_data)
    top_movie_data_for_db = api_data.prepare_top_250_data(top_movie_data)
    most_pop_movies = api_data.get_most_popular("Movies")
    most_pop_tv = api_data.get_most_popular("TVs")
    # I'm getting sloppy here to make this quicker and the code smaller
    dataBaseStuff.put_top_250_in_database("top_show_data", top_show_data_for_db, db_cursor)
    dataBaseStuff.put_top_250_in_database("top_movie_data", top_movie_data_for_db, db_cursor)
    dataBaseStuff.put_most_popular_in_database("most_popular_movies", most_pop_movies, db_cursor)
    dataBaseStuff.put_most_popular_in_database("most_popular_shows", most_pop_tv, db_cursor)
    dataBaseStuff.put_in_wheel_of_time(db_cursor)
    big_mover_records = api_data.get_big_movers(most_pop_movies)
    big_mover_ratings = api_data.get_big_mover_ratings(big_mover_records)
    ratings_data = api_data.get_ratings(top_show_data)
    db_ready_ratings_data = api_data.prepare_ratings_for_db(ratings_data)
    dataBaseStuff.put_ratings_into_db(db_ready_ratings_data, db_cursor)
    dataBaseStuff.put_ratings_into_db(big_mover_ratings, db_cursor)
    dataBaseStuff.close_db(connection)


def graph_most_popular_movies_trending_pos():
    connection, db_cursor = dataBaseStuff.open_db("project1db.sqlite")
    data = charts.prepare_most_popular_movies_trending_pos(db_cursor)
    charts.build_graph(data)


def graph_most_popular_movies_trending_neg():
    connection, db_cursor = dataBaseStuff.open_db("project1db.sqlite")
    data = charts.prepare_most_popular_movies_trending_neg(db_cursor)
    charts.build_graph(data)


def graph_most_popular_tv_shows_trending_pos():
    connection, db_cursor = dataBaseStuff.open_db("project1db.sqlite")
    data = charts.prepare_most_popular_tv_shows_trending_pos(db_cursor)
    charts.build_graph(data)


def graph_most_popular_tv_shows_trending_neg():
    connection, db_cursor = dataBaseStuff.open_db("project1db.sqlite")
    data = charts.prepare_most_popular_tv_shows_trending_neg(db_cursor)
    charts.build_graph(data)


def table_most_popular_movies():
    connection, db_cursor = dataBaseStuff.open_db("project1db.sqlite")
    data = charts.prepare_most_popular_movies_table(db_cursor)
    charts.build_table(data)


def table_most_popular_shows():
    connection, db_cursor = dataBaseStuff.open_db("project1db.sqlite")
    data = charts.prepare_most_popular_shows_table(db_cursor)
    charts.build_table(data)


def table_most_popular_movies_in_top():
    connection, db_cursor = dataBaseStuff.open_db("project1db.sqlite")
    data = charts.prepare_most_popular_movies_in_top_250(connection)
    charts.build_table(data)


def table_most_popular_shows_in_top():
    connection, db_cursor = dataBaseStuff.open_db("project1db.sqlite")
    data = charts.prepare_most_popular_shows_in_top_250(connection)
    charts.build_table(data)


def main():

    root = Tk()
    root.title('2022 spring 4')
    root.geometry("500x500")

    update_btn = Button(root, text="Update data", command=get_data_and_put_in_db)
    update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

    #  data analysis buttons
    graph_btn = Button(root, text="Graph Most Popular Movies +", command=graph_most_popular_movies_trending_pos)
    graph_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
    graph_btn = Button(root, text="Graph Most Popular Movies -", command=graph_most_popular_movies_trending_neg)
    graph_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
    graph_btn = Button(root, text="Graph Most Popular Show +", command=graph_most_popular_tv_shows_trending_pos)
    graph_btn.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
    graph_btn = Button(root, text="Graph Most Popular Show -", command=graph_most_popular_tv_shows_trending_neg)
    graph_btn.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

    graph_btn = Button(root, text="Display table for most popular movies", command=table_most_popular_movies)
    graph_btn.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
    graph_btn = Button(root, text="Display table for most popular shows", command=table_most_popular_shows)
    graph_btn.grid(row=17, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
    graph_btn = Button(root, text="Display table for popular movies in top 250",
                       command=table_most_popular_movies_in_top)
    graph_btn.grid(row=18, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
    graph_btn = Button(root, text="Display table for popular shows in top 250", command=table_most_popular_shows_in_top)
    graph_btn.grid(row=19, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

    root.mainloop()


if __name__ == '__main__':
    main()
