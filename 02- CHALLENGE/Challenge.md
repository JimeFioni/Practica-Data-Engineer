# Challenge-Data 

## Objetivo
El objetivo de este desafío es desarrollar habilidades de scraping para extraer información específica de la bolsa de trabajo de Apple México y presentar los resultados de manera estructurada. 

## Sitio Web de Referencia
[Bolsa de Trabajo de Apple México](https://jobs.apple.com/en-us/search?location=mexico-MEXC)

## Tareas a Realizar

- **Scraping de Páginas Principales**: Obtener una lista de las categorías de trabajo disponibles en la bolsa de trabajo de Apple México. Extraer el enlace y el nombre de cada categoría. 

- **Scraping de Ofertas de Trabajo:** Seleccionar una categoría de trabajo específica (por ejemplo, "Ingeniería"). Extraer información de al menos 5 ofertas de trabajo, incluyendo título, ubicación, fecha de publicación y descripción

- **Manejo de Paginación:** Si la bolsa de trabajo tiene múltiples páginas, desarrollar un script que maneje la paginación y extraiga información de todas las páginas.

- **Datos Adicionales:** Para cada oferta de trabajo, intentar extraer información adicional como requisitos y responsabilidades (si está disponible). 

- **Procesamiento y almacenamiento de Datos:** Procesar la información según los parametros necesarios para la plataforma (ETL). Almacenar la información extraída en un formato estructurado como lo es un archivo .json.

## Preguntas de Reflexión:

- ¿Cómo manejarías situaciones en las que la estructura de la página cambia?

- ¿Qué estrategias utilizarías para evitar ser bloqueado por medidas de seguridad en el sitio web?

## Notas Importantes
- Utilizar preferiblemente BeautifulSoup y/o Selenium para el scraping. 

- Respetar las políticas de uso del sitio web y asegurarse de no violar los términos y condiciones.

- El modelo de la base de datos que se debe conseguir, esta [aquí.](https://github.com/CarCarrasco1/Challenge-Data/blob/main/schema.py)

## Tiempo de realización 72 hs.

