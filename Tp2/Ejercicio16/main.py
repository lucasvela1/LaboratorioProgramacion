from Ejercicio16 import parser_html, articulo

articulos= [
articulo("Principito", "Antoine de Saint-Exupéry", "Un libro que habla de la vida y la soledad"), 
articulo("El Aleph", "Jorge Luis Borges", "Un cuento que explora el infinito y la memoria"), 
articulo("Cien años de soledad", "   Gabriel García Márquez", "Una novela sobre la historia de la familia Buendía"),
articulo("Rayuela", "Julio   Cortázar", "Una novela que invita a leerla de diferentes formas"), 
articulo("El túnel", "Ernesto Sabato", "Una novela sobre la obsesión y la locura"), 
articulo("Ficciones", "Jorge Luis Borges", "Una colección de cuentos fantásticos y filosóficos"), 
articulo("La casa de los espíritus", "   Isabel Allende", "Una novela que mezcla realismo mágico y políticaUna novela que mezcla realismo mágico y políticaUna novela que mezcla realismo mágico y políticaUna novela que mezcla realismo mágico y políticaUna novela que mezcla realismo mágico y políticaUna novela que mezcla realismo mágico y políticaUna novela que mezcla realismo mágico y política"), 
articulo("Pedro Páramo", "juan Rulfo", "Una novela sobre la muerte y el recuerdo"), 
articulo("Los premios", "julio    Cortázar", "Una novela sobre la búsqueda de la identidad"), 
articulo(" ","Pedro Escobar", "Una novela sobre la búsqueda de la identidad"),
articulo("La casa de los espíritus", " ", "Una novela que mezcla realismo mágico y política"),
articulo("La invención de Morel", "adolfo bioy Casares", "Una novela sobre la realidad y la ficción")
] #Lista de tuplas con los libros, autores y resumenes para hacer de prueba

parser= parser_html(articulos)  #Parsea las tuplas que le dimos y las pone en el html
parser.guardar_html("articulos.html") #Guarda el HTML en un archivo

