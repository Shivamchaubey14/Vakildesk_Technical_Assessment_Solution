import requests
from bs4 import BeautifulSoup

def scrape_latest_articles(url):
    '''
    Function for scraping the title and the url of latest news.
    '''
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all span tags with the specific class for article titles
            articles = soup.find_all('span', class_='container__headline-text')
            
            if not articles:
                print("No articles found. Check the HTML structure.")
                
            for article in articles:
                title = article.get_text(strip=True)
                
                # Try to find the URL by looking for the parent 'a' tag
                link_tag = article.find_parent('a')
                
                if link_tag:
                    link = link_tag['href']
                    if not link.startswith('http'):
                        link = url + link  # Handle relative links
                else:
                    link = "No URL found"
                
                print(f"Title: {title}")
                print(f"URL: {link}\n")
                
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Example: Scraping CNN's latest articles (with titles and URLs)
scrape_latest_articles('https://edition.cnn.com/')
