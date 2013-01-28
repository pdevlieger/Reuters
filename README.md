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

![alt text][logo]
[logo]: https://github.com/uctpphd/Reuters/blob/master/word_count.png "Word count (for 'crisis')"
![alt text][logo]
[logo]: https://github.com/uctpphd/Reuters/blob/master/body_length.png "Body lenght (for different timings)"


[Source of sgm-files](http://www.daviddlewis.com/resources/testcollections/reuters21578/)
