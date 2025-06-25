import os
import re
import yaml
import json

from src.nikhil.medha_data.config.settings import Settings


class DirectoryProcessor:
    def __init__(self, config_path: str):
        self.config = self._load_config(config_path)
        self.directory_path = os.path.abspath(self.config.get('directory_to_scan', ''))
        self.output_file_path = self.config.get('output_file_path')
        self.content_json_path = os.path.join(self.directory_path, 'content.json')

    def _load_config(self, path):
        try:
            with open(path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file '{path}' not found.")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML configuration: {e}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error loading config: {e}")

    def scan_directory(self):
        """Scans the directory and stores all filenames (excluding content.json) into content.json."""
        if not os.path.isdir(self.directory_path):
            raise NotADirectoryError(f"Directory '{self.directory_path}' does not exist.")
        print(f"Scanning directory: {self.directory_path}")

        file_list = [
            f for f in os.listdir(self.directory_path)
            if os.path.isfile(os.path.join(self.directory_path, f)) and f != 'content.json'
        ]

        with open(self.content_json_path, 'w') as f:
            json.dump(file_list, f, indent=4)

        print(f"Saved {len(file_list)} files to '{self.content_json_path}'")
        return file_list

    def load_content_json(self):
        """Loads the content.json file."""
        if not os.path.exists(self.content_json_path):
            raise FileNotFoundError(f"'{self.content_json_path}' does not exist.")

        with open(self.content_json_path, 'r') as f:
            try:
                data = json.load(f)
                print(f"Loaded {len(data)} entries from '{self.content_json_path}'")
                return data
            except json.JSONDecodeError:
                raise ValueError(f"Invalid JSON format in '{self.content_json_path}'")

    @staticmethod
    def _natural_keys(text):
        def convert(segment):
            return int(segment) if segment.isdigit() else segment.lower()
        return [convert(c) for c in re.split(r'([0-9]+)', text)]

    def process_filenames(self, filenames):
        """Removes file extensions and sorts filenames naturally, then writes to topic.json."""
        if not isinstance(filenames, list):
            raise TypeError("Input must be a list of filenames.")

        processed = [os.path.splitext(name)[0] for name in filenames]
        processed.sort(key=self._natural_keys)

        with open(self.output_file_path, 'w') as f:
            json.dump(processed, f, indent=4)

        print(f"Processed and saved {len(processed)} sorted entries to '{self.output_file_path}'")
        return processed

    def create_topic_directories_with_json(self, topic_list):
        if not os.path.isdir(self.directory_path):
            raise NotADirectoryError(f"Base directory '{self.directory_path}' does not exist.")

        if not isinstance(topic_list, list):
            raise TypeError("Provided topic_list must be a list of strings.")

        for topic in topic_list:
            topic_dir = os.path.join(self.directory_path, topic)
            os.makedirs(topic_dir, exist_ok=True)

            content_json_path = os.path.join(topic_dir, 'content.json')
            if not os.path.exists(content_json_path):
                with open(content_json_path, 'w') as f:
                    json.dump([], f, indent=4)

        print(f"Created {len(topic_list)} topic directories with empty content.json files.")



if __name__ == "__main__":
    settings = Settings()
    processor = DirectoryProcessor(settings.INPUT_CONFIG_PATH)

    # Step 1: Scan directory and generate content.json
    #filenames = processor.scan_directory()

    # Step 2: Process content.json and generate topic.json
    #processor.process_filenames(filenames)

    content_json_path = r"E:\Python\medha_data\data\vnit\s1\DataTransformation\endterm\topic.json"
    with open(content_json_path, 'r') as f:
        data = json.load(f)

    # Step 3: Create folders for each topic with an empty content.json inside
    processor.create_topic_directories_with_json(data)
