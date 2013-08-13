
import random
import re

from app import data


def get_random_one(alist):
	return alist[random.randint(0,len(alist)-1)]


def get_random_one_or_not(alist):
	if random.randint(0,1) == 1:
		return get_random_one(alist)
	else:
		return ""


def get_random_some(alist, amount):
	list_results = []
	for i in xrange(amount):
		if len(list_results) == len(alist):
			return " ".join(list_results)
		while True:
			result = get_random_one(alist)
			if result not in list_results:
				break
		list_results.append(result)
	return list_results


def get_random_some_joined(alist, amount):
	return " ".join(get_random_some(alist, amount))


def generate_first_question():
	return get_random_one(data.first_questions)


def generate_middle_question():
	return get_random_one(data.middle_questions)


def generate_last_questions():
	return get_random_some_joined(data.last_questions, random.randint(1,3))


def generate_first_ofence():
	return get_random_one(data.first_ofenses)


def generate_first_sentence(subject):
	content = {
		'subject': subject,
		'object': get_random_one(data.generic_singular_objects)
	}
	return "The %(subject)s is %(object)s." % content


def generate_second_sentence(subject):
	content = {
		'starter': get_random_one(data.second_sentence_starters),
		'adjectives': get_random_some_joined(data.generic_adjectives, random.randint(0,2)),
		'subject': subject,
		'subject_descriptor': get_random_one_or_not(data.generic_subject_descriptors),
		'verb': get_random_one(data.generic_singular_verbs),
		'object': get_random_one(data.generic_singular_objects),
		'punctuation': "!" if random.randint(1,3)==1 else ".",
	}
	sentence = "%(starter)s the %(adjectives)s %(subject)s " \
			   "%(subject_descriptor)s %(verb)s %(object)s%(punctuation)s" \
			   % content
	sentence = re.sub(r"  +", " ", sentence) # remove redundant spaces
	return sentence


def generate_conector_sentence(subject):
	content = {
		'like': get_random_one(data.generic_comparisons),
		'subject': subject,
	}
	sentence = "%(like)s %(subject)s." % content
	# Fix bug: sentences should always start with uppercase. %(like)s can be a sentence
	pattern = re.compile(r'(?<=(\?|\.|\!)\s)(?P<thechar>\w)', re.M)
	def repl_upper(m):
		return "%s" % m.group('thechar').upper()
	if pattern.search(sentence) is not None:
		sentence = pattern.sub(repl_upper, sentence)
	return sentence


def generate_confusing_sentence(subject):
	content = {
		'subject': subject,
		'adjective': get_random_one(data.weird_adjectives),
	}
	sentence_format = get_random_one(data.confusing_sentence_formats)
	sentence = sentence_format % content
	sentence = sentence[0].upper() + sentence[1:] # uppercase first letter
	return sentence


def generate_after_confusion_sentence():
	return get_random_one(data.after_confusion_sentences)


def generate_text(subject=None):
	subjects = get_random_some(data.generic_singular_subjects, 2)
	subject1 = subjects[0] if subject is None else subject
	subject2 = subjects[1]
	content = {
		'question1': generate_first_question(),
		'ofense': generate_first_ofence(),
		'sentence1': generate_first_sentence(subject1),
		'sentence2': generate_second_sentence(subject1),
		'sentence3': generate_conector_sentence(subject2),
		'sentence4': generate_confusing_sentence(subject2),
		'question2': generate_middle_question(),
		'sentence5': generate_after_confusion_sentence(),
		'sentence6': generate_first_sentence(subject2),
		'question3': generate_last_questions(),
	}
	return "%(question1)s %(ofense)s " \
		   "%(sentence1)s %(sentence2)s " \
		   "%(sentence3)s %(sentence4)s " \
		   "%(question2)s %(sentence5)s " \
		   "%(sentence6)s %(question3)s" % content


