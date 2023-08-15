from django.shortcuts import render
from .models import Worker, PlantsModel
# Create your views here.

def index(request):
    """View function for home page of site."""

    num_worker = Worker.objects.all().count()

    num_plantModel = PlantsModel.objects.count()

    context = {
        'num_worker': num_worker,
        'num_plantModel': num_plantModel,
    }

    return render(request, 'index.html', context=context)
