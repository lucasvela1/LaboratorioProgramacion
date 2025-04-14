#Ejercicio 1: Crear la clase base ParserHtml, inicializarla con una lista de tuplas de artículos y
#generar un HTML básico con f-strings. Los artículos deben tener nombre, autor y
#texto

from datetime import datetime #Lo importamos para el punto 3, para poder usar el datetime.now() para conseguir la hora actual del equipo.

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
        cuerpo_articulos=""
        for titulo, autor, texto in self.articulos:
            cuerpo_articulos += f"""
               <article>
                  <h2>{titulo}</h2>
                  <h4>De {autor}</h4>
                  <p>{texto}</p>
                  <hr> 
                </article>
            """ 

        fecha_actual= datetime.now().strftime("%d/%m/%Y") #Formato de la fecha, dia/mes/año .strftime(Significa string format time, es para darle formato de String)

        html = f""" 
            <!DOCTYPE html> 
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Artículos de lectura</title>
            </head>
            <body>    
               <header>
                 <h1>Artículos</h1>
               </header>  
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