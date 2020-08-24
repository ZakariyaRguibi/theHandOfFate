#a simple io lib to help me get shits done
import json

#get dungeon master
def getDM():
        with open('dm.json') as f:
            data = json.load(f)
            return data

#set dungeon master
def setDM(dm):
        with open('dm.json', 'w') as json_file:
            json.dump(dm, json_file)