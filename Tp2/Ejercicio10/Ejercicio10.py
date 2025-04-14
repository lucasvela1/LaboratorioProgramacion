from datetime import datetime 
from collections import defaultdict 

#9) Modificar la representación del artículo para mostrar solo los primeros 300
#   caracteres de texto, seguido de ….

class articulo:
    def __init__(self, titulo, autor, texto):
        self.titulo = titulo.strip()
        self.autor = " ".join(autor.strip().title().split())
        self.texto = texto.strip()  

    def to_html(self):
       texto_corto=self.texto[:300]
       if len(self.texto)>300:
          texto_corto+="..."
       return f"""
       <article>
          <h4>{self.titulo}</h4>    
          <p>{texto_corto}</p>
          <hr>
        </article>
         """      
    
    def es_valido(self):
       return all([self.titulo, self.autor, self.texto])  


class parser_html ():
    def __init__(self, articulos):
        self.articulos = self.normalizar_y_filtrar(articulos)

    def filtrar_por_palabra(self, palabra):
       palabra=palabra.lower()
       return [art for art in self.articulos if palabra in art.texto.lower()]

    def normalizar_y_filtrar(self, articulos): 
       articulos_filtrados = []
       for item in articulos:
           if item.es_valido():  
             articulos_filtrados.append(item)
       return articulos_filtrados
             
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
           id_autor = autor.lower().replace(" ", "-")  
           cuerpo_articulos += f'<section>\n<h3 id="{id_autor}">{autor}</h3>\n'
           for articulo in articulos:
              archivo_articulo=f"{articulo.titulo.lower().replace(' ','-')}.html"
              self.guardar_articulo(articulo, archivo_articulo) 
              cuerpo_articulos += f'<a href="{archivo_articulo}">{articulo.titulo}</a><br>\n'
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

    def guardar_articulo(self, articulo, nombre_archivo):
       html_articulo=f"""
         <!DOCTYPE html>
         <html lang="es">
         <head>
            <meta charset="UTF-8">
            <title>{articulo.titulo}</title>
            <link rel="stylesheet" href="estilo_articulos.css">
         </head>
         <body>
            <header>
               <h1>{articulo.titulo}</h1>
               <h2>De: {articulo.autor}</h2>
            </header>
            <article>
               <p>{articulo.texto}</p>
            </article>
         </body>
         </html>    
        """
       with open(nombre_archivo,"w", encoding="utf-8") as archivo:
           archivo.write(html_articulo) 
           
