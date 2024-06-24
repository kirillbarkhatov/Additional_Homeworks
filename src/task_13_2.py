import json
from datetime import datetime as dt

events = [
  {
    "name": "Event 1",
    "start_date": "2022-01-01",
    "end_date": "2022-01-05"
  },
  {
    "name": "Event 2",
    "start_date": "2022-02-15",
    "end_date": "2022-02-18"
  },
  {
    "name": "Event 3",
    "start_date": "2022-03-10",
    "end_date": "2022-03-20"
  }
]


def get_duration_events(events):
    result = [(dt.strptime(event["end_date"], "%Y-%m-%d") - dt.strptime(event["start_date"], "%Y-%m-%d")).days + 1 for event in events]
    return result


if __name__ == '__main__':
    print(get_duration_events(events))