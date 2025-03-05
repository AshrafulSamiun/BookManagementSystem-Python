from django.urls import path,include
from .views import homepage, add_book, update_book, delete_book, display_book
urlpatterns = [
   path('',homepage,name='homepage'),
   path('book_list',homepage,name='book_list'),
   path('add_book',add_book, name='add_book'),
   path('update_book/<int:id>/',update_book, name='update_book'),
   path('display_book/<int:id>/',display_book, name='display_book'),
   path('delete_book/<int:id>/',delete_book, name='delete_book')
   # path('',include('book.urls'))
]