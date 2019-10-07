import argparse
import math
import random

class City():
    def __init__(self, index, x_coord, y_coord):
        self.index = index
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __repr__(self):
        return "[" + str(self.x_coord) + ", " + str(self.y_coord) + "]"

    def get_distance_to(self, other):
        dx = (other.x_coord - self.x_coord) ** 2
        dy = (other.y_coord - self.y_coord) ** 2
        return math.sqrt(dx + dy)

class Instance():
    def __init__(self, route):
        self.route = route
        self.route_distance = self.get_route_distance()
        self.fitness = self.get_fitness()

    def get_route_distance(self):
        distance = 0
        for i in range(len(self.route)):
            src = self.route[i]
            dest = self.route[i + 1] if i + 1 < len(self.route) else self.route[0]
            distance += src.get_distance_to(dest)
        return distance

    def get_fitness(self):
        return 1 / self.route_distance

class GeneticAlgorithm():
    def __init__(self, population_size, elitism, max_generations, crossover_rate, mutation_rate, cities_list):
        self.population_size = population_size
        self.elitism = elitism
        self.max_generations = max_generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.cities_list = cities_list

    def generate_instance(self):
        route = random.sample(self.cities_list, len(self.cities_list))
        instance = Instance(route)
        return instance

    def create_initial_population(self):
        initial_population = []
        for _ in range(self.population_size):
            initial_population.append(self.generate_instance())
        return initial_population

    def crossover(self, p1, p2): # proposing good crossover method https://www.hindawi.com/journals/cin/2017/7430125/
        #implement simple crossover then try to enhance it 
        #ordered crossover 
        li = 0
        hi = 0
        while hi <= li:
            li = int(random.random() * len(p1)) 
            hi = int(random.random() * len(p1))
        chunk = p1[li:hi] 
        child = []
        not_used_el_in_p2 = [el for el in p2 if el not in chunk]
        pointer = 0
        for _ in range(li):
            child.append(not_used_el_in_p2[pointer])
            pointer += 1
        child += chunk
        for _ in range(hi, len(p1)):
            child.append(not_used_el_in_p2[pointer])
            pointer += 1
        return child

    def mutation(self, instance):
        if random.random() < self.mutation_rate:
            i1, i2 = random.sample(range(len(self.cities_list)), 2)
            instance[i1], instance[i2] = instance[i2], instance[i1]

    def selection(self):
        pass

    def generate_path(self):
        # Step 1. Create an initial population of P chromosomes.

        # Step 2. Evaluate the fitness of each chromosome.

        # Step 3. Choose P/2 parents from the current population via proportional selection.

        # Step 4. Randomly select two parents to create offspring using crossover operator.

        # Step 5. Apply mutation operators for minor changes in the results.

        # Step 6. Repeat Steps  4 and 5 until all parents are selected and mated.

        # Step 7. Replace old population of chromosomes with new one.

        # Step 8. Evaluate the fitness of each chromosome in the new population.

        # Step 9. Terminate if the number of generations meets some upper bound; otherwise go to Step  3.
        return 0

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
            cities.append((line_contents[0], line_contents[1], line_contents[2]))
    f.close()
    return cities

def create_cities(coordinates_list):
    cities_list = []
    for coordinates in coordinates_list:
        cities_list.append(City(coordinates[0], coordinates[1], coordinates[2]))
    return cities_list

def main():
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

    gen_algo = GeneticAlgorithm(population_size, elitism, max_generations, crossover_rate, mutation_rate, cities_list)
    # distance = gen_algo.generate_path()
    # print(distance)

if __name__ == "__main__":
    main()