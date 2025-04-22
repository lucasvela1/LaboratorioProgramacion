from datetime import datetime 
from collections import defaultdict 
import string

def generar_footer(incluir_boton=True):
   año_actual = datetime.now().year
   boton = '<a href="articulos.html" class="btn btn-secondary mt-2">Volver al índice</a>' if incluir_boton else ""
   return f'''
    <footer class="text-center mt-4 mb-4">
        <p>{año_actual} - Tp2 de laboratorio, Lucas Vela</p>
        {boton}
    </footer>
    '''

class ArticuloInvalidoErrror(Exception):  
   def __init__(self, mensaje): 
       super().__init__(mensaje)

class Articulo:
    def __init__(self, titulo, autor, texto):
        titulo = titulo.strip()
        texto= texto.strip() 
        if len(titulo) == 0:
            raise ArticuloInvalidoErrror("El título debe tener al menos un caracter.")
        if len(texto) == 0:  
            raise ArticuloInvalidoErrror("El texto debe tener al menos un caracter.")
        self.titulo= titulo
        self.autor = " ".join(autor.strip().title().split())
        self.texto = texto

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

def apellido(autor):
    partes = autor.split() 
    return partes[-1] if partes else autor  #Nos da el apellido del autor

def inicial_apellido(autor):
    return apellido(autor)[0].upper()  #Ponnos la inicial del apellido en mayuscula

def generar_barra_alfabetica(autores):
    letras_presentes = {inicial_apellido(autor) for autor in autores} #Las letras que se mostraran
    barra = '<div class="text-center mb-4">\n' 
    for letra in string.ascii_uppercase:
        if letra in letras_presentes:  #Le pongo solo el anchor a las letras de los apellidos de los autores que si estan
            barra += f'<a href="#letra-{letra}" class="btn btn-outline-dark btn-sm m-1">{letra}</a>'
        else: #Si no esta en las letras presentes, le pongo un span para que no sea un link
            barra += f'<span class="btn btn-outline-secondary btn-sm m-1 disabled">{letra}</span>'
    barra += '\n</div>'
    return barra

class Parser_html():
    def __init__(self, articulos):
        self.articulos = self.normalizar_y_filtrar(articulos)

    def filtrar_por_palabra(self, palabra):
       palabra=palabra.lower()
       return [art for art in self.articulos if palabra in art.texto.lower()]

    def normalizar_y_filtrar(self, articulos): 
       articulos_filtrados = []
       for item in articulos:
           try: 
             if item.es_valido():  
               articulos_filtrados.append(item)
           except ArticuloInvalidoErrror as e:
              print(f"[ERROR]Articulo invalido:{e}")    
       return articulos_filtrados
             
    def generar_html(self):

        articulos_por_autor = defaultdict(list)
        for articulo in self.articulos:
            articulos_por_autor[articulo.autor].append(articulo)

        todos_los_articulos = []
        for articulos in articulos_por_autor.values():
            todos_los_articulos.extend(articulos)

        barra_alfabetica = generar_barra_alfabetica(articulos_por_autor.keys())

        tabla_autores = """
        <div class="container mb-4">
             <h2>Cantidad de artículos por autor</h2>
            <table class="table table-bordered table-striped"> 
                <thead>
                  <tr>
                    <th>Autor</th>
                    <th>Cantidad de Artículos</th>
                  </tr>
                </thead>
                <tbody>
        """    

        for autor in sorted(articulos_por_autor.keys(), key=apellido): #Ordeno por apellido
           id_autor = autor.lower().replace(" ", "-")
           tabla_autores += f"<tr><td><a href=\"#{id_autor}\">{autor}</a></td><td>{len(articulos_por_autor[autor])}</td></tr>\n"
        tabla_autores += """
                </tbody>
            </table>
        </div>
        """
        
        cuerpo_articulos = "<div class='container mt-4'>"
        letra_actual = ""

        for autor in sorted(articulos_por_autor.keys(), key=apellido):
            nueva_letra = inicial_apellido(autor)
            if nueva_letra != letra_actual:
                letra_actual = nueva_letra #Con esto se consgiue que el usuario pueda saltar de una letra a otra con la barra
                cuerpo_articulos += f'<h4 id="letra-{letra_actual}" class="mt-4">{letra_actual}</h4>' 

            id_autor = autor.lower().replace(" ", "-")
            cuerpo_articulos += f'<section class="mb-4"><h3 id="{id_autor}">{autor}</h3><div class="row">'
            for articulo in articulos_por_autor[autor]:
                archivo_articulo = f"{articulo.titulo.lower().replace(' ', '-')}.html"
                indice = todos_los_articulos.index(articulo)
                self.guardar_articulo(articulo, archivo_articulo, todos_los_articulos, indice)
                cuerpo_articulos += articulo.to_html(archivo_articulo)
            cuerpo_articulos += "</div></section>"
        cuerpo_articulos += "</div>"

        html = f""" 
            <!DOCTYPE html> 
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Artículos de lectura</title>
                <link rel="icon" href="favicon.png" type="image/png">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <link href="estilo_articulos.css" rel="stylesheet">
            </head>
            <body>    
               <header>
                 <h1 class="text-center my-4">Artículos</h1>
                 <img src="imagenLectura.jpg" alt="Imagen de lectura" class="img-fluid mx-auto d-block mb-4" style="max-width: 20%;">
               </header>  
               {barra_alfabetica}
               {tabla_autores}
               {cuerpo_articulos} 
               {generar_footer(incluir_boton=False)}    
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            </body> 
            </html>
        """ 
        return html
    
    def guardar_html(self, nombre_archivo="articulos.html"):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(self.generar_html()) 

    def guardar_articulo(self, articulo, nombre_archivo, lista_articulos, indice):
       enlace_anterior = ""
       enlace_siguiente = ""

       if indice > 0:
          anterior = lista_articulos[indice - 1]
          archivo_anterior = f"{anterior.titulo.lower().replace(' ', '-')}.html"
          enlace_anterior = f'<a href="{archivo_anterior}" class="btn btn-outline-secondary">← Anterior</a>'
    
       if indice < len(lista_articulos) - 1:
         siguiente = lista_articulos[indice + 1]
         archivo_siguiente = f"{siguiente.titulo.lower().replace(' ', '-')}.html"
         enlace_siguiente = f'<a href="{archivo_siguiente}" class="btn btn-outline-secondary">Siguiente →</a>'

       navegacion = f"""
       <div class="d-flex justify-content-between mt-4">
           {enlace_anterior}
           {enlace_siguiente}
       </div>
       """

       html_articulo = f"""
         <!DOCTYPE html>
         <html lang="es">
         <head>
            <meta charset="UTF-8">
            <title>{articulo.titulo}</title>
            <link rel="icon" href="favicon2.png" type="image/png">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="estilo_articulos.css" rel="stylesheet">
         </head>
         <body>
            <header>
               <h1 class="text-center my-4">{articulo.titulo}</h1>
               <h2 class="text-center">De: {articulo.autor}</h2>
            </header>
            <article class="container">
               <p>{articulo.texto}</p>
               {navegacion}
            </article>
            {generar_footer()} 
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
         </body>
         </html>    
        """
       with open(nombre_archivo, "w", encoding="utf-8") as archivo:
           archivo.write(html_articulo) 
