# Word Pair Problem

## The Basics

* Given a list of words, find a pair with the highest score.
* The score is determined by multiplying the lengths of the words by one another.
* For instance:
	`[Spoke, Branch] = 30`
    `5   *   6    = 30`

* With the exception that if the words share any letters in common then the pair's score is zero.
* For instance, the following pair yields a score of 0 because both words contain the letter 'r' :

	`[Shrink, Branch] = 0`

## Some Details

* Your method should return a single pair of words.
* In the event that multiple pairs tie for the highest score...
    - Any of these pairs is an acceptable answer
    - Pick one and only one, don't return a list of pairs
* Zero, while the lowest possible score, is a valid score



### Python project creation:
    
    #### Ccreate project dir
    `mkdir $PYTHON_WORKSPACE/problem`

    #### Create virtualenv for project
    `mkvirtualenv -p python2.7 -a $PYTHON_WORKSPACE/problem problem`

    #### Activate virtualenv workspace
    `workon problem`

    #### Stop working in virtualenv workspace
    `deactivate`

    #### Installing modules
    `pip install -r requirements.txt`


#### Procuring a list of words from the internets

    1. get the list of words (assuming you already found a source from github or google):

    `curl ![alt text](https://raw.githubusercontent.com/sindresorhus/word-list/master/words.txt "github link to word list") > words.txt`

    2. the list is in alphabetical order so we need to shuffle it:

    `perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' < words.txt  > words_shuf.txt`

    3. there were 274925 words in the downloaded list - we need 110k of those:

    `tail -110000  words_shuf.txt  > words_shuf_110k.txt`


    * We end up with the file 'words_shuf_110k.txt' which is unsorted and  comprised of 110k words.

    * We can now use resultant file as the seed file for our program.