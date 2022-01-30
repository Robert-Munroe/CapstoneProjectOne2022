# Robert Munroe Senior Capstone Project 1

import requests


def get_data(url: str):

    final_url = f"{url}"
    response = requests.get(final_url)
    if response.status_code != 200:
        print(response.text)
        return []
    print(response.text)
    json_data = response.json()

    return json_data


def main():
    url = "https://imdb-api.com/en/API/Top250TVs/k_x2v878m2"
    print(get_data(url))


if __name__ == '__main__':
    main()
