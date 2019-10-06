import argparse

class City():
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __repr__(self):
        return "{" + str(self.x_coord) + ", " + str(self.y_coord) + "}"

class GeneticAlgorithm():
    def __init__(self, population_size):
        self.population_size = population_size

    def crossover(self):
        pass

    def mutation(self):
        pass

# parses command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=str, default="a280.tsp", help="path to the input file")
    parser.add_argument('-s', type=int, default=50, help="population size")
    parser.add_argument('-e', type=int, default=1, help="elitism")
    parser.add_argument('-mg', type=int, default=50, help="max generations")
    parser.add_argument('-cr', type=float, default=0.3, help="crossover rate")
    parser.add_argument('-mr', type=float, default=0.1, help="mutation rate")
    args = parser.parse_args()
    return args.p, args.s, args.e, args.mg, args.cr, args.mr

# parses file, returns list of city coordinates(ex: [(x1, y1), ...])
def parse(file_path): #coordinates start from the 7th line, end with EOF
    cities = []
    f = open(file_path, "r")
    for _ in range(6):
        f.readline()
    for line in f:
        line_contents = line.split()
        if len(line_contents) == 3:
            cities.append((line_contents[1], line_contents[2]))
    f.close()
    return cities

def create_cities(coordinates_list):
    cities_list = []
    for coordinates in coordinates_list:
        cities_list.append(City(coordinates[0], coordinates[1]))
    return cities_list

if __name__ == "__main__":
    path, population_size, elitism, max_generations, crossover_rate, mutation_rate = parse_arguments()
    #delete prints
    print(path)
    print(population_size) 
    print(elitism) 
    print(max_generations) 
    print(crossover_rate) 
    print(mutation_rate)
    #####
    coordinates_list = parse(path)
    cities_list = create_cities(coordinates_list)

    # GeneticAlgorithm(population_size = 90)
