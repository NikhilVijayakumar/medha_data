import os
import yaml
import json
import argparse

from src.nikhil.medha_data.config.settings import Settings


def process_directory(config_file_path):
    try:
        with open(config_file_path, 'r') as file:
            config = yaml.safe_load(file)

        directory_path = config.get('directory_to_scan')
        if not directory_path:
            print("Error: 'directory_to_scan' not found in the YAML configuration.")
            return

        directory_path = os.path.abspath(directory_path)

        if not os.path.isdir(directory_path):
            print(f"Error: Directory '{directory_path}' does not exist.")
            return

        print(f"Scanning directory: {directory_path}")

        content_json_path = os.path.join(directory_path, 'content.json')

        file_list = []
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isfile(item_path) and item != 'content.json':
                file_list.append(item)



        with open(content_json_path, 'w') as json_file:
            json.dump(file_list, json_file, indent=4)

        print(f"Successfully saved file list to '{content_json_path}'")

    except FileNotFoundError:
        print(f"Error: Configuration file '{config_file_path}' not found.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML configuration: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    settings = Settings()
    process_directory(settings.INPUT_CONFIG_PATH)
