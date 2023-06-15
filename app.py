from flask import Flask, render_template, request, jsonify
import re
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from transformers import pipeline
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        product_link = request.json['productLink']
        reviews = scrape_amazon_reviews(product_link)
        sentiment = analyze_reviews(reviews)
        return jsonify(sentiment=sentiment)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify(error=str(e))

def word_to_number(word):
    word = word.lower()
    num_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10
    }
    return num_dict.get(word, word)

def scrape_amazon_reviews(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    reviews = []

    while True:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-hook="review"]'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        review_elements = soup.find_all('div', {'data-hook': 'review'})
        for element in review_elements:
            review_text = element.find('span', {'data-hook': 'review-body'}).text.strip()
            review_rating = float(element.find('span', {'class': 'a-icon-alt'}).text.split()[0])
            review_date_text = element.find('span', {'data-hook': 'review-date'}).text
            review_date_text = re.sub(r'Reviewed in .* on ', '', review_date_text)
            review_date = datetime.datetime.strptime(review_date_text, '%d %B %Y')

            helpful_votes_element = element.find('span', {'data-hook': 'helpful-vote-statement'})
            if helpful_votes_element:
                helpful_votes = int(word_to_number(helpful_votes_element.text.split()[0]))
            else:
                helpful_votes = 0

            reviews.append({
                'text': review_text,
                'rating': review_rating,
                'date': review_date,
                'helpful_votes': helpful_votes
            })

        try:
            next_page_link = driver.find_element_by_css_selector('a.a-pagination-next')
            next_page_link.click()
            time.sleep(2)
        except Exception as e:
            break

    driver.quit()
    return reviews

def analyze_reviews(reviews):
    nlp = pipeline('sentiment-analysis')
    positive_count = 0
    negative_count = 0
    total_weight = 0

    for review in reviews:
        result = nlp(review['text'])[0]
        weight = review['helpful_votes'] + 1
        total_weight += weight

        if result['label'] == 'POSITIVE':
            positive_count += weight
        elif result['label'] == 'NEGATIVE':
            negative_count += weight

    if total_weight == 0:
        return "No reviews available."
    else:
        positive_percentage = (positive_count / total_weight) * 100
        negative_percentage = (negative_count / total_weight) * 100

        if positive_percentage > negative_percentage:
            return "Overall, the product has positive reviews. Great choice!"
        elif positive_percentage < negative_percentage:
            return "Overall, the product has negative reviews. Proceed with caution!"
        else:
            return "Overall, the product has mixed reviews. It's a hit or miss!"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
