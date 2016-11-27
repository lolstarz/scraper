from flask import Flask
from flask import render_template
import scraper

app = Flask(__name__)

@app.route("/<path:url>", methods=['GET'])
def hello(url):
    content = scraper.scrape_url("http://" + scraper.decode_url(url))
    return render_template("content.html",
                            content=content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
