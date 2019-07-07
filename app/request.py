import urllib.request,json
from .models import Quote
# Getting the quote base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']


def get_quote():
    '''
    Function that gets the json response to our url request
    '''
    get_quote_url = base_url

    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

    return get_quote_response



def process_results(get_quote_response):
        '''
        Function  that processes the movie result and transform them to a list of Objects
        Args:
        movie_list: A list of dictionaries that contain movie details
        Returns :
        movie_results: A list of movie objects
        '''
        quote_result = []
        for quote in get_quote_response:
            id = quote.get('id')
            author = quote.get('author')
            quote = quote.get('quote')
            permalink = quote.get('permalink')
            if quote:
                quote_object = Quote(id,author,quote,permalink)
                quote_result.append(quote_object)
        return quote_result    
