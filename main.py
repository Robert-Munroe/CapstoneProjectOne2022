# Robert Munroe Senior Capstone Project 1

import requests
import secrets
import json


def out_of_dictionary(data, qualifier: str):
    new_data = data.get(qualifier)
    return new_data


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


def get_tv_show_data(title_code: str):
    url = 'https://imdb-api.com/en/API/UserRatings/' + secrets.api_key + "/" + title_code
    results = requests.get(url)
    if results.status_code != 200:
        print("hmm")
        return
    data = results.json()
    return data


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


def main():
    # f = open("total_data.txt", "w+")
    # top_250_data = get_data()
    # f.write(all_data)
    # f.close()
    # list_of_data = out_of_dictionary(top_250_data, 'items')
    # print(top_250_data)
    # print(get_tv_show_data(get_tv_show_title_id("the wheel of time 2021"))) complete function


if __name__ == '__main__':
    main()
