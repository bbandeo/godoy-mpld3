# libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mpld3

df = pd.read_csv('datos.csv')
df.dropna(subset=['PESO'], inplace=True)
df = df.drop(columns=['DESC','ANCHO','LARGO','ALTO'])

df = df.drop(df[df['PESO']>30].index)
df = df.drop(df[df['PESO']<3].index)
df = df.drop(df[df['CANTIDAD']>5000].index)

x = df['CANTIDAD']
y = df['PESO']
z = df['MESES']


fig, ax = plt.subplots(subplot_kw=dict(adjustable='datalim'), figsize=(18, 8))


fig, ax = plt.subplots(subplot_kw=dict(adjustable='datalim'), figsize=(18, 8))
# YlOrRd RdBu RdGy
scatter = ax.scatter(x, y, s=z * 5, c=z, cmap="gist_heat", alpha=0.7, edgecolors="grey", linewidth=0.5)
ax.set_xlim((-1 , 1300))
ax.set_ylim((-1, 35))
ax.set_title('El color y tamaño de las burbujas corresponde a la cantidad de meses en las que el producto tuvo rotación '
             , size=16)
ax.set_xlabel('Cantidad distribuida en 36 meses', size=30)
ax.set_ylabel('Peso [kg]', size=30)

labels = []
for i in range(len(df.PESO)):
    label = df[i:i + 1].T
    label.columns = [df.COD[i:i + 1]]
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
  font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  border: 1px solid black;
  text-align: right;
}
"""
# Define the html tooltip associated to the scatter plot, pass the labels and the css
tooltip = mpld3.plugins.PointHTMLTooltip(scatter, labels, voffset=-20, hoffset=20, css=css)

# Connect it to the figure
mpld3.plugins.connect(fig, tooltip)

mpld3.save_html(fig, 'cantidad-peso.html')

# COD,DESC,CANTIDAD,COMPRO,CLIENTES,MESES,PESO,ANCHO,LARGO,ALTO,CD
