En este proyecto, me correspondió  analizar un dataset  en donde se  especifican ciertas caracteristicas de peliculas y resolver lo siguiente:
+ Algunos campos, como **`belongs_to_collection`**, **`production_companies`** y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder  y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.

+ Los valores nulos de los campos **`revenue`**, **`budget`** deben ser rellenados por el número **`0`**.
  
+ Los valores nulos del campo **`release date`** deben eliminarse.

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**, además deberán crear la columna **`release_year`** donde extraerán el año de la fecha de estreno.

+ Crear la columna con el retorno de inversión, llamada **`return`** con los campos **`revenue`** y **`budget`**, dividiendo estas dos últimas **`revenue / budget`**, cuando no hay datos disponibles para calcularlo, deberá tomar el valor **`0`**.

+ Eliminar las columnas que no serán utilizadas, **`video`**,**`imdb_id`**,**`adult`**,**`original_title`**,**`vote_count`**,**`poster_path`** y **`homepage`**.

<br/>

**`Desarrollo API`**:   Propones disponibilizar los datos de la empresa usando el framework ***FastAPI***. Las consultas que propones son las siguientes:

Deben crear 6 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).
+ Cantidad de películas producidas por un determinado país en determinado año. La función debe llamarse get_country(year, country) y debe devolver sólo número de películas producidas por dicho país en dicho año.
+ Recaudacion por productora y por año. La función debe llamarse get_company_revenue(company, year) y debe devolver un int, con el total de dólares recaudados ese año por esa productora.
+ Cantidad de películas que salieron en determinado año. La función debe llamarse get_count_movies(year) y debe devolver un int, con el número total de películas que salieron ese año.
+ Película con mayor retorno en determinado año. La función debe llamarse get_return(title, year) y debe devolver sólo el string con el nombre de la película con mayor retorno de inversión en ese año.
+ Película con el menor presupuesto en determinado año. La función debe llamarse get_min_budget(year) deberia devolver el string con el nombre de la película, el año de estreno y el presupuesto, en un diccionario con las llaves llamadas 'title', 'year', 'budget' y cada una con su valor correspondiente.
+ Lista con las 5 franquicias, colleciones o series de películas que más recaudaron históricamente. La función se llamará get_collection_revenue() y debería devolver una lista de longitud 5 que contenga el nombre en string de las 5 franquicias que más recaudaron históricamente.
+ Todo  esto a travez de una API
