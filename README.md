# playstore-country-check
This python script/module checks all localized versions of Google's PlayStore for 
the availability of a specific app. Supports threading with a default of 10 
simultaneous threads (rate limit of Google probably much higher!). Sample 
code uses the German Corona-Warn-App for COVID-19 Contact Tracing with package 
name de.rki.coronawarnapp.

Relies on `requests` and `BeautifulSoup4`:

```
pip install requests
pip install beautifulsoup4
```

List with country codes modified from https://github.com/danieliu/play-scraper.

#### Usage:

As script (with 10 parallel threads):
```
python playstore_country_check.py <playstore.package.name>
```
As module:
```
import playstore_country_check

# Returns list of countries where app is available, default 10 threads
playstore_country_check.availability('playstore.package.name', threads=10)

# Returns True if available, False if not available, gl = 2 letter country code)
playstore_country_check.check('playstore.package.name', 'gl')
```

## ToDo:

- lots of error/exception handling
- make country lists configurable by cmdline switches
- make number of threads configurable when running as script
- modularize (work in progress!):
  - suppress output when running as module
  - and/or fix status messages when running as module
- classify?
- translation of country names (by scraping from PlayStore!)
- ~~maybe modify scraping method~~ done!

## Changelog:

##### 0.3

- implemented threading for faster results (default: 10 threads)
- implemented basic modularization

##### 0.2

- changed scraping method (only checking release date was unreliable)

##### 0.11

- specify PlayStore package name in command line argument, default is `de.rki.coronawarnapp`
- added live feedback to progress indicator
- added reduced lists of countries (default: Europe only, comment/uncomment for different lists)
- added `requirements.txt`

##### 0.1

- Initial release

