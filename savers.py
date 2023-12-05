import json
def save_etalon_signal(signal, filename):
    with open(filename, 'w') as f:
        json.dump(signal, f)

def read_etalon_signal(filename):
    with open(filename, 'r') as f:
        signal = json.load(f)
    return signal

def save_signals(signals_pos, signals_neg, filename):
    dict = {}
    dict["Positives_signals"] = signals_pos
    dict["Negatives_signals"] = signals_neg
    with open(filename, 'w') as f:
        json.dump(dict, f)

def read_signals_pos(filename):
    signals_pos = []
    with open(filename, 'r') as f:
        signals = json.load(f)
        signals_pos = signals["Positives_signals"]
    return signals_pos

def read_signals_neg(filename):
    signals_neg = []
    with open(filename, 'r') as f:
        signals = json.load(f)
        signals_neg = signals["Negatives_signals"]
    return signals_neg