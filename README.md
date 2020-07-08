# playstore-country-check 0.11
This python script checks all localized versions of Google's PlayStore for the availability of a specific app. Sample code uses the German Corona-Warn-App for COVID-19 Contact Tracing with package name de.rki.coronawarnapp.

Relies on https://github.com/JoMingyu/google-play-scraper:

```
pip install google-play-scraper
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
- maybe modify scraping method

## Changelog:

##### 0.11

- specify PlayStore package name in command line argument, default is `de.rki.coronawarnapp`
- added live feedback to progress indicator
- added reduced lists of countries (default: Europe only, comment/uncomment for different lists)
- added `requirements.txt`

##### 0.1

- Initial release
