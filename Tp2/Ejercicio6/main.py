from Ejercicio6 import parser_html

articulos= [
("Principito", "Antoine de Saint-Exupéry", "Un libro que habla de la vida y la soledad"), (
"El Aleph", "Jorge Luis Borges", "Un cuento que explora el infinito y la memoria"), 
("Cien años de soledad", "   Gabriel García Márquez", "Una novela sobre la historia de la familia Buendía"),
("Rayuela", "Julio   Cortázar", "Una novela que invita a leerla de diferentes formas"), 
("El túnel", "Ernesto Sabato", "Una novela sobre la obsesión y la locura"), 
("Ficciones", "Jorge Luis Borges", "Una colección de cuentos fantásticos y filosóficos"), 
("La casa de los espíritus", "   Isabel Allende", "Una novela que mezcla realismo mágico y política"), 
("Pedro Páramo", "juan Rulfo", "Una novela sobre la muerte y el recuerdo"), 
("Los premios", "julio    Cortázar", "Una novela sobre la búsqueda de la identidad"), 
("  ","Pedro Escobar", "Una novela sobre la búsqueda de la identidad"),
("La casa de los espíritus", " ", "Una novela que mezcla realismo mágico y política"),
("La invención de Morel", "adolfo bioy Casares", "Una novela sobre la realidad y la ficción")
] #Lista de tuplas con los libros, autores y resumenes para hacer de prueba

parser= parser_html(articulos)  #Parsea las tuplas que le dimos y las pone en el html
parser.guardar_html("articulos.html") #Guarda el HTML en un archivo

