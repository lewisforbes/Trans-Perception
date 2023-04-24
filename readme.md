# Discussion of Trans Women vs Trans Men on Twitter

This project collects tweets and compares the prevelence of discussion about trans women vs that of trans men. 

**Content warning**: the tweets in `raw_results.csv` are unmoderated and many are transphobic.

The Twitter API was used to query recent Tweets matching the following keywords:
- trans man/men
- transgender man/men
- trans woman/women
- transgender woman/women

This led to the following summary of results from the 34478 Tweets pulled:

| Gender      | Mentions in Tweets| Average Likes per Tweet | Average Retweets per Tweet |
| ----------- | ----------- | ------ | ------|
|Men|19%|20|4.4|
| Women   |70%|11 | 1.5|

The raw data `raw_results.csv` is created with `main-scraper.py` and the full results `overview.txt` are created with `main-analyser.py`.
