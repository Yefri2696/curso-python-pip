import utils# puedes crear tus propio mudulos y importarlos
import read_csv
import charts

def rund():
  data = read_csv.read_csv('population.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  name = 'South America'

  countries = list(map(lambda x: x ['Country/Territory'], data))
  percentage = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(name, countries, percentage)

  country = input ('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_char(country['Country/Territory'], labels, values)
  
  
  print(result)

if __name__ == '__main__':#dice que si es ejecutado desde la terminar use el metodo run y si es ejecutado desde otro archivo no se ejecutara, sirve para correr de forma directa o en otro archivo
 rund()
 '''


def run():
  name = 'South America'
  data = read_csv.read_csv('population.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  percentage = list(map(lambda x: x['World Population Percentage'], data))
  territory = list(map(lambda x: x['Country/Territory'], data))
  charts.generate_pie_chart(name, territory, percentage)


if __name__ == '__main__':
  run()
 
  
def ip():
  population = read_csv.read_csv('./app/population.csv')
    
  data = list(map(lambda item: item['Country/Territory'], population))
  sin_repetir = []
  for elemento in data:
    if elemento not in sin_repetir:
        sin_repetir.append(elemento)
  print(sin_repetir)
  
ip()
  
'''