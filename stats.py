import matplotlib.pyplot as plt; 


def parse_log_data():
    generations = []
    fitnesses = []
    for line in open("logs.log", "r"):
        info = line.split(" ")
        generations.append(info[0])
        fitnesses.append(info[1])
    return generations, fitnesses

if __name__ == "__main__":
    (generations, fitnesses) = parse_log_data()
    plt.plot(generations, fitnesses)
    plt.ylabel("Fitness")
    plt.title("Runtime statistics")
    plt.show()
