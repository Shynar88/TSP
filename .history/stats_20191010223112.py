import matplotlib.pyplot as plt; 
import numpy as np


def parse_log_data():
    generations = []
    distances = []
    for line in open("logs.log", "r"):
        info = line.split(" ")
        generations.append(info[0])
        distances.append(info[1])
    return generations, distances

if __name__ == "__main__":
    (generations, distances) = parse_log_data()
    distances.reverse()
    plt.plot(generations, distances)
    plt.ylabel("Distance")
    plt.title("Runtime statistics")
    plt.show()
