# libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mpld3

df = pd.read_csv('datos.csv')
df.dropna(subset=['PESO'], inplace=True)

mayor = df[df.PESO > 50]
medio = df[(df.PESO > 20) & (df.PESO < 50)]
todos = df[df.PESO > 10]

nueva = mayor

x = nueva['PESO']
y = nueva['CANTIDAD']
z = nueva['CANTIDAD']

fig, ax = plt.subplots(subplot_kw=dict(adjustable='datalim'), figsize=(18, 8))
# YlOrRd RdBu RdGy
scatter = ax.scatter(x, y, s=z * 5, c=z, cmap="gist_heat", alpha=0.7, edgecolors="grey", linewidth=0.5)
ax.set_xlim((40, 410))
ax.set_ylim((-1, 1150))
ax.set_title('Peso de las piezas vs Cantidad total - El tamaño de las burbujas corresponde a la cantidad de piezas en '
             'total', size=16)
ax.set_xlabel('Peso [kg]', size=30)
ax.set_ylabel('Cantidad', size=30)

labels = []
for i in range(len(nueva.PESO)):
    label = nueva[i:i + 1].T
    label.columns = [nueva.COD[i:i + 1]]
    # append it to the list. str() remove the leading 'u' in the unicode output of .to_html()
    labels.append(str(label.to_html()))

print(label)
# Define the css
css = """
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
"""
# Define the html tooltip associated to the scatter plot, pass the labels and the css
tooltip = mpld3.plugins.PointHTMLTooltip(scatter, labels, voffset=-20, hoffset=20, css=css)

# Connect it to the figure
mpld3.plugins.connect(fig, tooltip)

mpld3.save_html(fig, 'chart-cantidad-peso.html')

# COD,DESC,CANTIDAD,COMPRO,CLIENTES,MESES,PESO,ANCHO,LARGO,ALTO,CD
