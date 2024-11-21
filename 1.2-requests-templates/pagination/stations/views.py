from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open('data-398-2018-08-30.csv', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        bus_station_list = []
        for row in file_reader:
            bus_station_list.append(row)
    paginator = Paginator(bus_station_list, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    page_list = page.object_list
    context = {'page': page,
               'bus_stations': page_list}
    return render(request, 'stations/index.html', context)
