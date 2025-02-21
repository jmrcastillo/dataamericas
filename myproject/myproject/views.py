# from django.shortcuts import render

# Create your views here.
import os
from dotenv import load_dotenv 
import csv
import requests
from django.shortcuts import render, redirect
from .models import Data
from .forms import UploadFileForm, FetchDataForm # type: ignore



def index(request):
    data = Data.objects.all()
    return render(request, 'index.html', {'data': data})


def tablesdata(request):
    data = Data.objects.all()
    return render(request, 'tablesdata.html', {'data': data})


def tablesgeneral(request):
    data = Data.objects.all()
    return render(request, 'tablesgeneral.html', {'data': data})


def chartschartjs(request):
    data = Data.objects.all()
    return render(request, 'chartschartjs.html', {'data': data})

def chartsapexcharts(request):
    data = Data.objects.all()
    return render(request, 'chartsapexcharts.html', {'data': data})

def chartsecharts(request):
    data = Data.objects.all()
    return render(request, 'chartsecharts.html', {'data': data})

def usersprofile(request):
    data = Data.objects.all()
    return render(request, 'usersprofile.html', {'data': data})

def pagescontact(request):
    data = Data.objects.all()
    return render(request, 'pagescontact.html', {'data': data})

def pagesregister(request):
    data = Data.objects.all()
    return render(request, 'pagesregister.html', {'data': data})

def pageslogin(request):
    data = Data.objects.all()
    return render(request, 'pageslogin.html', {'data': data})


def countries(request):
    data = Data.objects.all()
    return render(request, 'countries.html', {'data': data})

def countries(request):
    data = Data.objects.all()
    return render(request, 'unitedstates.html', {'data': data})

def home(request):
    data = Data.objects.all()
    return render(request, 'home.html', {'data': data})

def index(request):
    # Fetch data from the database
    data = Data.objects.all()

    #load the file env for the key
    load_dotenv()
    
     # API key and URL for fetching news articles
     
    api_key = os.getenv("SECRET_API_KEY")
    # api_key = 'X0JGJVseutnRfgwAD1l0ACSC4D1JEsh9'
    url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key={api_key}"
   
    news = []
    articles = []  # Initialize articles list
    headlines  = []  # Initialize articles list
    

    try:
        # Make the request to the NYT API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response and limit to 5 articles
        json_response = response.json()
        docs = json_response.get("response", {}).get("docs", [])[:10]

        # Create a list of articles with key fields (check for missing data)
        for article in docs:
            articles.append({
                'headline': article.get("headline", {}).get("main", "No headline available"),
                'snippet': article.get("snippet", "No snippet available"),
                'url': article.get("web_url", "#"),
                'pub_date': article.get("pub_date", "No publication date")
            })

    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
    
    # Pass data from the database and articles to the template
    context = {
        'data': headlines,
        'articles': articles
    }
    
    return render(request, 'index.html', context)
    # return redirect('index.html')



def data_list(request):
    data = Data.objects.all()
    return render(request, 'data_list.html', {'data': data})

def upload_csv(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            reader = csv.reader(file.read().decode('utf-8').splitlines())
            for row in reader:
                Data.objects.create(source='CSV', content=','.join(row))
            return redirect('data_list')
    else:
        form = UploadFileForm()
    return render(request, 'upload_csv.html', {'form': form})

def fetch_data(request):
    if request.method == 'POST':
        form = FetchDataForm(request.POST)
        if form.is_valid():
            api_url = form.cleaned_data['api_url']
            link_url = form.cleaned_data['link_url']
            api_response = requests.get(api_url).json()
            link_response = requests.get(link_url).text
            Data.objects.create(source='API', content=str(api_response))
            Data.objects.create(source='Link', content=link_response)
            return redirect('data_list')
    else:
        form = FetchDataForm()
    return render(request, 'fetch_data.html', {'form': form})
