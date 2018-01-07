from django.http import Http404
from django.shortcuts import render
from.models import Programs

def index(request):
    all_programs = Programs.objects.all()
    return render(request, 'alumni/index.html', {'all_programs': all_programs,})

def detail(request, program_id):
    try:
        programs = Programs.objects.get(pk=program_id)
    except Programs.DoesNotExist:
        raise Http404("Course does not exist")
    return  render(request, 'alumni/detail.html', {'programs': programs})