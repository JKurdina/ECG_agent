from event_handler import Event
from event_handler import Event_handler

if __name__ == '__main__':
    events_file = "D:\\PycharmProjects\\ECG_agent\\events.json"  # file with dataset

    e_1 = Event(1,2.774, "name1")
    e_2 = Event(1,4.47, "name2")
    e_3 = Event(5.2478, 6.4840, "name3")
    e_4 = Event(7.358, 8.353, "name4")

    arr_e = Event_handler()
    arr_e.add_elem(e_1)
    arr_e.add_elem(e_2)
    arr_e.add_elem(e_3)
    arr_e.add_elem(e_4)

    arr_e.save_to_file(events_file)

    arr_e_1 = Event_handler()
    arr_e_1.restore_from_file(events_file)
    arr_e_1.print_events()