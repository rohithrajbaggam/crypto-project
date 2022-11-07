from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views, status  
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import uuid 
from .models import CryptoAnalyzerAnalysisImageModel
# Create your views here.


class CoinAnalysesCoinGraphAPIView(views.APIView):
    def get(self, request):
        try:
            # cryptocurrencies = ['BNB-USD','BTC-USD', 'ETH-USD', 'XRP-USD']
            coin1 = request.GET["coin1"]
            coin2 = request.GET["coin2"]
            coin3 = request.GET["coin3"]
            coin4 = request.GET["coin4"]
            start_date = request.GET["start_date"]
            end_date = request.GET["end_date"]

            cryptocurrencies = [coin1, coin2, coin3, coin4]
            # data = yf.download(cryptocurrencies, start='2020-01-01',
            #                 end='2022-10-01')
            data = yf.download(cryptocurrencies, start=start_date,
                            end=end_date)
            data.head()
            data.isnull().any()

            adj_close=data['Adj Close']
            adj_close.head()


            # Returns i.e. percentage change in the adjusted close price and drop the first row with NA's
            returns = adj_close.pct_change().dropna(axis=0)
            #view the first 5 rows of the data frame
            returns.head()


            #ploting the returns
            fig, axs = plt.subplots(2,2,figsize=(16,8),gridspec_kw ={'hspace': 0.2, 'wspace': 0.1})
            axs[0,0].plot(returns[coin1])
            axs[0,0].set_title(coin1)
            axs[0,0].set_ylim([-0.5,0.5])
            axs[0,1].plot(returns[coin2])
            axs[0,1].set_title(coin2)
            axs[0,1].set_ylim([-0.5,0.5])
            axs[1,0].plot(returns[coin3])
            axs[1,0].set_title(coin3)
            axs[1,0].set_ylim([-0.5,0.5])
            axs[1,1].plot(returns[coin4])
            axs[1,1].set_title(coin4)
            axs[1,1].set_ylim([-0.5,0.5])
            plt.savefig(fname="demo")
            plt.show()
            return Response({"message" : "okay"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message" : f"Internal server error, {e}" }, status=status.HTTP_400_BAD_REQUEST)
