from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from shop_api.models import Document
from shop_api.permissions import IsOwnerOrReadOnly
from shop_api.serializers import DocumentSerializer


class DocumentList(APIView):
    def get(self, request, format=None):
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        doctypeid = self.request.query_params.get('doctypeid', None)
        userid = self.request.query_params.get('userid', None)
        storeid = self.request.query_params.get('storeid', None)

        sqlsuff = ''

        if date_from is not None and date_to is not None:
            sqlsuff = sqlsuff + ' WHERE updated BETWEEN {} AND {}'.format(date_from, date_to)

        if doctypeid is not None:
            sqlsuff = self.make_sql(sqlsuff, ' type_id = {} '.format(doctypeid))

        if userid is not None:
            sqlsuff = self.make_sql(sqlsuff, ' user_id = {} '.format(userid))

        if storeid is not None:
            sqlsuff = self.make_sql(sqlsuff, ' store_id = {} '.format(storeid))

        try:
            print(sqlsuff)
            documents = Document.objects.raw('SELECT * FROM shop_api_document ' + sqlsuff)
            serializer = DocumentSerializer(documents, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def make_sql(self, sql_suff: str, sql: str):
        if sql_suff.__len__() == 0:
            sql_suff = sql_suff + ' WHERE '
        else:
            sql_suff = sql_suff + ' AND '

        return sql_suff + sql

    def post(self, request, format=None):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
