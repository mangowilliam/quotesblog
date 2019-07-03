import urllib.request,json
from .user import Quote

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']



def get_quote(category):
    '''
    Function that gets the json response to our url request
    '''
    get_quote_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = None

        if get_quote_response['results']:
            quote_results_list = get_quote_response['results']
            quote_results = process_results(quote_results_list)


    return quote_results
def process_results(quote_list):
    '''
    Function  that processes the movie result and transform them to a list of Object
    '''
    quote_results = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        author = quote_item.get('original_title')
        quote = quote_item.get('overview')
        permalink = quote_item.get('poster_path')
       

        quote_object = Quote(id,author,quote,permalink)
        quote_results.append(quote_object)

    return quote_results
