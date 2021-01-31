from django.shortcuts import render

listings = [
    {
        'author' : 'asiqur',
        'title' : 'Iphone 12',
        'content' : 'Click the Build tab to bring it forward. From the Work In drop-down list, select the page group that owns the HTML Template. Under the Layout & Appearance section, click the Browse link next to HTML Templates. Click the Copy link next to the HTML Template.',
        'title2' : 'Samsung 12',
        'content2' : 'Click the Build tab to bring it forward. From the Work In drop-down list, select the page group that owns the HTML Template. Under the Layout & Appearance section, click the Browse link next to HTML Templates. Click the Copy link next to the HTML Template.',
        'date_posted' : 'september 1 , 2019'
    },
    {
        'author' : 'asiqur',
        'title' : 'Iphone 12',
        'content' : 'Click the Build tab to bring it forward. From the Work In drop-down list, select the page group that owns the HTML Template. Under the Layout & Appearance section, click the Browse link next to HTML Templates. Click the Copy link next to the HTML Template.',
        'title2' : 'Samsung 12',
        'content2' : 'Click the Build tab to bring it forward. From the Work In drop-down list, select the page group that owns the HTML Template. Under the Layout & Appearance section, click the Browse link next to HTML Templates. Click the Copy link next to the HTML Template.',
        'date_posted' : 'september 1 , 2019'
    },
    {
        'author' : 'asiqur',
        'title' : 'Iphone 12',
        'content' : 'Click the Build tab to bring it forward. From the Work In drop-down list, select the page group that owns the HTML Template. Under the Layout & Appearance section, click the Browse link next to HTML Templates. Click the Copy link next to the HTML Template.',
        'title2' : 'Samsung 12',
        'content2' : 'Click the Build tab to bring it forward. From the Work In drop-down list, select the page group that owns the HTML Template. Under the Layout & Appearance section, click the Browse link next to HTML Templates. Click the Copy link next to the HTML Template.',
        'date_posted' : 'september 1 , 2019'
    }
]

def home(request):
    postings = {
        'listings' : listings 
    }
    return render(request, 'front/front.html',  postings)

def about(request):
    postings = {
        'listings' : listings 
    }
    return render(request, 'front/about.html', postings )
