import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.title.string if soup.title else 'No title found'
    
    links = [a['href'] for a in soup.find_all('a', href=True)]
    
    return {
        'title': title,
        'links': links
    }

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    result = scrape_website(url)
    
    if result:
        print(f"Page Title: {result['title']}")
        print("Links:")
        for link in result['links']:
            print(link)
    else:
        print("Failed to scrape the website.")