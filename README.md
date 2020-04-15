1) How would we filter for all books with the titles containing the word "Django"

books_django = Books.objects.filter(name__contains='Django') 

2) How would we filter for all books with tag "Fiction"

books_fiction = Book.objects.filter(tags__name="Fiction")

3) How would we filter for all the authors who have written books containing the word "Django"? 

authors_list = Books.obects.filter(name__contains="Django")