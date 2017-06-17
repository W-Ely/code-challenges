"""String Pyramid kata

Blind4Basics

def watch_pyramid_from_the_side(characters):
    if not characters : return characters
    baseLen = len(characters)*2-1
    return '\n'.join( ' '*(i) + characters[i]*(baseLen-2*i) + ' '*(i) for i in range(len(characters)-1,-1,-1) )


def watch_pyramid_from_above(characters):
    if not characters : return characters
    baseLen = len(characters)*2-1
    return '\n'.join( characters[0:min(i,baseLen-1-i)] + characters[min(i,baseLen-1-i)]*(baseLen-2*min(i,baseLen-1-i)) + characters[0:min(i,baseLen-1-i)][::-1] for i in range(baseLen) )


def count_visible_characters_of_the_pyramid(characters):
    return -1 if not characters else (len(characters)*2-1)**2


def count_all_characters_of_the_pyramid(characters):
    return -1 if not characters else sum( (2*i+1)**2 for i in range(len(characters)) )

"""


def watch_pyramid_from_the_side(characters):
    if not characters:
        return characters
    side = ''
    for i, chr in enumerate(characters[::-1]):
        extra_spaces = (' ' * (len(characters) - (i + 1)))
        character_layer = chr * (2 * (i + 1) - 1)
        side += extra_spaces + character_layer + extra_spaces + '\n'
    return side[0:-1]


def watch_pyramid_from_above(characters):
    if not characters:
        return characters
    top = ''
    for i, chr in enumerate(characters[::-1]):
        char = chr * (i * 2 + 1)
        before = characters[::-1][i+1:][::-1]
        after = characters[::-1][i+1:]
        line = before + char + after
        if not top:
            top = line
        else:
            top = line + '\n' + top + '\n' + line
    return top


def count_visible_characters_of_the_pyramid(characters):
    if not characters:
        return -1
    return (len(characters) * 2 - 1) ** 2


def count_all_characters_of_the_pyramid(characters):
    if not characters:
        return -1
    if len(characters) == 1:
        return 1
    layer = (len(characters) * 2 - 1) ** 2
    return layer + count_all_characters_of_the_pyramid(characters[1:])
