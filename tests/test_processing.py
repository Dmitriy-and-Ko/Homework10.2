import datetime
import pytest
from src.processing import filter_by_state

@pytest.mark.parametrize('user_list, user_state, expected', [
    ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}, {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}, {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}, {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], 'EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}, {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}, {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}, {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], 'CANCELED', [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}, {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]),
    ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}, {"id": 939719570,  "date": "2018-06-30T02:08:58.425572"}, {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}, {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], 'EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]),
    ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}, {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}, {"id": 594226727, "date": "2018-09-12T21:27:25.241689"}, {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], 'CANCELED', [{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]),
    ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}, {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}, {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"}, {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"}], 'CANCELED', []),
    ([], 'EXECUTED', []),
    ([], 'CANCELED', [])
])
def test_filter_by_state(user_list, user_state, expected):
    assert filter_by_state(user_list, user_state) == expected