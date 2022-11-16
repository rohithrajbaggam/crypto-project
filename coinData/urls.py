from django.urls import path
from . import views 
urlpatterns = [
    path("support-coins-list/", views.coinsSupportedCoinListAPIView.as_view(), name="coinsSupportedCoinListAPIViewURL"),
    path("coins-list/", views.coinsCoinListAPIView.as_view(), name="coinsCoinListAPIViewURL"),
    path("save-coins/", views.coinsSavedCoinstoDataBase.as_view(), name="coinsSavedCoinstoDataBaseURL"),
    
    path("single-coin-price/", views.singleCoinPriceAPIView.as_view(), name="singleCoinPriceAPIViewURL"),
    path("api-coin-list/", views.CoinListAPIView.as_view(), name="CoinListAPIViewURL"),
    path("api-coin-list/<coin_id>/", views.CoinDetailsAPIView.as_view(), name="CoinDetailsAPIViewURL"),
    path("api-coin-list-market/", views.CoinMarketListAPIView.as_view(), name="CoinMarketListAPIViewURL"),
    path("api-coin-history/", views.CoinHistoryListAPIView.as_view(), name="CoinHistoryListAPIViewURL"),
    path("api-coin-market-chart/", views.CoinMarketChartAPIView.as_view(), name="CoinMarketChartAPIViewURL"),
    path("api-coin-market-chart-range/", views.CoinMarketChartRangeAPIView.as_view(), name="CoinMarketChartRangeAPIViewURL"),
    # graph data for Visualizer 
    path("api-coin-graph-data/<coin_id>/", views.CoinOHLCGraphDataAPIView.as_view(), name="CoinOHLCGraphDataAPIViewURL"),
    path("unix-converter/", views.coinConvertDatetimeToUnixTime.as_view(), name="coinConvertDatetimeToUnixTimeURL"),
    path("crypto-predictor/<coin_id>/", views.CoinCrytoPredictorAPIView.as_view(), name="CoinCrytoPredictorAPIViewURL"),
    # path("")
    
]