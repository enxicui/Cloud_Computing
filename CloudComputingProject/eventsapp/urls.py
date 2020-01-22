from django.urls import path
from .views import PostDetailView, PostDeleteView, PostListView, SearchResultsView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='events-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.post_new, name='post-create'),
    path('post/<int:pk>/update', views.post_edit, name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='events-about'),
    path('past_events/', views.past_events, name='past_events'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
