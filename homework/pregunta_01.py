# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


import os
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv('./files/input/shipping-data.csv', index_col=0)
    return df

def create_graph_for_warehouse_block(df):
    plt.figure()
    df = df.copy()
    counts = df.Warehouse_block.value_counts()
    counts.plot.bar(
        xlabel='Warehouse block',
        ylabel='Record Count'
    )

    plt.title('Shipping per Warehouse')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('./docs/shipping_per_warehouse.png')

def create_graph_for_mode_of_shipment(df):
    plt.figure()
    df = df.copy()
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        ylabel='',
        wedgeprops={'width': 0.35}
    )

    plt.title('Mode of Shipment')
    plt.savefig('./docs/mode_of_shipment.png')

def create_graph_for_customer_rating(df):
    plt.figure()
    df = df.copy()
    df = df[['Mode_of_Shipment', 'Customer_rating']].groupby('Mode_of_Shipment').describe()
    df.columns = df.columns.droplevel()

    plt.barh(
        y=df.index,
        width=df['max'] - 1,
        height=0.9,
        left=df['min'] - 1,
        color='lightgray',
        alpha=0.8
    )

    colors = ['tab:green' if value >= 3.0 else 'tab:orange' for value in df['mean'].values]
    
    plt.barh(
        y=df.index,
        width=df['mean'] - 1,
        height=0.5,
        left=df['min'] - 1,
        color=colors
    )

    plt.title('Average Customer Rating')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_color('gray')
    plt.gca().spines['bottom'].set_color('gray')
    plt.savefig('./docs/average_customer_rating.png')

def create_graph_for_weight_in_gms(df):
    plt.figure()
    df = df.copy()
    df.Weight_in_gms.plot.hist(
        color='tab:orange',
        edgecolor='white'
    )

    plt.title('Shipped Weight Distribution')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('./docs/weight_distribution.png')

def create_html():
    with open('./docs/index.html', 'w') as index:
        index.write('<!DOCTYPE html>\
<html lang="en">\n\
<body>\n\
    <h1>Shipping Dashboard Example</h1>\n\
    <div style="width:45%;float:left">\n\
        <img src="shipping_per_warehouse.png" alt="Fig 1">\n\
        <img src="mode_of_shipment.png" alt="Fig 2">\n\
    </div>\n\
    <div style="width:45%;float:left">\n\
        <img src="average_customer_rating.png" alt="Fig 3">\n\
        <img src="weight_distribution.png" alt="Fig 4">\n\
    </div>\n\
</body>\n\
</html>'
        )

    
def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    # Crear directorio docs si no existe
    if not os.path.exists('./docs'):
        os.makedirs('./docs')
    
    
    # Cargar datos
    df = load_data()
    create_graph_for_warehouse_block(df)
    create_graph_for_mode_of_shipment(df)
    create_graph_for_customer_rating(df)
    create_graph_for_weight_in_gms(df)
    create_html()

pregunta_01()