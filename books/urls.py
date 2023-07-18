from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (BookViewApi,
                    BookDetailApiView,
                    BookUpdateApiView,
                    BookDeleteApiView,
                    BookUpdateDestroy,
                    BookListCreateAPI,
                    BookListApiView,
                    BookCreateApiView,
                    BookViewSet)
app_name = 'books'
simplerouter = SimpleRouter()
simplerouter.register('books', BookViewSet, basename='books')
urlpatterns = [
    # path('books/', BookViewApi.as_view(),),
    # path('bookslist/', BookListApiView.as_view()),
    # path('bookscreate/', BookCreateApiView.as_view()),
    # # path('create/', BookCreateApiView.as_view(),),
    # path('booklistcreate/', BookListCreateAPI.as_view()),
    # path('bookupdatedelete/', BookUpdateDestroy.as_view()),
    # path('books/<int:pk>/', BookDetailApiView.as_view(),),
    # path('book/<int:pk>/update', BookUpdateApiView.as_view(),),
    # path('book/<int:pk>/delete', BookDeleteApiView.as_view(),),
]
urlpatterns = urlpatterns + simplerouter.urls

