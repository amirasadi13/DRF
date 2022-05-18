from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from core.models import Music
from core.serializers import MusicSerializer
from utils.musicPagination import MusicListPagination
from rest_framework import filters


class MusicView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def put(self, request, pk):
        try:
            music = Music.objects.get(id=pk)
            serializer = MusicSerializer(instance=music, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
        except Music.DoesNotExist:
            return Response(status=404, data={"message": "music not found"})

    def delete(self, request, pk):
        try:
            music = Music.objects.get(id=pk)
            # music.is_deleted = True
            # music.save()
            music.delete()
            return Response(status=200, data={'message': 'success fully deleted'})
        except Music.DoesNotExist:
            return Response(status=404, data={'message': 'music not found'})


class MusicsList(ListAPIView):
    queryset = Music.objects.all().order_by('-id')
    serializer_class = MusicSerializer
    permission_classes = [AllowAny]
    # pagination_class = MusicListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['song', 'singer']
