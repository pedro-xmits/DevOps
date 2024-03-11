from django.shortcuts import render
from core.models import Gasto
from django.http import HttpResponseRedirect, HttpResponse
import csv
import os


def exportar_gastos_csv(request):
    pasta_destino = os.path.join('C:', 'Users', 'Pedro', 'Desktop', 'controle', 'temp')

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    file_path = os.path.join(pasta_destino, "gastos.csv")

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="gastos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Valor','Data'])

    gastos = Gasto.objects.all()

    for gasto in gastos:
        writer.writerow([gasto.valor, gasto.data])

    with open(file_path, 'wb') as csv_file:
        csv_file.write(response.content)

    return response

def GetData(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            data.append(row)
    return data