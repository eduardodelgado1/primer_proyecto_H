from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carga los datos del dataframe
df = pd.read_csv('C:\\Users\\eduar\\OneDrive\\Documentos\\Henry\\primer proyecto individual\\proyecto cohrte 10\\archivo.csv', dtype={'columna_4': str}, low_memory=False)
#df = pd.read_csv('ruta_del_archivo.csv', dtype={'columna_4': str}, low_memory=False)


"""CANTIDAD DE PELICULAS POR PAIS EN UN AÑO"""
#Ruta de la API para obtener la cantidad de películas producidas por un país en un año
@app.route('/movies', methods=['GET'])
def get_country():
    year = request.args.get('year')
    country = request.args.get('country')

    # Filtra el dataframe por año y país
    filtered_df = df[(df['release_date'].dt.year == int(year)) & (df['production_countries_name'].str.contains(country))]

    # Obtiene el número de películas producidas
    count = filtered_df.shape[0]

    # Devuelve la respuesta en formato JSON
    return jsonify({'count': count})

"""----------------------------------------------------------------------------------------------------------"""
"""RECAUDACION POR PRODUCTORA Y POR AÑO"""

def get_company_revenue(company, year):
    # Filtra el dataframe por productora y año
    filtered_df = df[(df['production_company_name'] == company) & (df['release_date'].dt.year == int(year))]

    # Suma la columna de recaudación (revenue) filtrada
    total_revenue = filtered_df['revenue'].sum()

    # Devuelve el total de dólares recaudados como entero
    return int(total_revenue)

@app.route('/revenue')
def get_revenue():
    company = request.args.get('company')
    year = request.args.get('year')

    # Llama a la función get_company_revenue para obtener el resultado
    revenue = get_company_revenue(company, year)

    # Devuelve el resultado como respuesta en formato JSON
    return jsonify({'revenue': revenue})

"""-------------------------------------------------------------------------------------------------------------"""

"""CANTIDAD DE PELICULAS QUE SALIERON EN  DETERMINADO AÑO"""


def get_count_movies(year):
    # Filtra el dataframe por el año de estreno
    filtered_df = df[df['release_date'].dt.year == int(year)]

    # Obtiene la cantidad de películas
    count_movies = len(filtered_df)

    # Devuelve el número total de películas como entero
    return int(count_movies)

"""--------------------------------------------------------------------------------------------------------------"""
"""PELICULA CON MAYOR RETORNO EN DETERMINADO AÑO"""

def get_return(year):
    # Filtra el dataframe por el año de estreno
    filtered_df = df[df['release_date'].dt.year == int(year)]

    # Obtiene la película con el mayor retorno
    max_return_movie = filtered_df.loc[filtered_df['return'].idxmax(), 'title']

    # Devuelve el nombre de la película con mayor retorno
    return max_return_movie

"""---------------------------------------------------------------------------------------------------------------"""
"""PELICULA CON MENOR PRESUPUESTO EN DETERMINADO AÑO"""


def get_min_budget(year):
    # Filtra el dataframe por el año de estreno
    filtered_df = df[df['release_date'].dt.year == int(year)]

    # Obtiene la película con el menor presupuesto
    min_budget_movie = filtered_df.loc[filtered_df['budget'].idxmin()]

    # Crea un diccionario con los datos de la película
    movie_info = {
        'title': min_budget_movie['title'],
        'year': min_budget_movie['release_date'].year,
        'budget': min_budget_movie['budget']
    }

    # Devuelve el diccionario con la información de la película
    return movie_info

"""-------------------------------------------------------------------------------------------------------"""
""" LISTA CON LAS 5 FRANQUICIAS QUE MAS RECAUDARON"""


def get_collection_revenue():
    # Agrupa el dataframe por la columna 'name_belongs_to_collection' y suma la columna 'revenue'
    collection_revenue = df.groupby('name_belongs_to_collection')['revenue'].sum()

    # Obtiene las 5 franquicias con mayor recaudación
    top_5_collections = collection_revenue.nlargest(5).index.tolist()

    # Devuelve la lista de las 5 franquicias más recaudadoras
    return top_5_collections

"""----------------------------------------------------------------------------------------------------"""

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='localhost', port=8000)
    
"""if __name__ == '__main__':
    app.run()"""