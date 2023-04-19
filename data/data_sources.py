from newsapi import NewsApiClient
from creds.credentials import NEWSAPI_KEY

# Init the client with NEWSAPI KEY
newsapi = NewsApiClient(api_key=NEWSAPI_KEY)


#Get top 5 headlines
def get_top_headlines(query=None, country='us', k_top=5):
    if query is not None:
        query = query
    else:
        query =''
    headlines = newsapi.get_top_headlines(q=query,
                                          language='en',
                                          country=country)
    top_headlines = [h['title'].split('-')[0] for h in headlines['articles'][:k_top]]

    return top_headlines