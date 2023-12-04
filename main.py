from event_handler import Event
from event_handler import Event_handler

if __name__ == '__main__':
    e_1 = Event(10.345,2.774)
    e_2 = Event(1,4.47)
    e_3 = Event(5.2478, 6.4840)
    e_4 = Event(7.358, 8.353)

    arr_e = Event_handler()
    arr_e.add_elem(e_1)
    arr_e.add_elem(e_2)
    arr_e.add_elem(e_3)
    arr_e.add_elem(e_4)

    arr_e.save_to_file("coordinates.txt")

    arr_e_1 = Event_handler()
    arr_e_1.restore_from_file("coordinates.txt")
    arr_e_1.print_events()