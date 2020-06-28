def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')#用空格对stuff中的字符串进行分割，并存储words列表中
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)#对单词排序

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)#获得第一个单词
    print(word)

def print_last_word(words):
    """Prints the last word after popping it of."""
    word = words.pop(-1)#获得最后一个单词
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return (sort_words(words))

def print_first_and_last(sentence):
    """Prints the first and last words of a sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)