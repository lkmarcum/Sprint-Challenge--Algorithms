'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# originally started writing this with an indexing variable to move through the string
# realized I'd either accidentally use loops with this method or it would get clunky keeping track of the index
# started over using slices to control what part of the string I'm evaluating -- much easier to follow


def count_th(word):
    # initialize counting variable to 0
    num_th = 0

    # base case if the length of the string is too short to contain 'th'
    if len(word) < 2:
        return num_th

    # if first two characters are 'th' then increment num_th
    # call count_th again with word minus first character and include num_th
    elif word[:2] == 'th':
        num_th += 1
        return count_th(word[1:]) + num_th

    # if no 'th' then just call count_th again with word minus first character
    else:
        return count_th(word[1:])


print(count_th("thmfngthams"))
