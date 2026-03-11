# TODO Найдите количество книг, которое можно разместить на дискете
weight_book  = 4 * 25 * 50 * 100
Mb_to_b = 1.44 * 1024 * 1024
number_of_books = Mb_to_b // weight_book
number_of_books = int(number_of_books)
print("Количество книг, помещающихся на дискету:", number_of_books)

