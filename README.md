# Open-Source Javascript speed reading application

Python and Javascript [web application](http://reader-app.appspot.com/) to read text one word at a time.

(Obviously) inspired by upcoming [Spritz reader app](http://www.spritzinc.com/).

Currently running on [Google App Engine](http://reader-app.appspot.com/).

## URL Fetcher component uses Boilerpipe library

For now, this is done through the [web application](http://boilerpipe-web.appspot.com/).
Boilerpipe Removal and Fulltext Extraction
Background and documentation can be found [here](http://www.kohlschutter.com/).

## TODO:
1. Add rewind button (to beginning of last sentence)
 - Change pause so it blanks screen instead of stopping on last word
 - Figure out way to differentiate sentence-ends from periods
 - Half pause on commas/semi-colons
2. Experiment with different interfaces, e.g. trail of previous and upcoming words
