import matplotlib.pyplot as plt; 
import numpy as np


def parse_log_data():
    generations = []
    distances = []
    inputs = []
    for line in open("logs.log", "r"):
        info = line.split(" - ")
        generations.append(info[0])
        distances.append(expr[0])
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
    (generations, distances) = parse_log_data()
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) (gener dist )
    plot_graph(indexes, distances)
    plt.show()
