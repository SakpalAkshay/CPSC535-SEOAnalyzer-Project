import requests
import bs4
from utility import clean_text, custom_stopwords




def getWepageData(url):
    
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            text = clean_text(soup.get_text())
    
    # Tokenize the text
            words = text.split()

    # Remove custom stop words
            filtered_words = [word for word in words if word.lower() not in custom_stopwords]

    # Join the filtered words back into a text
            filtered_text = " ".join(filtered_words)

        else:
            print("Failed to retrieve the web page. Status code:", response.status_code)
            return None
    except Exception as e:
        print("Error Encountered", e)
        return None
    return filtered_text        


