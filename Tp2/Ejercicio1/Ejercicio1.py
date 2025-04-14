#Crear la clase base ParserHtml, inicializarla con una lista de tuplas de artículos y
#generar un HTML básico con f-strings. Los artículos deben tener nombre, autor y
#texto

class parser_html ():
    def __init__(self, articulos):
        self.articulos = articulos
    
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
        html = f""" 
            <!DOCTYPE html> 
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Artículos</title>
            </head>
            <body>    
               <h1>Artículos</h1>
               {cuerpo_articulos} 
            </body> 
            </html>
        """ 
        return html
    
    def guardar_html (self, nombre_archivo="articulos.html"):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(self.generar_html()) #Abrimos el archivo para escribir y le cargamos nuestros datos.

#<hr> Es un separador de secciones, se puede usar para separar los articulos, como parrafos o temas.
#No se puede comentar dentro de los cuerpos del html porque luego se toma como parte del body del html.