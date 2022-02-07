import csv, io

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Record1
from django.contrib import messages

'''
Daniel Cummings
CST8333 Programming Language Research Project
'''
#this is the view layer that will be shown in the /admin/records/record1.html page
@permission_required('admin.can_add_log_entry')
def view(request):
    record_list = Record1.objects.get(id=6)
    context = {
        'pruid': record_list.pruid,
        'prname': record_list.prname,
        'prnameFR': record_list.prnameFR,
        'date': record_list.date,
        'update': record_list.update,
        'numconf': record_list.numconf,
        'numprob': record_list.numprob,
        'numdeaths': record_list.numdeaths,
        'numtotal': record_list.numtotal,
        'numtested': record_list.numtested,
        'numrecover': record_list.numrecover,
        'percentrecover': record_list.percentrecover,
        'ratetested': record_list.ratetested,
        'numtoday': record_list.numtoday,
        'percentoday': record_list.percentoday,
        'ratetotal': record_list.ratetotal,
        'ratedeaths': record_list.ratedeaths,
        'numdeathstoday': record_list.numdeathstoday,
        'percentdeath': record_list.percentdeath,
        'numtestedtoday': record_list.numtestedtoday,
        'numrecoveredtoday': record_list.numrecoveredtoday,
        'percentactive': record_list.percentactive,
        'numactive': record_list.numactive,
        'rateactive': record_list.rateactive,
        'numtotal_last14': record_list.numtotal_last14,
        'ratetotal_last14': record_list.ratetotal_last14,
        'numdeaths_last14': record_list.numdeaths_last14,
        'ratedeaths_last14': record_list.ratedeaths_last14,
        'numtotal_last7': record_list.numtotal_last7,
        'ratetotal_last7': record_list.ratetotal_last7,
        'numdeaths_last7': record_list.numdeaths_last7,
        'ratedeaths_last7': record_list.ratedeaths_last7,
        'avgtotal_last7': record_list.avgtotal_last7,
        'avgincidence_last7': record_list.avgincidence_last7,
        'avgdeaths_last7': record_list.avgdeaths_last7,
        'avgratedeaths_last7': record_list.avgratedeaths_last7}
    return render(request, "index.html", context=context)

@permission_required('admin.can_add_log_entry')
def index(request):
    record_list = Record1.objects.all()
    context = {'record_list': record_list}
    return render(request, 'index.html', context)

