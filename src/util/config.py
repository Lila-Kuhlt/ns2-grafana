import json

config_file = open("../config/config.json", "r")
config = json.load(config_file)
config_file.close()


def get():
    return config
