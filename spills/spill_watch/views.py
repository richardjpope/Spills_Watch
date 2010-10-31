from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import models 

def index(request):
    return render_to_response('index.html', {}, context_instance = RequestContext(request))

def company(request, company_id):
    company = get_object_or_404(models.Company, id=company_id)    
    return render_to_response('company.html', {'company': company}, context_instance = RequestContext(request))


def companies(request, page = 1):

    companies = models.Company.objects.all()
    companies =  companies.order_by('name')
    paginator = Paginator(companies, 100)

    try:
          companies = paginator.page(page)
    except (EmptyPage, InvalidPage):
          companies = paginator.page(paginator.num_pages)
                      
    return render_to_response('companies.html', {'companies': companies}, context_instance = RequestContext(request))

def search(request):

    search_term = request.GET.get('q', '').strip()
    if search_term != '':
        page = 1
        companies = models.Company.objects.filter(name__icontains=search_term)
    
        companies =  companies.order_by('name')
        paginator = Paginator(companies, 100)

        try:
              companies = paginator.page(page)
        except (EmptyPage, InvalidPage):
              companies = paginator.page(paginator.num_pages)
    else:
        companies = []
          
    return render_to_response('search.html', {'companies': companies, 'search_term': search_term}, context_instance = RequestContext(request))



def incident(request, incident_id):
    incident = get_object_or_404(models.Incident, id=incident_id)
    return render_to_response('incident.html', {'incident': incident}, context_instance = RequestContext(request))


def incidents(request, page = 1):

    incidents = models.Incident.objects.all()
    incidents =  incidents.order_by('title')
    paginator = Paginator(incidents, 100)

    try:
          incidents = paginator.page(page)
    except (EmptyPage, InvalidPage):
          incidents = paginator.page(paginator.num_pages)

    return render_to_response('incidents.html', {'incidents': incidents}, context_instance = RequestContext(request))