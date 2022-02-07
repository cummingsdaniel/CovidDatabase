import csv, io
import json
import datetime
from django.contrib import admin
from .models import Record1
from django.shortcuts import render
from django.urls import path, reverse
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.admin.filters import DateFieldListFilter
# from django.db.models.functions import TruncDay
# from django.db.models import Count
# from django.core.serializers.json import DjangoJSONEncoder
# from rangefilter.filters import DateRangeFilter
'''
Daniel Cummings
CST8333 Programming Language Research Project
'''
# class MyDateTimeFilter(DateFieldListFilter):
#     def __init__(self, *args, **kwargs):
#         super(MyDateTimeFilter, self).__init__(*args, **kwargs)
#
#         now = timezone.now()
#         if timezone.is_aware(now):
#             now = timezone.loc

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class Record1Admin(admin.ModelAdmin):
    '''list_display and list_filter are actually overridding the BaseModelAdmin tuples with the same name
    list_display provides the header names for each column and the list_filter calls fitler component
    implements a filter window with the given models fields'''

    list_display = ('pruid', 'prname', 'prnameFR', 'date',
                    'update', 'numconf', 'numprob', 'numdeaths', 'numtotal', 'numtested', 'numrecover',
                    'percentrecover', 'ratetested', 'numtoday', 'percentoday', 'ratetotal', 'ratedeaths',
                    'numdeathstoday', 'percentdeath', 'numtestedtoday', 'numrecoveredtoday','percentactive',
                    'numactive', 'rateactive', 'numtotal_last14', 'ratetotal_last14', 'numdeaths_last14',
                    'ratedeaths_last14', 'numtotal_last7', 'ratetotal_last7', 'numdeaths_last7',
                    'ratedeaths_last7', 'avgtotal_last7', 'avgincidence_last7', 'avgdeaths_last7',
                    'avgratedeaths_last7')
    list_filter = ('prname', ('date', DateFieldListFilter))
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'

    '''Both has_add_permission and has_delete_permission are actually
    overriding the same method in from the BaseModelAdmin.py in the admin library'''
    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    # the 'upload-csv/' should also be in change_list.html in href= attribute
    # and the self. should be the same name as the html file in templates/admin
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls





# this is the component that uploads the data in the csv file
    def upload_csv(self, request):
        # this is a checks if the right file type has been uploaded
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\r")
            for column in csv_data:
                fields = column.split(",")
                created = Record1.objects.update_or_create(
                    pruid = fields[0],
                    prname = fields[1],
                    prnameFR = fields[2],
                    date = fields[3],
                    update = fields[4],
                    numconf = fields[5],
                    numprob = fields[6],
                    numdeaths = fields[7],
                    numtotal = fields[8],
                    numtested = fields[9],
                    numrecover = fields[10],
                    percentrecover = fields[11],
                    ratetested = fields[12],
                    numtoday = fields[13],
                    percentoday = fields[14],
                    ratetotal = fields[15],
                    ratedeaths = fields[16],
                    numdeathstoday = fields[17],
                    percentdeath = fields[18],
                    numtestedtoday = fields[19],
                    numrecoveredtoday = fields[20],
                    percentactive = fields[21],
                    numactive = fields[22],
                    rateactive = fields[23],
                    numtotal_last14 = fields[24],
                    ratetotal_last14 = fields[25],
                    numdeaths_last14 = fields[26],
                    ratedeaths_last14 = fields[27],
                    numtotal_last7 = fields[28],
                    ratetotal_last7 = fields[29],
                    numdeaths_last7 = fields[30],
                    ratedeaths_last7 = fields[31],
                    avgtotal_last7 = fields[32],
                    avgincidence_last7 = fields[33],
                    avgdeaths_last7 = fields[34],
                    avgratedeaths_last7 = fields[35],
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url) #takes user back to previous page after the uplaod

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Record1, Record1Admin)
# Register your models here.
