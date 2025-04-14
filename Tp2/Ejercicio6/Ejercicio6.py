#Ejercicio 1: Crear la clase base ParserHtml, inicializarla con una lista de tuplas de artículos y
#generar un HTML básico con f-strings. Los artículos deben tener nombre, autor y
#texto

#Separar los artículos por autor usando encabezados <h3>, generando una sección
#por autor con sus artículos debajo.

#Con esto tenemos que cambiar nuestra forma de formatear el texto, porque estabamos poniendo de titulo el nombre del articulo.

from datetime import datetime #Lo importamos para el punto 3, para poder usar el datetime.now() para conseguir la hora actual del equipo.
from collections import defaultdict 

class parser_html ():
    def __init__(self, articulos):
        self.articulos = self.normalizar_y_filtrar(articulos)
    
    #Ejercicio 2:Filtrar artículos vacíos y normalizar el texto del autor quitando espacios y
    #capitalizando el nombre)

    def normalizar_y_filtrar(self, articulos): #Quitar espacios al nombre del autor y haciendo que su nombre se vea en mayusculas y quitar espacios en articulos
       articulos_filtrados = []
       for titulo, autor, texto in articulos:
           if not titulo.strip() or not autor.strip() or not texto.strip():  #Las cadenas vacías son falsas, si alguna es falsa entra en el if, y el continue pasa al siguiente paso del FOR, haciendo que no se agregue esa tupla a la nueva lista.
               continue
           autor_normalizado=" ".join(autor.strip().title().split())#.Strip() Elimina espacios antes y después del String. .title() Cambia la primera letra de cada palabra a mayús. .Split() Separa el string en una lista (para que podamos usar efectivamente el title()) Luego les unimos con el join
           articulos_filtrados.append((titulo.strip(), autor_normalizado, texto.strip()))
       return articulos_filtrados
             
       
    #Ejercicio 3: 3) Modificar el HTML generado para que tenga un header con título del sitio y un
    #                footer con la fecha de generación.
    #El header ya lo creamos en el punto 1, pero le hicimos el titulo como <h1> ahora vamos a meter eso en el <Header> 
    #Usamos datetime.now() para conseguir la fecha actual y se lo agregamos al <footer>.
    
    

    def generar_html(self):

        articulos_por_autor=defaultdict(list)
        for titulo,autor,texto in self.articulos:
          articulos_por_autor[autor].append((titulo,texto))
        
        #6) Incluir al comienzo de la página un índice con enlaces a cada autor usando anchors
        #   internos (<a href="#autor-nombre">…</a>)
        
        indice_html = "<nav><h2>Indice por autor</h2><ul>\n"
        for autor in articulos_por_autor:
         id_autor = autor.lower().replace(" ", "-")
         indice_html += f'<li><a href="#{id_autor}">{autor}</a></li>\n'
        indice_html += "</ul></nav>\n"  

        cuerpo_articulos = ""
        for autor, articulos in articulos_por_autor.items():
           id_autor = autor.lower().replace(" ", "-")  # Volvés a generar el id
           cuerpo_articulos += f'<section>\n<h3 id="{id_autor}">{autor}</h3>\n'
           for titulo, texto in articulos:
              cuerpo_articulos += f"""            
              <article>
                <h4>{titulo}</h4>
                <p>{texto}</p>
                <hr> 
              </article>
              """ 
        cuerpo_articulos += "</section>\n"

        fecha_actual= datetime.now().strftime("%d/%m/%Y") #Formato de la fecha, dia/mes/año .strftime(Significa string format time, es para darle formato de String)
        
        #4) Incluir un bloque de <style> dentro del <head> para aplicar estilos simples como
        #colores, márgenes y tipografía básica.
        #Cada articulo cuenta con su titulo de titulo (valga la redundancia), 
        #seguido de su autor y la descripción. Así le damos un paddin (es decie separación tipo caja entre ellos)
        #y un margen entre cada uno de los articulos.
        html = f""" 
            <!DOCTYPE html> 
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Artículos de lectura</title>
                <style>
                   body{{
                       font-family: Arial, Helvetica, sans-serif;
                       margin: 40px;
                       background-color: #8a6752 ;
                       color: #ff0000;
                   }}
                   article{{
                    background-color: white;
                    padding: 20px;
                    margin: 20px 0;
                    border-radius: 5px;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    }}  
                    nav {{
                    background-color: #e0c5b7;
                    padding: 15px;
                    border-radius: 5px;
                    margin-bottom: 30px;
                }}
                nav ul {{
                    list-style: none;
                    padding: 0;
                }}
                nav li {{
                    margin: 5px 0;
                }}
                nav a {{
                    text-decoration: none;
                    color: #5c3d2e;
                    font-weight: bold;
                }}
                </style>    
            </head>
            <body>    
               <header>
                 <h1>Artículos</h1>
               </header>  
               {indice_html}
               {cuerpo_articulos} 
               <footer> 
                     <p>Fecha de generación: {fecha_actual}</p>
               </footer>         
            </body> 
            </html>
        """ 
        return html
    
    def guardar_html (self, nombre_archivo="articulos.html"):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(self.generar_html()) #Abrimos el archivo para escribir y le cargamos nuestros datos.

#<hr> Es un separador de secciones, se puede usar para separar los articulos, como parrafos o temas.
#No se puede comentar dentro de los cuerpos del html porque luego se toma como parte del body del html.