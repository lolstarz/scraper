import requests
import logging
import urllib.parse
from lxml import html

logger = logging.getLogger('debug')
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

def scrape_url(url):
    """
    Given a url, return the as a collection of HTML elements

    :param url: URL to scrape
    :return: The tree of HTML elements comprising the page
    """

    try:
        page = requests.get(url)
    except requests.exceptions.HTTPError as e:
        logger.debug(e)

    print(page.content)
    tree = html.fromstring(page.content)

    return page.content

def decode_url(url):
    """
    Takes a url which has been encoded with percent encoding and
    returns the unencoded form

    :param url: An encoded URL
    :return: The original URL
    """
    return urllib.parse.unquote(url)
