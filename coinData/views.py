from .serializers import coinsSupportedCoinListSerializer, coinsDatetimeToUnixTimeSerializer
from .models import coinsSupportedCoinListModel
from rest_framework import views, status, generics
from rest_framework.response import Response
from core.coinmarket import COIN_MARKET_API_DOMAIN, header, APILAYER_API_URL, APILAYER_headers, APILAYER_payload, DollarImage, InrImage 
import requests, datetime, calendar, random


session = requests.Session()

class coinsSupportedCoinListAPIView(views.APIView):
    def get(self, request):
        queryset = coinsSupportedCoinListModel.objects.all()
        serializer = coinsSupportedCoinListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class coinsCoinListAPIView(views.APIView):
    def get(self, request):
        queryset = coinsSupportedCoinListModel.objects.all()
        serializer = coinsSupportedCoinListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class coinsSavedCoinstoDataBase(views.APIView):
    def post(self, request):
        params = { 
            "start" : 1,
            "limit" : 20,
            "convert" : "USD"
        }
        request_data = session.get(url=f"{COIN_MARKET_API_DOMAIN}", params=params, headers=header)
        for data in request_data.json():
            # print(data)
            if coinsSupportedCoinListModel.objects.filter(
                coin_id=data["id"]).exists():
                pass 
            else:
                coinsSupportedCoinListModel.objects.create(
                    coin_id=data["id"],
                    symbol=data["symbol"],
                    name=data["name"],
                    thumb=data["image"]["thumb"],
                    coin_slug=data["id"],
                    small=data["image"]["small"],
                    large=data["image"]["large"],
                ) 
        
        return Response({"message" : "ok"})
    


class singleCoinPriceAPIView(views.APIView):
    def get(self, request):
        try:

            # ?ids=bitcoin&vs_currencies=usd
            params = {
                "ids" : request.GET["ids"],
                "vs_currencies" : request.GET["vs_currencies"]
            }
            query = coinsSupportedCoinListModel.objects.get(coin_id=request.GET["ids"])
            req_data = session.get(url=f"{COIN_MARKET_API_DOMAIN}simple/price", 
            params=params, headers=header)
            if request.GET["vs_currencies"] == "usd":
                currencyImage = DollarImage
            else:
                currencyImage = InrImage
            return_data = {
                "coin" : request.GET["ids"],
                "currencies" : request.GET["vs_currencies"],
                "price" : req_data.json()[f'{request.GET["ids"]}'][f'{request.GET["vs_currencies"]}'],
                "coin_image" : query.large,
                "currency_image" : currencyImage

            }
            
            return Response(return_data)
        except:
            return Response({"message" : "Internal Server Error"}, status=status.HTTP_400_BAD_REQUEST)

# ?start=1&limit=20&convert=USD
        # params = {
        #     "start" : 1,
        #     "limit" : 20,
        #     "convert" : "USD"
        # }

class CoinListAPIView(views.APIView):
    def get(self, request):
        try:

            # ?start=1&limit=20&convert=USD
            params = {
                "start" : request.GET["start"],
                "limit" : request.GET["limit"],
                "convert" : request.GET["convert"]
            }
            req_data = session.get(url=f"{COIN_MARKET_API_DOMAIN}coins", 
            params=params, headers=header)
            return Response(req_data.json())
        except:
            return Response({"message" : "Internal Server Error"}, status=status.HTTP_400_BAD_REQUEST)



class CoinMarketListAPIView(views.APIView):
    def get(self, request):
        try:

            # ?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false
            params = {
                "vs_currency" : request.GET["vs_currency"],
                "order" : request.GET["order"],
                "per_page" : request.GET["per_page"],
                "page" : request.GET["page"],
                "sparkline" : request.GET["sparkline"],
                
            }
            req_data = session.get(url=f"{COIN_MARKET_API_DOMAIN}coins/markets", 
            params=params, headers=header)
            return Response(req_data.json())
        except:
            return Response({"message" : "Internal Server Error"}, status=status.HTTP_400_BAD_REQUEST)



class CoinDetailsAPIView(views.APIView):
    def get(self, request, coin_id):
        try:
            req_data = session.get(url=f"{COIN_MARKET_API_DOMAIN}coins/{coin_id}", 
            headers=header)
            return Response(req_data.json())
        except:
            return Response({"message" : "Internal Server Error"}, status=status.HTTP_400_BAD_REQUEST)

# ?date=30-12-2017
class CoinHistoryListAPIView(views.APIView):
    def get(self, request):
        try:
            # ?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false
            params = {
                "date" : request.GET["date"],                
            }
            req_data = session.get(url=f"{COIN_MARKET_API_DOMAIN}coins/bitcoin/history", 
            params=params, headers=header)
            return Response(req_data.json())
        except:
            return Response({"message" : "Internal Server Error"}, status=status.HTTP_400_BAD_REQUEST)


class CoinMarketChartAPIView(views.APIView):
    def get(self, request):
        try:
            # ?vs_currency=usd&days=14
            params = {
                "vs_currency" : request.GET["vs_currency"],
                "days" : request.GET["days"],
            }
            req_data = session.get(url=f"{COIN_MARKET_API_DOMAIN}coins/bitcoin/market_chart", 
            params=params, headers=header)
            return Response(req_data.json())
        except:
            return Response({"message" : "Internal Server Error"}, status=status.HTTP_400_BAD_REQUEST)

class CoinMarketChartRangeAPIView(views.APIView):
    def get(self, request):
        try:
            # ?vs_currency=usd&from=1392577232&to=1422577232
            params = {
                "vs_currency" : request.GET["vs_currency"],
                "from" : request.GET["from"],
                "to" : request.GET["to"]
            }
            req_data = session.get(url=f"{COIN_MARKET_API_DOMAIN}coins/bitcoin/market_chart/range", 
            params=params, headers=header)
            return Response(req_data.json())
        except:
            return Response({"message" : "Internal Server Error"}, status=status.HTTP_400_BAD_REQUEST)




class CoinOHLCGraphDataAPIView(views.APIView):
    def get(self, request, coin_id):
        try:
            params = {
                "vs_currency" : request.GET["vs_currency"],
                "days" : request.GET["days"]
            }
            req_data = session.get(url=f"{COIN_MARKET_API_DOMAIN}coins/{coin_id}/ohlc", 
            params=params, headers=header)
            return Response(req_data.json())
        except:
            return Response({"message" : "Internal Server Error"}, status=status.HTTP_400_BAD_REQUEST)


class coinConvertDatetimeToUnixTime(generics.GenericAPIView):
    serializer_class = coinsDatetimeToUnixTimeSerializer
    def post(self, request):
        try:
            print('reqest-data', request.data)
            date_list = list(str(request.data["datetime"]).split("-"))
            date_time = datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]), 0, 0).utcnow()
            unix_timestamp =  calendar.timegm(date_time.utctimetuple())
            return Response({"unix_timestamp" : unix_timestamp})
        except:
            return Response({"message" : "Internal Server Error"},
             status=status.HTTP_400_BAD_REQUEST)



class CoinCryptoGraphAnalysisAPIView(views.APIView):
    def get(self, request, coin_id):
        try:
            params = {
                "vs_currency" : request.GET["vs_currency"],
                "days" : request.GET["days"]
            }
            req_data = session.get(url=f"{COIN_MARKET_API_DOMAIN}coins/{coin_id}/ohlc", 
            params=params, headers=header)
            return Response(req_data.json())
        except:
            return Response({"message" : "Internal Server Error"}, status=status.HTTP_400_BAD_REQUEST)


class CoinCrytoPredictorAPIView(views.APIView):
    def getUSDollarValue(self):
        try:
            dollar_data = session.get(url=APILAYER_API_URL, headers=APILAYER_headers).json()
            x = dollar_data['result']
            return x
        except:
            return 80

    def getBitCoinGraphData(self, request):
        params = {
                "vs_currency" : request.GET["vs_currency"],
                "days" : request.GET["days"]
            }
        req_data = session.get(url=f"{COIN_MARKET_API_DOMAIN}coins/bitcoin/ohlc", 
            params=params, headers=header)
        return req_data.json()
    
    def getRequestedCoinGraphData(self, request, coin_id):
        params = {
                "vs_currency" : request.GET["vs_currency"],
                "days" : request.GET["days"]
            }
        req_data = session.get(url=f"{COIN_MARKET_API_DOMAIN}coins/{coin_id}/ohlc", 
            params=params, headers=header)
        return req_data.json()  

    def dataEngineering(self, x, usd, i, lis):
        count = random.randint(1, 10)

        if count % 2 ==0 :
            x += ((x*0.001*count))
        else:
            x -= ((x*0.001*count))
        return x
    # 1668708000000
    #0.00000000000001
    # def dataEngineering(self, x, usd, i, lis):
    #     _sum = 0
    #     count = 0
    #     print('lis', lis)
    #     try:
    #         for k in range(1, 5):
    #             if k != i:
    #                 _sum += lis[k]
    #                 count+=1
    #         print(_sum, count)
    #         main_sum = float(_sum/count)
    #         return main_sum
    #     except Exception as e:
    #         print(e)
    #         return x

    def cryptoPredictorFunction(self, request, coin_id, UsDollarValue):
        result = []
        count=len(self.getRequestedCoinGraphData(request, coin_id))-1
        for x in self.getRequestedCoinGraphData(request, coin_id):
            data = []
            # data.append(x[0])
            data.append(count)
            count = count - 1 
            
            for i in range(1, 5):
                data.append(self.dataEngineering(x[i], UsDollarValue, i, x))

            result.append(data)
        return result

    def get(self, request, coin_id):
        
        try:
            # UsDollarValue = self.getUSDollarValue()
            UsDollarValue = 80
            return_data = self.cryptoPredictorFunction(request, coin_id, UsDollarValue)
            return Response(return_data[::-1])
        except Exception as e:
            return Response({"data" : f"Something went wrong, {e}"})


