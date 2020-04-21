from django.urls import path

from . import views

urlpatterns = [
    path('', views.basic_view, name='Base'),
    path('app', views.second_view, name='second'),

    path('<int:product_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:product_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:product_id>/vote/', views.vote, name='vote'),
]