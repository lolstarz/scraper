import requests
import logging
import urllib.parse
from bs4 import BeautifulSoup

logger = logging.getLogger('debug')
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

def scrape_url_for_images(url):
    """
    Given a url, return links to all the images
    used on the page along with the alt text if
    present.

    :param url: URL to scrape
    :return: The images and alt text (if present) of the page
    """
    page_content = scrape_url(url)
    soup = BeautifulSoup(page_content, 'html.parser')
    results = ""
    for img in soup.find_all('img'):
        if img.get('src'):
            results += img.get('src')
            if img.string:
                results += img.string

            results += '\n'

    return results

def scrape_url_for_links(url):
    """
    Given a url, return all the links
    This will return links denoted by <a href="..."> tags

    :param url: URL to scrape
    :return: The links of the page
    """
    soup = scrape_url(url)
    results = ""
    for link in soup.find_all('a'):
        if link.get('href'):
            if link.string:
                results += link.string + ": " + link.get('href') + '\n'
            else:
                results += link.get('href') + '\n'

    return results

def scrape_url_for_text(url):
    """
    Given a url, return all the text content
    This will be all the content between html <tags>

    :param url: URL to scrape
    :return: The text of the page
    """
    soup = scrape_url(url)
    for script in soup(["script","style"]):
            script.extract()

    output = soup.get_text()
    result = ""
    newline = False
    for line in output:
        if (line != '\n' and line != '\r'):
            if(not newline or line != ' '):
                result += line
                newline = False
        else:
            if not newline:
                result += line
                newline = True

    return result

def formatted_html(url):
    return scrape_url(url).prettify()

def scrape_url(url):
    """
    Given a url, return the as a collection of HTML elements

    :param url: URL to scrape
    :return: The HTML comprising the page
    """

    try:
        page = requests.get(url)
    except requests.exceptions.HTTPError as e:
        logger.debug(e)

    return BeautifulSoup(page.content, 'html.parser')

def decode_url(url):
    """
    Takes a url which has been encoded with percent encoding and
    returns the unencoded form

    :param url: An encoded URL
    :return: The original URL
    """
    return urllib.parse.unquote(url)
