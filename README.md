# Practica4_Black_box_Testing_BDD_y_Selenium
Repositorio para la práctica 4 de la asignatura de Verificación y desarrollo de porgramas.
## Autores
<a href="https://github.com/juanDeVicente">Juan de Vicente</a><br>
<a href="https://github.com/JaimeEscribano">Jaime Escribano</a><br>
<a href="https://github.com/Ayato27">Raúl Martínez</a><br>
<a href="https://github.com/PaulaPascual">Paula Pascual</a><br>
<a href="https://github.com/ClaudiaRodriguezM">Claudia Rodríguez</a>

## Consideraciones
Para poder ejecutar los tests es necesario tener instalado el navegador web <a href="https://www.mozilla.org/firefox/new/">Firefox</a>.

## Instrucciones de instalación
1. Clonar el repositorio git.
2. Instalar las librerias listadas en <a href="https://github.com/juanDeVicente/get_last_50_tweets/blob/master/requirements.txt">requirements.txt</a>
3. Abrir la consola de Python y ejecutar los siguientes comandos:
    ```python
    >>> import nltk
    >>> nltk.download()
    ```
    En la ventana emergente seleccionar la pestaña CORPORA.
    ![N|Solid](https://jantoniomora.files.wordpress.com/2017/08/screenshot-43.png)
    
    En la pestaña seleccionar el "identifier" stopwords y hacer click en el botón de "Download".
    ![N|Solid](https://jantoniomora.files.wordpress.com/2017/08/screenshot-44.png)
4. Añadir tus creedenciales de <a href="https://developer.twitter.com/en/apply-for-access">desarrollador de twitter</a> a las variables de entorno de Python.<br>
    Abrir una consola de Python y ejecutar los siguientes comandos:
    ```python
    >>> import os
    >>> os.environ['ACCESS_TOKEN_KEY'] = <accesstokenkey> 
    >>> os.environ['ACCESS_TOKEN_SECRET'] = <accesstokensecret> 
    >>> os.environ['CONSUMER_KEY'] = <consumerkey>
    >>> os.environ['CONSUMER_SECRET'] = <consumersecret>
    ```
## Instrucciones para ejecutar los tests
1. Abrir la terminal
2. Ejecutar el siguiente comando para ejecutar todos los tests disponibles:
    ```
    <rutaproyecto> Python -m pytest tests/ -v
    ```
3. Ejecutar el siguiente comando para ejecutar los tests de "twitter_word_count.py":
    ```
    <rutaproyecto> Python -m pytest tests/twitter_word_count_test.py -v
    ```
## Instrucciones para ejecutar las pruebas de twitter_word_count
1. Abrir la terminal
2. Ejecutar el siguiente comando para ejecutar la prueba de "twitter_word_count_test.py" con Arturo Pérez Reverte:
    ```
    <rutaejecutablepython> <rutaproyecto>/twitter_word_count.py
    ```

## Instrucciones para ejecutar las pruebas de la página web
1. Abrir la terminal
2. Ejecutar el siguiente comando para ejecutar la prueba de "twitter_word_count_test.py" con Arturo Pérez Reverte:
    ```
    <rutaproyecto>python pytest BDD_tests.py
    ```
    
 ## Instrucciones para instalar selenium
 1. Ejecutar en consola python -m pip install selenium

 ## Instrucciones para ejecutar el servidor de Django
 1. Abrir la terminal
 2. Ir a la ruta del proyecto
 3. Escribir en el terminal 
  ```
    python manage.py runserver 8000
  ```
  Para más información consultar la documentación de Django https://docs.djangoproject.com/en/2.2/
