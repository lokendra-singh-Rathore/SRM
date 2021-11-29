from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import MultiWidget
from django_filters.widgets import RangeWidget,SuffixedMultiWidget
import django_filters
from .models import *
from django import forms
from django_filters import DateFilter,DateFromToRangeFilter


class Feefilter(django_filters.FilterSet):
    upcoming_Due_Date= django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
                attrs={'placeholder': 'yyyy-mm-dd'}))
   
    class Meta:
        model=Fee
        fields=['student','payment_mode']


        
        