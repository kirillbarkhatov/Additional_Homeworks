import json
import os


def avg_temp_in_file(file_path, city):
    with open(file_path, "r") as file:
        weather = json.load(file)
    avg_temp = round(sum([t for t in weather[city].values()]) / len(weather[city]), 2)
    print(avg_temp)
    data = {city: {"Average temperature": avg_temp}}
    project_dir = os.path.dirname(os.getcwd())
    data_dir = os.path.join(project_dir, "data")
    name_file_path = os.path.join(data_dir, f"avg_weather_{city}.json")
    with open(name_file_path, "w") as new_file:
        json.dump(data, new_file, indent=4)







if __name__ in "__main__":
    project_dir = os.path.dirname(os.getcwd())
    data_dir = os.path.join(project_dir, "data")
    name_file_path = os.path.join(data_dir, "weather.json")
    city = input()
    avg_temp_in_file(name_file_path, city)