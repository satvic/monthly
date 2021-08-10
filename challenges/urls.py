from django.urls import path
from challenges import views as challenges_views

urlpatterns = [
    path('january/', challenges_views.index, name="jan")
]
