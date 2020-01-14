from ast import literal_eval

import matplotlib.pyplot as plt; 
plt.rcdefaults()
import numpy as np


def parse_log_data():
    generations = []
    distances = []
    inputs = []
    for line in open("logs.log", "r"):
        info = line.split(" - ")
        generations.append(info[0])
        expr = literal_eval(info[1])
        distances.append(expr[0])
        inputs.append(expr[1])
    indexes = tuple(np.arange(1, len(generations) + 1))
    return indexes, generations, distances, inputs


def plot_graph(indexes, distances):
    plt.figure(1)
    y_pos = np.arange(len(indexes))
    bars = plt.bar(y_pos, distances, align="center", alpha=0.5)
    autolabel(bars)
    plt.xticks(y_pos, indexes)
    plt.ylabel("Distance")
    plt.title("Runtime statistics")


if __name__ == "__main__":
    (indexes, generations, distances, inputs) = parse_log_data()
    plot_graph(indexes, distances)
    plt.show()
