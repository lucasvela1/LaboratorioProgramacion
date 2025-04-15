from Ejercicio18 import parser_html, articulo, ArticuloInvalidoErrror

#18) Crear un archivo que use assert para probar métodos clave tanto de la clase
#    Articulo como ParserHtml.


#Testeo de la clase Articulo.
def test_articulo_valido():
    art=articulo("Titulo validado", "Autor", "Texto del articulo")
    assert art.titulo == "Titulo validado"
    assert art.autor == "Autor"
    assert art.texto == "Texto del articulo"
    assert art.es_valido()


def test_articulo_invalido_titulo():
    try:
        articulo(" ", "Juan Pérez", "Texto suficientemente largo.")
        assert False, "Debería haber lanzado excepción por título vacio"
    except ArticuloInvalidoErrror as e:
        assert str(e) == "El título debe tener al menos un caracter."    

def test_articulo_invalido_texto():
    try:
        articulo("Título válido", "Juan Pérez", " ")
        assert False, "Debería haber lanzado excepción por texto vacio"
    except ArticuloInvalidoErrror as e:
        assert str(e) == "El texto debe tener al menos un caracter."        

def test_to_html_con_archivo():
    art = articulo("Titulo validado", "Ana López", "Texto validado.")
    html = art.to_html("archivo.html")
    assert "Leer más" in html
    assert "archivo.html" in html  

#Fin testeo de la clase Articulo.         

#Testeo clase Parser
def test_parser_filtrado_normalizacion():
    arts = [
        articulo("Artículo A", "Carlos Gómez", "Contenido válido del artículo uno."),
        articulo("Artículo B", "María Soler", "Otro contenido también válido."),
    ]
    parser = parser_html(arts)
    assert len(parser.articulos) == 2
    assert parser.articulos[0].autor == "Carlos Gómez"
    assert parser.articulos[1].autor == "María Soler"


def test_filtrar_por_palabra():
    arts = [
        articulo("Artículo C", "Luis Pérez", "Texto con la palabra mágica."),
        articulo("Artículo D", "Ana Ruiz", "Otro texto común."),
    ]
    parser = parser_html(arts)
    filtrados = parser.filtrar_por_palabra("mágica")
    assert len(filtrados) == 1
    assert filtrados[0].autor == "Luis Pérez"    

if __name__ == "__main__":
    test_articulo_valido()
    test_articulo_invalido_titulo()
    test_articulo_invalido_texto()
    test_to_html_con_archivo()
    test_parser_filtrado_normalizacion()
    test_filtrar_por_palabra()
    print("Todos los tests pasaron correctamente.")    