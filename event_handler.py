
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
        f = open(filename, 'w')

        for event in self.arr_e:
            f.write(f"({event.x}, {event.y})\n")

        f.close()

    def restore_from_file(self, filename):
        f = open(filename)

        for line in f:
            x = ''
            y = ''
            flag = True
            for l in line:

                if l == "(":
                    pass
                elif l == ")":
                    flag = True
                elif l == ",":
                    flag = False
                elif l in "0123456789.-":
                    if flag:
                        x = x + l
                    else:
                        y = y + l
                else:
                    pass

            e = Event(x, y)
            self.add_elem(e)

        f.close()

    def print_events(self):

        for event in self.arr_e:
            print(f"({event.x}, {event.y})\n")







