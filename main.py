# Robert Munroe Senior Capstone Project 1

import requests
import secrets
import json

# out of dictionary takes the raw data given from json, and the key of the dictionary
# and only returns the list


def out_of_dictionary(data, qualifier: str):
    new_data = data.get(qualifier)
    return new_data

# get tv show title id searches the api for a string and returns just the imbd tv show id


def get_tv_show_title_id(tv_show_title: str):
    url = 'https://imdb-api.com/en/API/SearchTitle/' + secrets.api_key + "/" + tv_show_title
    results = requests.get(url)
    if results.status_code != 200:
        print('hmm')
        return
    data = results.json()
    list_of_show = out_of_dictionary(data, 'results')
    show_title_id = list_of_show[0]['id']
    return show_title_id

# get tv show data takes the id code of a tv show and returns the user data


def get_tv_show_data(title_code: str):
    url = 'https://imdb-api.com/en/API/UserRatings/' + secrets.api_key + "/" + title_code
    results = requests.get(url)
    if results.status_code != 200:
        print("hmm")
        return
    data = results.json()
    return data

# get 50th tv show data takes in the list of the top 250 tv shows, searches for a rank, and returns the id when the
# rank matches the one I want, and then search the user data api with the id given
# the same process is repeated for 100, 150, 200 - I plan to look for a way to combine these on my free time


def get_50th_tv_show_data(top_250_show_list):

    for i in range(len(top_250_show_list)):
        if top_250_show_list[i]['rank'] == '50':
            return get_tv_show_data(top_250_show_list[i]['id'])


def get_100th_tv_show_data(top_250_show_list):

    for i in range(len(top_250_show_list)):
        if top_250_show_list[i]['rank'] == '100':
            return get_tv_show_data(top_250_show_list[i]['id'])


def get_top_150_tv_show_data(top_250_show_list):

    for i in range(len(top_250_show_list)):
        if top_250_show_list[i]['rank'] == '150':
            return get_tv_show_data(top_250_show_list[i]['id'])


def get_top_200_tv_show_data(top_250_show_list):

    for i in range(len(top_250_show_list)):
        if top_250_show_list[i]['rank'] == '200':
            return get_tv_show_data(top_250_show_list[i]['id'])


def get_data():
    # provides a dictionary of dictionaries
    url = "https://imdb-api.com/en/API/Top250TVs/" + secrets.api_key
    # final_url = url + secrets.api_key
    results = requests.get(url)
    if results.status_code != 200:
        print("hmmm")
        return
    data = results.json()
    list_of_data = out_of_dictionary(data, 'items')
    return list_of_data


def print_to_file(top50, top100, top150, top200, wheeloftime):
    f = open("total_data.txt", "w+")
    f.write(top50)
    f.write(top100)
    f.write(top150)
    f.write(top200)
    f.write(wheeloftime)
    f.close()

    return


def main():
    # f = open("total_data.txt", "w+")
    # f.write(all_data)
    # f.close()

    top_250_data = get_data()
    print(top_250_data)

    top50_data = get_50th_tv_show_data(top_250_data)
    print(top50_data)
    top100_data = get_100th_tv_show_data(top_250_data)
    print(top100_data)
    top150_data = get_top_150_tv_show_data(top_250_data)
    print(top150_data)
    top200_data = get_top_200_tv_show_data(top_250_data)
    print(top200_data)

    wheel_of_time_data = get_tv_show_data(get_tv_show_title_id("the wheel of time 2021"))  # complete function
    print(wheel_of_time_data)

    print_to_file(json.dumps(top50_data), json.dumps(top100_data), json.dumps(top150_data)\
                  , json.dumps(top200_data), json.dumps(wheel_of_time_data))


if __name__ == '__main__':
    main()
