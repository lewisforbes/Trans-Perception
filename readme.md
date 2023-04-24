# Perception of Trans Women vs Trans Men on Twitter

This project collects tweets and compares the prevelence of discussion about trans women vs that of trans men. 

The Twitter API was used to query recent Tweets matching the following keywords:
- trans man/men
- transgender man/men
- trans woman/women
- transgender woman/women

This lead to the following summary of results:

| Gender      | Mentions in Tweets| Average Likes per Tweet | Average Retweets per Tweet |
| ----------- | ----------- | ------ | ------|
|Trans Man|19%|20|4.4|
| Trans Woman   |70%|11 | 1.5|

The raw data `raw_results.csv` is created with `main-scraper.py` and the full results `overview.txt` are created with `main-analyser.py`.
