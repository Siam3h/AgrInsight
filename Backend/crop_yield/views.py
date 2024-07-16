from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .model_pipeline import CropYieldModel
from .serializers import CropYieldInputSerializer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from django.http import HttpResponse

crop_yield_model = CropYieldModel()

class PredictYield(APIView):
    def post(self, request):
        serializer = CropYieldInputSerializer(data=request.data, many=True)
        if serializer.is_valid():
            data = serializer.validated_data
            df = pd.DataFrame(data)
            try:
                predictions = crop_yield_model.predict(df)
                return Response(predictions, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class YieldGraph(APIView):
    def get(self, request):
        # Load data
        df_yield = pd.read_csv(r'crop_yield/data/yield.csv')
        df_yield.rename(columns={"Value": "hg/ha_yield"}, inplace=True)

        # Plot
        plt.figure(figsize=(10, 6))
        sns.boxplot(x="Item", y="hg/ha_yield", data=df_yield)
        plt.title('Crop Yield per Item')

        # Save plot to a BytesIO object
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Return the plot as a response
        return HttpResponse(buffer, content_type='image/png')
