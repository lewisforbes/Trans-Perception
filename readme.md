# Discussion of Trans Women vs Trans Men on Twitter

This project collects tweets and compares the prevelence of discussion about trans women vs that of trans men. 

**Content warning**: the tweets in [`raw_results.csv`](/raw_results.csv) are unmoderated and many are transphobic.

The Twitter API was used to query recent Tweets matching the following keywords:
- trans man/men
- transgender man/men
- trans woman/women
- transgender woman/women

A Tweet was classified (case-insensitively) as...
- ...*M* if it contained any of the first two queries, as well as "transman"* or "transmen"*.
- ...*F* if it contained any of the final two queries, as well as "transwoman"* or "transwomen"*.
- ...*Both* if it could be classified as both *M* and *F*.
- ...*None* if it could be classified as neither *M* or *F*.

This led to the following summary of results from the 34478 Tweets pulled:

| Gender      | Mentions in Tweets| Average Likes per Tweet | Average Retweets per Tweet |
| ----------- | ----------- | ------ | ------|
|Men|19%|20|4.4|
| Women   |70%|11 | 1.5|

The raw data [`raw_results.csv`](/raw_results.csv) is created with [`main-scraper.py`](/main-scraper.py) and the full results [`overview.txt`](/overview.txt) are created with [`main-analyser.py`](/main-analyser.py).

*These terms [should not be used](https://www.glaad.org/reference/trans-terms). 'Trans' is an adjective which can modify a gender - using 'trans(wo)man' can imply that trans (wo)men are not (wo)men. 
