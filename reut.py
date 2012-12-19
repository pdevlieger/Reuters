from time import strptime

article_components = ['DATE', 'PLACES', 'DATELINE', 'TOPICS', 'PEOPLE', 'ORGS', 'EXCHANGES',
'COMPANIES', 'TITLE', 'BODY','HOUR']

files = ['reut2-000.sgm', 'reut2-001.sgm', 'reut2-002.sgm', 'reut2-003.sgm', 
'reut2-004.sgm', 'reut2-005.sgm', 'reut2-006.sgm', 'reut2-007.sgm', 'reut2-008.sgm',
'reut2-009.sgm', 'reut2-010.sgm', 'reut2-011.sgm', 'reut2-012.sgm', 'reut2-013.sgm',
'reut2-014.sgm', 'reut2-015.sgm', 'reut2-016.sgm', 'reut2-017.sgm', 'reut2-018.sgm',
'reut2-019.sgm', 'reut2-020.sgm', 'reut2-021.sgm']

def extract_text_between_tags(tag_word, string):
	try:
		start = string.index('<'+tag_word+'>') + 2 + len(tag_word)
		end = string.rindex('</'+tag_word+'>')
		if string[start:end] != "":
			return string[start:end]
		else:
			return None
	except ValueError:
		return None

def extract_id(string):
	try:
		start = string.index('NEWID="') + len('NEWID="')
		end = start + 1
		while 47 < ord(string[end]) < 58:
			end += 1
		return int(string[start:end])
	except ValueError:
		return None

def clean_string(string):
	return string.replace('\n', ' ')

def structure_time_date(string):
	# I need to slice of here because one day did on tidily report the date. 
	adjusted_string = string.strip()[:23]
	return strptime(adjusted_string, "%d-%b-%Y %H:%M:%S.%f")

def get_article_components(raw_string):
	article_data = dict((key, None) for key in article_components)
	article_string = clean_string(raw_string)
	
	for key in article_data:
		text = extract_text_between_tags(key, article_string)
		if text:
			if '<D>' and '</D>' in text:
				text = text.replace('<D>', '').replace('</D>', ' ').split()
		article_data[key] = text
	article_data['ID'] = extract_id(article_string)
	return article_data

def get_data():
	data = []
	for file in files:
		open_file = open(file).read().split('</REUTERS>')
		for raw_article in open_file:
			if '<REUTERS' in raw_article:
				article_components = get_article_components(raw_article)
				try:
					article_components['HOUR'] = structure_time_date(article_components['DATE']).tm_hour
					article_components['DAY_M'] = structure_time_date(article_components['DATE']).tm_mday
					article_components['DAY_Y'] = structure_time_date(article_components['DATE']).tm_yday
					article_components['MONTH'] = structure_time_date(article_components['DATE']).tm_mon
					article_components['YEAR'] = structure_time_date(article_components['DATE']).tm_year
				except:
					pass
				data.append(article_components)
	return data