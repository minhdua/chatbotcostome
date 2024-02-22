from actions.utils import read_json_file

data = read_json_file('rasaserver/data/nlu.json')

if data is not None:
    print(data)