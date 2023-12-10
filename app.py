from flask import Flask, jsonify, request
from recipe_scrapers import scrape_me

app = Flask(__name__)

@app.route('/api/scrape', methods=['GET', 'POST'])
def scrape():
    response = {}
    try:
        url:str = request.args.get('url')
        scraper = scrape_me(url)
        response = scraper.to_json()
    except Exception as e:
        print(f'Exception: {e}')
        response['error'] = str(e)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)