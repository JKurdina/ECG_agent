import savers
from event_handler import Event_handler as event
from print_ecg import draw_ECG
import matplotlib.pyplot as plt
class Learning_case1:

    def __init__(self):
        self.etalon_signal = savers.read_etalon_signal("etalon_signal.json")
        self.events_set = event()
        self.events_set.restore_from_file("events.json")
        self.positives = savers.read_signals_pos("signals.json")
        self.negatives = savers.read_signals_neg("signals.json")
    def get_etalon_signal(self):
        return self.etalon_signal
    def get_etalons_events_set(self):
        return self.events_set
    def get_positives(self):
        return self.positives
    def get_negatives(self):
        return self.negatives
    def draw(self):
        fig, ax = plt.subplots()
        draw_ECG(ax, self.etalon_signal)
        plt.show()


