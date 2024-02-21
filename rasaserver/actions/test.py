import json

def read_json_file(file_path):
    """Reads a JSON file and returns the parsed data.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The parsed JSON data, or None if an error occurs.

    Raises:
        FileNotFoundError: If the file is not found.
        json.JSONDecodeError: If the JSON data is invalid.
    """

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(f"Error: File not found: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON data: {e}")
        return None

data = read_json_file('rasaserver/data/nlu.json')

if data is not None:
    print(data)