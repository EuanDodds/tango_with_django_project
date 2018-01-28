import json
import urllib
import http.client
<<<<<<< HEAD
from rango.keys import BING_API_KEY
=======
from rango/keys import BING_API_KEY
>>>>>>> f1eeb615651f4c7b1ccacb44f28a5951e9d08079


def run_query(search_terms):
    # Specify the base
    host = "api.cognitive.microsoft.com"
    path = "/bing/v7.0/search"

    query = "'{0}'".format(search_terms)
    query = urllib.parse.quote(query)

    headers = {'Ocp-Apim-Subscription-Key': BING_API_KEY}
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", path + "?q=" +  query, headers=headers)
    response = conn.getresponse()
    headers = [k + ": " + v for (k,v) in response.getheaders() if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]

    response = response.read()
    json_response = json.loads(response)

    results = []

    for result in json_response['webPages']['value']:
        results.append({'title': result['name'], 'link': result['url'], 'summary': result['snippet']})

    return results
