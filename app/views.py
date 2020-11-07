from django.shortcuts import render
from django.shortcuts import render
from . import models
import requests
from bs4 import BeautifulSoup


# Create your views here.

def home(request):
    return render(request, 'base.html')


def search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    url = 'https://www.indeed.com/jobs?q={}&l='
    final_url = url.format(search)
    page = requests.get(final_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(id='resultsCol')
    job_elems = result.find_all('div', class_='jobsearch-SerpJobCard')

    final_posting = []
    for job_elem in job_elems:
        title = job_elem.find('h2', class_='title')
        company = job_elem.find('span', class_='company')
        location = job_elem.find('span', class_='location')
        summary = job_elem.find('div', class_='summary')
        date = job_elem.find('span', class_='date')
        link = job_elem.find('a')['href']
        if None in (title, company, location, summary):
            continue
        final_title = title.text.strip()
        final_company = company.text.strip()
        final_location = location.text.strip()
        final_summary = summary.text.strip()
        final_date = date.text.strip()
        final_link = f"https://indeed.com{link}\n"

        final_posting.append((final_title, final_company, final_location, final_summary, final_date, final_link))

    stuff_for_frontend = {
        'search': search,
        'final_postings': final_posting,
    }

    return render(request, 'app/index.html', stuff_for_frontend)
