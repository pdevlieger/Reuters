# Reuters
- - - 

Some newspaper article data processing, mainly to learn to deal with datetime data in python, analyze textual data and use pandas. The files contain articles which are identified between <REUTERS>...</REUTERS> tags. In between these tags, different tags identify differnt parts of the article (e.g. body, place, date, etc.)

## reut.py

This file focuses on extracting the data and organizing it in a list of dictionnaries.
* extract_id(string): takes the 'dirty' string as input. The index and ord function are combined to get the numbers between the <NEWID>...</NEWID> tags.

* structure_time_date(string): returns structured data for the date. Some slicing needs to be applied because one day in the dataset had a bunch of comments that didn't fit the general structure.

* extract_text_between_tags(tag_word, string): an easier, general function that allows to loop over the different article components.

* get_article_components(raw_string): loops over extract_text_between_tags for the different article components

## ds.py

This file uses the actual data and provides some simple descriptive graphs (other codes not uploaded).

The first (set of) graphs give a quick overview of the length of the body (in characters) and how this changes over the course of a month, a year and a day. For the monthly graph, we see that there is a spike around day 15, 22 and 28. For the yearly graph, it shows the data is mostly centered between days 50 and 120 of the year and portrays some seasonality. The daily graph shows that articles during the day are shorter than graphs that are posted in the morning or evening (probably because these could be mainly updates).

![Body length](https://raw.github.com/uctpphd/Reuters/master/body_length.png)

A word count in the different articles. The word that was searched for is "crisis".

![Word count ("crisis)](https://raw.github.com/uctpphd/Reuters/master/word_count.png)

## lessons learned

This data didn't really provide great insights, but many lessons learned. I was used to datasets that were analyzed using numbers, and performing analyses on textual data was something interesting, but required some different thinking here and there.

[Source of sgm-files](http://www.daviddlewis.com/resources/testcollections/reuters21578/)
