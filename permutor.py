import argparse
import itertools

def concat_tuple(tup):
    return ''.join(tup)
    
def can_case(string):
    if string is None or len(string) < 1:
        return False
    return string[0].lower() != string[0].upper()

def first_letter_reversed(string):
    if string[0].lower() == string[0]:
        return '{}{}'.format(string[0].upper(), string[1:])
    else:
        return '{}{}'.format(string[0].lower(), string[1:])
        
def capitalization_combos(wordlist):
    wordlists = []
    wordlists.append(wordlist)
    
    n = len(wordlist)
    
    for i in range(n):
        new_list = []
        for current_list in wordlists:
            if can_case(current_list[i]):
                tmp = list(current_list) # make a copy
                tmp[i] = first_letter_reversed(current_list[i])
                new_list.append(tmp)
        wordlists += new_list
    
    return wordlists
    
def letter_substitutions(wordlist):
    wordlists = []
    wordlists.append(wordlist)
    
    n = len(wordlist)
    
    for i in range(n):
        new_list = []
        for current_list in wordlists:
            if can_case(current_list[i]):
                tmp = list(current_list) # make a copy
                tmp[i] = first_letter_reversed(current_list[i])
                new_list.append(tmp)
        wordlists += new_list
    
    return wordlists
    
def swap_letters_for_symbols(word):
    replacements = {
        'e': '3', 'E': '3',
        'a': '@', 'A': '@',
        'i': '!', 'I': '!',
        's': '$', 'S': '$',
        'i': '1', 'L': '1',
        'o': '0', 'O': '0'
    }
    
    words = set([word])
    for idx, char in enumerate(list(word)):
        if char in replacements:
            new_words = set()
            for w in words:
                mutated = w[:idx] + replacements[char] + w[(idx + 1):]
                new_words.add(mutated)
            words = words.union(new_words)
    
    return words
    
def powerset(iterable):
    s = list(iterable)
    x = itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))
    return [y for y in list(x) if y is not (())] # remove the empty tuple
    
def base_wordlist(words):
    base_words = list(set(words))
    combos = capitalization_combos(base_words)
    combos = list(map(powerset, combos))
    combos = list(set([item for sublist in combos for item in sublist]))
    return list(map(concat_tuple, combos))

def main(arg_words, digits=2, no_special=False, no_subs=False):
    words = base_wordlist(arg_words)
    
    if no_special is False:
        # append hashtag
        words += list(map(lambda x: '#{}'.format(x), words))
        
    if digits > 0:
        # append numbers
        numbered_words = []
        for num in range(10 ** digits):
            numbered_words += list(map(lambda x: '{}{}'.format(x, num), words))
        words += numbered_words
    
    if no_special is False:
        # append exclamation
        words += list(map(lambda x: '{}!'.format(x), words))
    
    words = set(words)
    
    if no_subs is False:
        more_words = set()
        for w in words:
            more_words = more_words.union(swap_letters_for_symbols(w))
        words = words.union(more_words)
        
    for w in words:
        print(w)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate potential passwords from a given word or list of words')
    parser.add_argument('words', metavar='WORDS', nargs='+', help='words used to generate passwords')
    parser.add_argument('-n', '--digits', type=int, default=2,
        help='maximum number of digits at the end of a password')
    parser.add_argument('-nS', '--no-special', default=False, action='store_true',
        help='do not include permutations with `#` at the beginning and `!` at the end')
    parser.add_argument('-nL', '--no-substitutions', default=False, action='store_true',
        help='do not include common letter substitutions, for example `@` for `a`')
    
    args = parser.parse_args()
    arg_words = args.words  
    digits = args.digits
    no_special = args.no_special
    no_subs = args.no_substitutions
    
    main(arg_words, digits, no_special, no_subs)
