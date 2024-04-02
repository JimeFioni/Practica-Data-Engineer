# documentacion de Epam.py
Este codigo esta hecho por Martín Eluney Gómez Piñeiro y Jimena Fioni
para la pasantia de trabajo la Empresa Trabajo en Digital.

## Trabajo realizado
Se realizo un scrip de la pagina 'https://www.epam.com/careers/job-listings?country=Mexico', donde tuvimos que conectarnos a la pagina por medio de la API de la misma y realizar el scrapeo de esta usando la libreria de Python beutifulsoup4.

## Errores y observaciones 
+La pagina contaba con 105 ofertas de trabajo para la fecha y como su sistema de 'paginacion' constaba de un boton que si no se 'apretaba' bloqueba parte de la informacion, fue necesaria la utilizacion de la API, para sortear este problema, ya que con bs4 no es posible pedir realizar clicks en un boton.

+Las ofertas de trabajo no estaban bien delimitadas en cuanto a su separacion de categorias al momento de describirlas, todas sus separaciones contaban con el mismo nombre en cuanto a la clase de sus h3 que los separaban. por lo que debimos creear una funcion que tome el texto del h3 y lo use como clave, y el textyo dento der el li siguente, lo use como informacion de la clave.

## Pasos del Proyecto
 
1. Impotamos las librerias que utilizaria en el proyecto: 'requests', 'bs4', 'pandas', 'numpy', 're', 'deep_translator', 'nanoid' y 'slugify' 
2. Creamos una funcion que llamamos 'epam' que se encargaba de entrar a la pagina antes mencionada y extraer la url de todos los puestos de trabajo publicados
3. Creamos una funcion llamada 'remove_params' encargada de remover los parametros de la url despues del '?'.
4. Creamos 2 funcion que llamamos 'get_job_details_epam' que se encargo de scrapear todas las ofertas de trabajo y depositar su informacion en un dicc. Y 'link_trave', que se encargo de recorrer todos los links de las ofertas de trabajo y pasarlas por la funcion 'get_job_details_epam
5. LLevamos a cabo una normalizacion de los datos, eliminando simbolos que no queriamos, junto con partes de texto. Ademas renombramos la columna 'country' por 'city', ya que era mas acorde a su informacion
6. Creamos 4 listas llamadas 'skills', 'tools', 'aptitudes' y 'languages', proporcionadas por la empresa TeD(Trabajo en Digital), que serviran para buscar dentro de los textos de algunas columnas, las coincidencias que correspondan a cada lista.
7. Creamos 2 funciones para cada lista llamadas encontar_...(lista) y diccionario...(del 1 al 4) donde se buscan las coincidensias con la respectiva lista dentro de la columna req_text y se agrega esta coincidencia a undiccionario con el nombre de la lista.
8. Creamos una funcion llamada 'Encontrar skill' que agrega los diccionarios creeados previamente al dataframe en forma de columnas. Es decir que ahora hay 4 nuevas columnas con los nombres 'skills', 'tools', 'aptitudes' y 'languages'.
9. Creamos una funcion llamada 'Transform_df' donde se agregan las columnas faltantes del schema al DataFrame, se renomran las columnas ya eistentes para que coincidan con las pedidas en el Schema, se reorganiza el orden de las columnas y se completa las columnas corrspondientes con los datos por Default que se me proporcionaron. Para este momento ya tengo un DataFrame con 43 columnas como se me pide.
10. Utilizando la funcion proporcionada, llamada 'generate_slug' generamos el slug y completamos la columna con el mismo nombre.
11. creamos una funcion llamada 'translate_deep_translator' que se encarga de traducir las columnas 'description', 'skills', 'aptitudes', 'languages' y 'benefits'

