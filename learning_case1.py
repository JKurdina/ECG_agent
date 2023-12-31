import savers
import ecgClicker
from print_ecg import draw_ECG
import matplotlib.pyplot as plt
from  html_logger import HtmlLogger

class Learning_case1:

    def __init__(self):
        
        self.etalon_signal = savers.read_etalon_signal("etalon_signal.json")
        self.events_set = ecgClicker.Event_handler()
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
        log = HtmlLogger("index")
        log.add_text("Etalon signal and Events")

        fig, ax = plt.subplots()
        draw_ECG(ax, self.get_etalon_signal()[0:500])
        log.add_fig(fig, "")

        fig, ax = plt.subplots()
        fig = self.get_etalons_events_set().get_fig()
        log.add_fig(fig, "end")


        log.add_line_big()
        log.add_text("Positives examples")
        signals_pos = self.get_positives()
        for signal in signals_pos:
            fig, ax = plt.subplots()
            draw_ECG(ax, signal[0:500])
            log.add_fig(fig, "end")
            log.add_line_little()

        log.add_line_big()
        log.add_text("Negatives examples")
        signals_neg = self.get_negatives()
        for signal in signals_neg:
            fig, ax = plt.subplots()
            draw_ECG(ax, signal[0:500])
            log.add_fig(fig, "end")
            log.add_line_little()


