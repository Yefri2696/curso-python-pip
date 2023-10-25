import matplotlib.pyplot as plt

def generate_bar_char(name, labels, values):

  flig, ax = plt.subplots()#flig son las figuras y ax son las cordenadas
  ax.bar(labels, values)#tipo de grafico
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')#para que se organize
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [50, 300, 300]
  generate_pie_chart(labels, values)