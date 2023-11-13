import requests
import json



def google_search(keywords):
    api_key = ''
    endpoint = f"https://www.googleapis.com/customsearch/v1?q={keywords}&key={api_key}&num=14"
    response = requests.get(endpoint)
    return response.json()['items']  



# Function for Yahoo Search
def yahoo_search(keywords):
    api_key = ''
    endpoint = f"={keywords}&key={api_key}&num=14"
    response = requests.get(endpoint)
    return response.json()['items']  
    pass

def bing_search(keywords):
    pass


def duckduckgo_search(keywords):

    pass

def main(keywords):
    results = {
        "Google": google_search(keywords),
        "Yahoo": yahoo_search(keywords),
        "Bing": bing_search(keywords),
        "Ask": ask_search(keywords),
        "DuckDuckGo": duckduckgo_search(keywords)
    }
    return results

if __name__ == "__main__":
    keywords = input("Enter search keywords: ")
    aggregated_results = main(keywords)
    for engine, results in aggregated_results.items():
        print(f"\nResults from {engine}:")
        for result in results:
            print(result)

