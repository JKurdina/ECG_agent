import json
import matplotlib.pyplot as plt

import savers
from ecgClicker import ECGclicker, Event_handler
from learning_case1 import Learning_case1 as case1


def load_data():
    
    dataset_path = "D:\\5 семестр\\Курсовая\\ecg_data_200.json"


    with open(dataset_path, 'r') as f:
    
        data = json.load(f)
    
        return data
    
def get_signal_ecg(i):
    
    data = load_data()
    
    leads = data[list(data.keys())[i]]['Leads']
        
    signal = leads["i"]['Signal']
             
    return signal


def save_etalon():
    
    signal = get_signal_ecg(4)
    savers.save_etalon_signal(signal, "etalon_signal.json")

    
     

if __name__ == '__main__':
    
    # ------------------------click etalon------------------
    # fig, ax = plt.subplots();
    # path_events_file = "D:\\5 семестр\\Курсовая\\ECG_agent\\events.json" 
    # path_etalon_file = "D:\\5 семестр\\Курсовая\\ECG_agent\\etalon_signal.json"

    # events = ECGclicker(fig, ax, path_etalon_file, path_events_file)
    
    # events.draw_ecg_click()
    
    case = case1()
    
    case.draw()
    # ----------------------------------------------------
    
    # arr_e_1 = Event_handler()
    # arr_e_1.restore_from_file(path_events_file)
    # arr_e_1.print_events()
    
    # ---------------------------------------------------
    
    # events_file = "D:\\PycharmProjects\\ECG_agent\\events.json"  # file with dataset

    # save_etalon()

    

    # e_1 = Event(1,2.774, "name1")
    # e_2 = Event(1,4.47, "name2")
    # e_3 = Event(5.2478, 6.4840, "name3")
    # e_4 = Event(7.358, 8.353, "name4")

    # arr_e = Event_handler()
    # arr_e.add_elem(e_1)
    # arr_e.add_elem(e_2)
    # arr_e.add_elem(e_3)
    # arr_e.add_elem(e_4)

    # arr_e.save_to_file(events_file)

    


    # # signal = [50, 51, 53, 54, 55, 56]
    # # savers.save_etalon_signal(signal, "etalon_signal.json")




    # signals_pos = []
    # signal_pos_1 = [1, 2, 3]
    # signal_pos_2 = [4, 5, 6]
    # signal_pos_3 = [7, 8, 9]
    # signals_pos.append(signal_pos_1)
    # signals_pos.append(signal_pos_2)
    # signals_pos.append(signal_pos_3)

    # signals_neg = []
    # signal_neg_1 = [4, 5, 6]
    # signal_neg_2 = [4, 5, 6]
    # signal_neg_3 = [4, 5, 6]
    # signals_neg.append(signal_neg_1)
    # signals_neg.append(signal_neg_2)
    # signals_neg.append(signal_neg_3)

    # savers.save_signals(signals_pos, signals_neg, "signals.json")

    # signals_pos1 = savers.read_signals_pos("signals.json")
    # signals_neg1 = savers.read_signals_neg("signals.json")

    # case = case1()
    # etalon = case.get_etalon_signal()
    # pos = case.get_positives()
    # neg = case.get_negatives()
    # events = case.get_etalons_events_set()

