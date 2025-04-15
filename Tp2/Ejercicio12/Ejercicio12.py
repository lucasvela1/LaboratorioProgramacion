from datetime import datetime 
from collections import defaultdict 

#11) Incluir un enlace para volver al índice en cada página de artículo individual.

class articulo:
    def __init__(self, titulo, autor, texto):
        self.titulo = titulo.strip()
        self.autor = " ".join(autor.strip().title().split())
        self.texto = texto.strip()  

    def to_html(self, archivo_articulo=None):
        texto_corto = self.texto[:300]
        if len(self.texto) > 300:
            texto_corto += "..."
        boton = f'<a href="{archivo_articulo}" class="btn btn-outline-primary mt-2">Leer más</a>' if archivo_articulo else ""
        return f"""
        <div class="col-md-4 mb-4">
          <div class="card h-100">
             <div class="card-body">
               <h5 class="card-title">{self.titulo}</h5>
               <p class="card-text">{texto_corto}</p>
               {boton}
             </div>
          </div>
        </div>
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

        indice_html = """
           <nav class="navbar navbar-expand-lg navbar-light bg-light">
           <a class="navbar-brand" href="#">Índice de Artículos</a>
           <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
           <span class="navbar-toggler-icon"></span>
           </button>
           <div class="collapse navbar-collapse" id="navbarNav">
           <ul class="navbar-nav">
           """
        for autor in articulos_por_autor:
         id_autor = autor.lower().replace(" ", "-")
         indice_html += f'<li class="nav-item"><a class="nav-link" href="#{id_autor}">{autor}</a></li>\n'
        indice_html += """
            </ul>
          </div>
        </nav>
        """   

        cuerpo_articulos = "<div class='container mt-4'>"
        for autor, articulos in articulos_por_autor.items():
            id_autor = autor.lower().replace(" ", "-")
            cuerpo_articulos += f'<section class="mb-4"><h3 id="{id_autor}">{autor}</h3><div class="row">'
            for articulo in articulos:
                archivo_articulo = f"{articulo.titulo.lower().replace(' ', '-')}.html"
                self.guardar_articulo(articulo, archivo_articulo)
                cuerpo_articulos += articulo.to_html(archivo_articulo)
            cuerpo_articulos += "</div></section>"
        cuerpo_articulos += "</div>"

        fecha_actual= datetime.now().strftime("%d/%m/%Y") 

        html = f""" 
            <!DOCTYPE html> 
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Artículos de lectura</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

            </head>
            <body>    
               <header>
                 <h1 class = "text-center my-4">Artículos</h1>
               </header>  
               {indice_html}
               {cuerpo_articulos} 
               <footer> 
                     <p class = "text-center">Fecha de generación: {fecha_actual}</p>
               </footer>    

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
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
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

         </head>
         <body>
            <header>
               <h1 class="text-center my-4">{articulo.titulo}</h1>
               <h2 class="text-center">De: {articulo.autor}</h2>
            </header>
            <article class="container">
               <p>{articulo.texto}</p>
            </article>
            <footer class="text-center mt-4">
              <a href="articulos.html" class="btn btn-primary">Volver al índice</a>
            </footer>  
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
   
         </body>
         </html>    
        """
       with open(nombre_archivo,"w", encoding="utf-8") as archivo:
           archivo.write(html_articulo) 
           
