from django.http import HttpResponse
from django.template import loader
from.models import Programs

def index(request):
    all_programs = Programs.objects.all()
    template = loader.get_template('alumni/index.html')
    context = {
        'all_programs': all_programs,
    }
    return HttpResponse(template.render(context, request))

def detail(request, program_id):
    return HttpResponse("<h2>Details for Album id: " + str(program_id) +"</h2>")