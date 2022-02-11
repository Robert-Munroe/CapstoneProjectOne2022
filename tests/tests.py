import main
import sqlite3
import pytest


def test_250():
    top250shows = main.get_top_250_data()
    assert len(top250shows) == 250
