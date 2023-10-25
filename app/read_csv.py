import csv
from os import read
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')# delimiter sirve para que determine como estan separados los datos , : etc. reader es un interable que se puede llamar por lineas
    header = next(reader)
    population = []
    for row in reader:
      iterable = zip(header, row)
     
      country_dict = {key: value for key, value in iterable}
      
      population.append(country_dict)
    return population
if __name__ == '__main__':#lo ejecupa como un scrip
  population = read_csv('./app/population.csv')
  print(population[0])
 
  