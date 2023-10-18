from django.shortcuts import render, get_object_or_404, redirect
from .models import WeightRecord
from .forms import WeightRecordForm
from django.db import models

def index(request):
    records = WeightRecord.objects.order_by('-date')
    max_weight = records.first().max_weight if records else 0
    min_weight = records.last().min_weight if records else 0

    average_max_weight = records.aggregate(avg_max=models.Avg('max_weight'))
    average_min_weight = records.aggregate(avg_min=models.Avg('min_weight'))
    average_differences = records.aggregate(avg_differences=models.Avg(models.F('max_weight') - models.F('min_weight')))
    
    average_max_weight = round(average_max_weight['avg_max'], 2) if average_max_weight['avg_max'] is not None else "Belum Ada Data"
    average_min_weight = round(average_min_weight['avg_min'], 2) if average_min_weight['avg_min'] is not None else "Belum Ada Data"
    average_differences = round(average_differences['avg_differences'], 2) if average_differences['avg_differences'] is not None else "Belum Ada Data"

    context = {
        'records': records,
        'max_weight': max_weight,
        'min_weight': min_weight,
        'average_max_weight': average_max_weight,
        'average_min_weight': average_min_weight,
        'average_differences': average_differences
    }
    return render(request, 'index.html', context)


def detail(request, record_id):
    record = get_object_or_404(WeightRecord, pk=record_id)
    return render(request, 'detail.html', {'record': record})

def create(request):
    if request.method == 'POST':
        form = WeightRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WeightRecordForm()
    
    return render(request, 'create.html', {'form': form})

def edit(request, record_id):
    record = get_object_or_404(WeightRecord, pk=record_id)
    if request.method == 'POST':
        form = WeightRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WeightRecordForm(instance=record)
    return render(request, 'edit.html', {'form': form})


def hapus_record(request, record_id):
    record = get_object_or_404(WeightRecord, pk=record_id)
    record.delete()
    return redirect('index')

