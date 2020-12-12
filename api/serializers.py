from rest_framework import serializers
from .models import Company , Match


class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ('id','source_id', 'source_name', 'name','website', 'email', 'phone', 'address', 'postal_code', 'city', 'country')


class MatchSerializer(serializers.ModelSerializer):
     class Meta:
        model = Match
        fields = ('id', 'left_company_id', 'right_company_id')