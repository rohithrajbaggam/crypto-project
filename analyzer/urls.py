from django.urls import path 
from . import views 

urlpatterns = [ 
    path("test/", views.CoinAnalysesCoinGraphAPIView.as_view(), name="CoinAnalysesCoinGraphAPIViewURL"),
]
