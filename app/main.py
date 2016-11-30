from flask import Flask
from flask import render_template
import scraper

app = Flask(__name__)

@app.route("/")
def landing():
    return "Welcome to Scraper! (pony)"

@app.route("/links/<path:url>")
def alllinks(url):
    content = scraper.scrape_url_for_links("http://" + scraper.decode_url(url))
    return render_template("content.html",
                            content=content)

@app.route("/text/<path:url>")
def alltext(url):
    content = scraper.scrape_url_for_text("http://" + scraper.decode_url(url))
    return render_template("content.html",
                            content=content)

@app.route("/<path:url>", methods=['GET'])
def fulltake(url):
    content = scraper.scrape_url("http://" + scraper.decode_url(url))
    return render_template("content.html",
                            content=content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
