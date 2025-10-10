#todo: Заданы множества
#Даны читатели книг
readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1' }

#Даны читатели газет
readers_magazines = { 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}

# Находим пересечение — читатели, которые читают и книги, и газеты
readers_both = readers_books & readers_magazines

print("Читатели, которые читают и книги, и газеты:", readers_both)