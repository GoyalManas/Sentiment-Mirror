""" from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.


def index(request):
    newsApi = NewsApiClient(api_key='7463816ad5914b6f8abb9769a7f06d4a')
    #headLines = newsApi.get_top_headlines(sources='ign, cnn')
   # headLines = newsApi.get_top_headlines(country='in', language='en', category='general', page_size=5)
    #headLines = newsApi.get_top_headlines(country='in', category='business')
    all_articles = newsApi.get_everything(q='rajasthan')

    

    articles = all_articles['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, "main/index.html", context={"mylist": mylist})

    """

""" from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
    # Get the user-inputted topic from the request's GET parameters
    topic = request.GET.get('topic', 'rajasthan')

    # Use the user-inputted topic in the News API query
    newsApi = NewsApiClient(api_key='7463816ad5914b6f8abb9769a7f06d4a')
    all_articles = newsApi.get_everything(q=topic)

    articles = all_articles['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    
    mylist = zip(news, desc, img)

    # Pass the user-inputted topic to the template
    return render(request, "main/index.html", context={"mylist": mylist, "topic": topic}) """

from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
    # Get the user-inputted topic from the request's GET parameters
    topic = request.GET.get('topic', 'rajasthan')

    # Use the user-inputted topic in the News API query
    newsApi = NewsApiClient(api_key='7463816ad5914b6f8abb9769a7f06d4a')
    all_articles = newsApi.get_everything(q=topic)

    articles = all_articles['articles']
    mylist = []

    for article in articles:
        title = article.get('title', '')
        desc = article.get('description', '')
        img_url = article.get('urlToImage', '')
        article_url = article.get('url', '')

        # Create a dictionary for each article
        article_data = {
            'title': title,
            'desc': desc,
            'img_url': img_url,
            'article_url': article_url,
        }

        mylist.append(article_data)

    # Pass the user-inputted topic to the template
    return render(request, "main/index.html", context={"mylist": mylist, "topic": topic})

