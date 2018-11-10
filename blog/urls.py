from django.urls import path
from . import views as bv

urlpatterns = [
    path('', bv.index,name='index'),
    path(r'article/<int:article_id>/', bv.article_page, name='article'),
    path('edit/<int:article_id>/', bv.page_edit, name='edit_page'),
    path('edit/action/', bv.action_edit, name='edit_action')

]
