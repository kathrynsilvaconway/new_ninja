from django.urls import path, include

urlpatterns = [
    path('', include('get_gold.urls')),
]
