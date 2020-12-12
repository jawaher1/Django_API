from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CompanySerializer , MatchSerializer
from .models import Company , Match
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework import status
from rest_framework import generics




class CompanyViewSet(viewsets.ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(viewsets.ModelViewSet):

    def get_object(self, pk): 
        return Company.objects.get(pk=pk)
         # except Company.DoesNotExist:
             # raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        company = CompanySerializer(company)
        return Response(company.data)



class MatchViewSet(viewsets.ModelViewSet):

    queryset = Match.objects.all()
    serializer_class = MatchSerializer


def get(request ,pk):
    import json
    if request.method == 'GET':
        
        l=[]
        
        query = 'SELECT * FROM companies where source_id in ( select left_company_id from matches where right_company_id = %s);' %pk 
        query2 = 'SELECT * FROM companies where source_id in ( select right_company_id from matches where left_company_id = %s);' %pk 
        for i in Company.objects.raw(query):
            s= CompanySerializer(i)
            l.append(s.data)
        for i in Company.objects.raw(query2):
            s= CompanySerializer(i)
            l.append(s.data)
        return JsonResponse(l, safe=False)

            
        
        #
        
       


