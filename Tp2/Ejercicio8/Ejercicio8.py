from datetime import datetime 
from collections import defaultdict 

#7)Reemplazar las tuplas por objetos de una clase Articulo con atributos titulo,
#autor, texto y un método to_html() que devuelva su representación.

class articulo:
    def __init__(self, titulo, autor, texto):
        self.titulo = titulo.strip()
        self.autor = " ".join(autor.strip().title().split())
        self.texto = texto.strip()  

    def to_html(self):
       return f"""
       <article>
          <h4>{self.titulo}</h4>    
          <p>{self.texto}</p>
          <hr>
        </article>
         """      
    
    def es_valido(self):
       return all([self.titulo, self.autor, self.texto])  # Verifica que todos los atributos no estén vacíos


class parser_html ():
    def __init__(self, articulos):
        self.articulos = self.normalizar_y_filtrar(articulos)
    

    #8)Agregar un método para filtrar por una palabra clave que devuelva solo los artículos
    #  que contienen esa palabra en el texto.

    def filtrar_por_palabra(self, palabra):
       palabra=palabra.lower()
       return [art for art in self.articulos if palabra in art.texto.lower()]

    def normalizar_y_filtrar(self, articulos): 
       articulos_filtrados = []
       for item in articulos:
           if item.es_valido():  
             articulos_filtrados.append(item)
       return articulos_filtrados #se modifica este metodo, al inicializar el objeto con los valores se normaliza. Aquí se agrega a la lista si cumple las condiciones
             
       
    def generar_html(self):

        articulos_por_autor=defaultdict(list)
        for articulo in self.articulos:
          articulos_por_autor[articulo.autor].append(articulo)

        indice_html = "<nav><h2>Indice por autor</h2><ul>\n"
        for autor in articulos_por_autor:
         id_autor = autor.lower().replace(" ", "-")
         indice_html += f'<li><a href="#{id_autor}">{autor}</a></li>\n'
        indice_html += "</ul></nav>\n"  

        cuerpo_articulos = ""
        for autor, articulos in articulos_por_autor.items():
           id_autor = autor.lower().replace(" ", "-")  # Volvés a generar el id
           cuerpo_articulos += f'<section>\n<h3 id="{id_autor}">{autor}</h3>\n'
           for articulo in articulos:
              cuerpo_articulos += articulo.to_html()  
        cuerpo_articulos += "</section>\n"

        fecha_actual= datetime.now().strftime("%d/%m/%Y") 

        html = f""" 
            <!DOCTYPE html> 
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Artículos de lectura</title>
                <link rel="stylesheet" href="estilo_articulos.css">  
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
            archivo.write(self.generar_html()) 