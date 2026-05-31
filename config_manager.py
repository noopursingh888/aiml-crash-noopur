# This program demonstrates reading and writing
# JSON files using the json module


import json


def save_config(data: dict, filename: str):

    """
    Saves a dictionary into a JSON file.
    """

    with open(filename, "w") as file:

        json.dump(data, file, indent=4)


def load_config(filename: str) -> dict:

    """
    Reads and returns data from a JSON file.
    """

    with open(filename, "r") as file:

        return json.load(file)


def update_config(filename: str, key: str, value):

    """
    Updates one key in the JSON file
    and saves the updated data.
    """

    config = load_config(filename)

    config[key] = value

    save_config(config, filename)


config_data = {
    "model": "GPT",
    "learning_rate": 0.01,
    "epochs": 10
}


save_config(config_data, "config.json")


loaded_data = load_config("config.json")

print("Original Config:")
print(loaded_data)


update_config("config.json", "epochs", 20)


updated_data = load_config("config.json")

print("\nUpdated Config:")
print(updated_data)


# json.dump() writes JSON directly into a file.
# json.dumps() converts Python data into a JSON string.