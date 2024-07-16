from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .model_pipeline import CropYieldModel
from .serializers import CropYieldInputSerializer
import pandas as pd

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
