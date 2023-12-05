import json

class Event:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

class Event_handler:
    def __init__(self):
        self.arr_e = []

    def add_elem(self, elem):
        self.arr_e.append(elem)

    def delete_elems(self):
        self.arr_e.clear()

    def save_to_file(self, filename):
        dict = {}
        k = 0
        with open(filename, 'w') as f:
            for event in self.arr_e:
                dict1 = {}
                dict1["name"] = event.name
                dict1["x"] = event.x
                dict1["y"] = event.y

                dict[k] = dict1
                k = k + 1

            json.dump(dict, f)



    def restore_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
            for event in data.keys():
                event = Event(data[event]["x"], data[event]["y"], data[event]["name"])
                self.add_elem(event)

    def print_events(self):

        for event in self.arr_e:
            print(f"({event.name}, {event.x}, {event.y})\n")








