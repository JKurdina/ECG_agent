import json
import matplotlib.pyplot as plt
from easygui import enterbox
from matplotlib.patches import Ellipse

import savers
from print_ecg import draw_ECG


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
            
class ECGclicker:
    
    def __init__(self, fig, ax, path_etalon_file, path_events_file):
        
        self.arr_events  = Event_handler()
        self.signal      = savers.read_etalon_signal(path_etalon_file)
        
        self.path_events_file = path_events_file
        
        self.ax          = ax
        self.fig         = fig
        
        self.cid         = 0
        
    
    def save_arr_events(self):
        
        self.arr_events.save_to_file(self.path_events_file)
    
    def on_close(self, event):
        
        self.fig.canvas.mpl_disconnect(self.cid)
        
        self.save_arr_events()
        
        
    def onclick(self, event):
        
        text = "Enter the data"
        title = "ECG click"

        output = enterbox(text, title)
    
        x = event.xdata
        y = event.ydata
        
        e = Event(x, y, output)
        
        self.arr_events.add_elem(e)
        
        # self.coords.append((x, y))
        
        
        ellipse = Ellipse((x, y), width=10, height=30, edgecolor='r', fc='None', lw=1)
        
        self.ax.add_patch(ellipse)
        
        plt.plot(x,y,'ro')
        
        
        
            
    def draw_ecg_click(self):
        
        
        draw_ECG(self.ax, self.signal[0:500])
        
        plt.show()
         
        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        
        self.cid = cid
        
        self.fig.canvas.mpl_connect('close_event', self.on_close)
        
       
        
        

