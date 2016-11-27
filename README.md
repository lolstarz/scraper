A basic webscraping application.

Build the docker container:

docker build -t 'scraper' .

Then run it:

docker run -d scraper

Check 127.0.0.1/www.testurl.com to verify that it works. Note that URLs cannot contain http://.
