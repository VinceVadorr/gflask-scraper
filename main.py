from flask import Flask, request, jsonify
from scraper import scrape_google

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def api_scrape():
    data = request.get_json()
    url = data['url']
    result = scrape_google(url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

# curl -X POST -H "Content-Type: application/json" -d '{"url":"https://www.google.fr/search?q=fermob;ie=utf-8&amp;oe=utf-8&amp;num=10"}' http://localhost:5000/scrape