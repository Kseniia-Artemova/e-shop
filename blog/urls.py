from django.urls import path

from blog.views import BlogEntryListView, BlogEntryCreateView, BlogEntryUnpublishedListView
from blog.views import BlogEntryDetailView, publish_blog_entry, BlogEntryUpdateView, BlogEntryDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', BlogEntryListView.as_view(), name='blog'),
    path('unpublished_entries/', BlogEntryUnpublishedListView.as_view(), name='unpublished_entries'),
    path('new_entry/', BlogEntryCreateView.as_view(), name='new_entry'),
    path('entry/<slug:slug>/', BlogEntryDetailView.as_view(), name='blog_entry'),
    path('activity/<slug:slug>/', publish_blog_entry, name='publish'),
    path('update_entry/<slug:slug>/', BlogEntryUpdateView.as_view(), name='update_entry'),
    path('delete_entry/<slug:slug>/', BlogEntryDeleteView.as_view(), name='delete_entry'),
]