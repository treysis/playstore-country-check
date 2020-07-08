# playstore-country-check 0.2
This python script checks all localized versions of Google's PlayStore for the availability of a specific app. Sample code uses the German Corona-Warn-App for COVID-19 Contact Tracing with package name de.rki.coronawarnapp.

Relies on `requests` and `BeautifulSoup4`:

```
pip install requests
pip install beautifulsoup4
```

List with country codes modified from https://github.com/danieliu/play-scraper.

#### Usage:
```
python playstore-country-check.py <app.package.name>
```

## ToDo:

- lots of error/exception handling
- make country lists configurable by cmdline switches
- modularize/classify
- translation of country names (by scraping from PlayStore!)
- ~~maybe modify scraping method~~ done!

## Changelog:

##### 0.2

- changed scraping method (only checking release date was unreliable)

##### 0.11

- specify PlayStore package name in command line argument, default is `de.rki.coronawarnapp`
- added live feedback to progress indicator
- added reduced lists of countries (default: Europe only, comment/uncomment for different lists)
- added `requirements.txt`

##### 0.1

- Initial release

