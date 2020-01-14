from ast import literal_eval

import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np


def parse_log_data():
    dates = []
    exec_times = []
    inputs = []
    for line in open("logs.log", "r"):
        info = line.split(" - ")
        dates.append(info[0])
        expr = literal_eval(info[1])
        exec_times.append(expr[0])
        inputs.append(expr[1])
    indexes = tuple(np.arange(1, len(dates) + 1))
    return indexes, dates, exec_times, inputs


def plot_graph(indexes, exec_times):
    plt.figure(1)
    y_pos = np.arange(len(indexes))
    bars = plt.bar(y_pos, exec_times, align="center", alpha=0.5)
    autolabel(bars)
    plt.xticks(y_pos, indexes)
    plt.ylabel("Time (s)")
    plt.title("Runtime statistics")


def autolabel(bars):
    """
    Attach a text label above each bar displaying its height
    """
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 "% 6.3f" % height,
                 ha="center", va="bottom")


if __name__ == "__main__":
    (indexes, dates, exec_times, inputs) = parse_log_data()
    plot_graph(indexes, exec_times)
    plt.show()
