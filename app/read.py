import csv

with open('./app/relatedEntities.csv','r') as file:
  reader = csv.reader(file, delimiter=',')
  header = next(reader)
  list = []
  for row in reader:
    itinerable = zip(header, row)
    dict = {key: value for key, value in itinerable}
    list.append(dict)
  lis=[]
  for x in list:
    if x not in lis:
      lis.append(x)

x=(filter(lambda x: x['Uovo'], lis))
print(x)