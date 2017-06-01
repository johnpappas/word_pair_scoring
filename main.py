#!/usr/bin/env python2.7


"""
	Main() function to execute code for get_highest_scoring_pair()
	function residing in word_utils module
	Filename read from arg passed via CLI
"""

import sys
from word_utils import read_file_to_list, sort_list_by_length, get_highest_scoring_pair

# read filename from stdin (either 'words_en.txt' or 'words_shuf_110k.txt')
word_file = sys.argv[1]


def main():
	unsorted_list = read_file_to_list(word_file=word_file)
	count = len(unsorted_list)
	sorted_list1 = sort_list_by_length(unsorted_list)
	sorted_list2 = sort_list_by_length(unsorted_list)

	# debugging stmnt to find trailing carriage-returns in words-en.txt sample
	# print 'sorted_list (by len): list={slist}'.format(slist=sorted_list1)

	print 'Heya check it out: number of words in list = {count}'.format(count=count)

	print get_highest_scoring_pair(sorted_list1, sorted_list2, count)


if __name__ == '__main__':
	main()
