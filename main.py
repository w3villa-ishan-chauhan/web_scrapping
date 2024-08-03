import requests
from bs4 import BeautifulSoup

# URL of the bookstore's webpage
url = "https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_6ld8byscaa_e&adgrpid=155259813553&hvpone=&hvptwo=&hvadid=674842289467&hvpos=&hvnetw=g&hvrand=15043962902158977216&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9300986&hvtargid=kwd-298110269403&hydadcr=5650_2359487&gad_source=1"
proxies = {
    "http": "http://181.10.200.154"
}

try:
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find book titles and prices based on inspected class names
    book_titles = soup.find_all('h3')
    book_prices = soup.find_all('p', {'class': 'price_color'})
    
    # Check if both lists have been populated
    if book_titles and book_prices:
        for title, price in zip(book_titles, book_prices):
            # Titles are within 'a' tags inside 'h3'
            book_title = title.find('a')['title']
            print("Book: " + book_title + ", Price: " + price.text)
    else:
        print("Failed to find book titles or prices. Please check the class names.")
except requests.exceptions.RequestException as e:
    print("Failed to retrieve the page: " + str(e))
