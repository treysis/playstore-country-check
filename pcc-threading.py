# playstore-country-check - testversion - by treysis / https://github.com/treysis
# License: LGPL 2.1
#
# Checks the availability of apps in local variants of Google's PlayStore.
#
# Relies on google-play-scraper (https://github.com/JoMingyu/google-play-scraper),
# install with:
#     pip install google-play-scraper
#
# --- DEPRECATED --- for testing or learning ;)

try:
    from google_play_scraper import app
except ImportError as error:
    print("Error: error while loading 'google-play-scraper'! Install with 'pip install google-play-scraper' and try again.")
    exit()

from sys import stdout
from multiprocessing.dummy import Pool
from itertools import product

# Initialize country codes and names
GL_CC = {
    "ad": "Andorra",
    "at": "Austria",
    "gd": "Grenada",
    "ge": "Georgia",
    "gf": "French Guiana",
    "gg": "Guernsey",
    "gh": "Ghana",
    "gi": "Gibraltar",
    "gl": "Greenland",
    "gm": "The Gambia",
    "gn": "Guinea",
    "gp": "Guadeloupe",
    "gq": "Equatorial Guinea",
    "gr": "Greece",
    "gs": "South Georgia and the South Sandwich Islands",
    "gt": "Guatemala",
    "gu": "Guam",
    "gw": "Guinea-Bissau",
    "gy": "Guyana",
    "hk": "Hong Kong",
    "hm": "Heard Island and McDonald Islands",
    "hn": "Honduras",
    "hr": "Croatia",
    "ht": "Haiti",
    "hu": "Hungary",
    "sk": "Slovakia",
    "sl": "Sierra Leone",
    "sm": "San Marino",
    "sn": "Senegal",
    "so": "Somalia",
    "sr": "Suriname",
    "ss": "South Sudan",
    "wf": "Wallis and Futuna",
    "ws": "Samoa",
    "xk": "Kosovo",
    "ye": "Yemen",
    "yt": "Mayotte",
    "za": "South Africa",
    "zm": "Zambia"
}

cwaa = list()
cwana = list()
delete = "\b" * 15


def crawl(a, k):
    # Progress indicator
    print("{0}{0}{1:{2}}".format(delete, len(cwaa)+len(cwana), 3), end=" of " + str(len(GL_CC)) + "... (current: " + k + ")")
    stdout.flush()
    #print(k, end = ',')
    # Request app data from google-play-scraper with country code. If available, "released" will
    # contain some release date. If not available in the selected country, this value is empty.
    if app(a, country=k)['released'] is not None:
        cwaa.append(GL_CC[k])
        print("{0}{0}{1:{2}}".format(delete, len(cwaa)+len(cwana), 3), end=" of " + str(len(GL_CC)) + "... (current: " + k + ")")
        stdout.flush()
    else:
        cwana.append(GL_CC[k])
        print("{0}{0}{1:{2}}".format(delete, len(cwaa)+len(cwana), 3), end=" of " + str(len(GL_CC)) + "... (current: " + k + ")")
        stdout.flush()

    return(k)


def main():

    print("--\nplaystore-country-check - testversion:\nChecking the enabled PlayStore countries for Germany's", \
            "Corona-Warn-App\n(package name: de.rki.coronawarnapp).")
    print("Sourcecode @ https://github.com/treysis/playstore-country-check\n\n")

    # Initialize variables.
    #cwaa = list()
    #cwana = list()
    #delete = "\b" * 15
    # Number of parallel threads. 10 seems safe to use for rate limiting.
    n_Psize = 10

    # Start checking
    print("Checking countries (using " + str(n_Psize) + " parallel threads):")
    #i=0
    pool = Pool(n_Psize)
    appname = ['de.rki.coronawarnapp']
    thread_result = pool.starmap(crawl, product(appname, list(GL_CC.keys())))
    print("...done!\n")
    print(thread_result)

    # Prepare and format output
    cwaa.sort()
    cwana.sort()
    print("App available in " + str(len(cwaa)) + " local PlayStores:")
    print(*cwaa, sep=", ", end=".\n")
    print("\nNot available in:")
    print(*cwana, sep=", ", end=".\n")
    print("\n--- Finished, exiting... ---")

    return

if __name__ == '__main__':
    main()
