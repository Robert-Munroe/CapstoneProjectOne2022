import api_data


def test_250():
    top250shows = api_data.get_top_250_data()
    assert len(top250shows) == 250
