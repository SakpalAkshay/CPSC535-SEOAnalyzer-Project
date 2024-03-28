import validators
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
def validateURL(url):
    
    if validators.url(url):
        return True
    return False

def checkSelection(lst):
    if len(lst) == 0:
        return True
    return False

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r"<[^>]*>", "", text)
    
    # Remove numbers, periods, special characters, angle brackets, and other characters you want to exclude
    text = re.sub(r"[0-9\.,‹›!\"#$%&'()*+,-/:;<=>?@[\]^_`{|}~]", "", text)
    
    # Remove excess spaces by replacing multiple spaces with a single space
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

def makeWorldCloud(dataframe):
        wordcloud = WordCloud(max_font_size=50, max_words=50, background_color="white").generate_from_frequencies(dataframe)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")

def makeBarPlot(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['Word'], df['Word Count'], color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Word Count')
    plt.title('Bar Chart of Word Counts')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()  # Adjust layout to prevent overlap of labels