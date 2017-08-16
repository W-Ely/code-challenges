"""Leetcode 126. Word Ladder II."""


class Solution(object):
    """Solution object."""

    def findLadders(self, beginWord, endWord, wordList):
        """Find shortest paths.

        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        graph = Graph()
        graph.add_node(beginWord)
        for word in wordList:
            graph.add_node(word)
            for node in graph.nodes():
                count = 0
                for i, letter in enumerate(word):
                    if letter is not node[i]:
                        count += 1
                if count == 1:
                    graph.add_edges(word, node)
        paths = graph.find_paths(beginWord, endWord)
        if paths:
            length = min((len(path) for path in paths))
        return [path for path in paths if len(path) == length]


class Graph(dict):
    """Create a graph data strcture modeled off a dictionary."""

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self.keys())

    def add_node(self, val):
        """Add a new node with value 'val' to the graph."""
        if val not in self:
            self.setdefault(val, [])

    def add_edges(self, val1, val2):
        """Add a new edge to the graph."""
        self.setdefault(val1, [])
        self.setdefault(val2, [])
        if val2 not in self[val1]:
            self[val1].append(val2)
        if val1 not in self[val2]:
            self[val2].append(val1)

    def find_paths(self,  start_val, end_val):
        """Find paths."""
        queue = [(start_val, set([start_val]), [start_val])]
        holding = []
        shortest = False
        paths = []
        while not shortest and queue:
            while queue:
                node, ref, path = queue.pop()
                for val in [x for x in self[node] if x not in ref]:
                    if val == end_val:
                        shortest = True
                        paths.append(path + [val])
                    else:
                        ref.add(val)
                        holding.append((val, ref, path + [val]))
            queue, holding = holding[::-1], []
        return paths


find = Solution()
beginWord = "cet"
endWord = "ism"
wordList = [
    "kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay",
    "sip", "kay", "per", "val", "mes", "ohs", "now", "boa", "cet", "pal",
    "bar", "die", "war", "hay", "eco", "pub", "lob", "rue", "fry", "lit",
    "rex", "jan", "cot", "bid", "ali", "pay", "col", "gum", "ger", "row",
    "won", "dan", "rum", "fad", "tut", "sag", "yip", "sui", "ark", "has",
    "zip", "fez", "own", "ump", "dis", "ads", "max", "jaw", "out", "btu",
    "ana", "gap", "cry", "led", "abe", "box", "ore", "pig", "fie", "toy",
    "fat", "cal", "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply",
    "awe", "pry", "tit", "tie", "yet", "too", "tax", "jim", "san", "pan",
    "map", "ski", "ova", "wed", "non", "wac", "nut", "why", "bye", "lye",
    "oct", "old", "fin", "feb", "chi", "sap", "owl", "log", "tod", "dot",
    "bow", "fob", "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib",
    "mel", "hus", "sob", "ifs", "tab", "ara", "dab", "jag", "jar", "arm",
    "lot", "tom", "sax", "tex", "yum", "pei", "wen", "wry", "ire", "irk",
    "far", "mew", "wit", "doe", "gas", "rte", "ian", "pot", "ask", "wag",
    "hag", "amy", "nag", "ron", "soy", "gin", "don", "tug", "fay", "vic",
    "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen", "paw", "his",
    "sub", "bob", "yea", "oft", "inn", "rod", "yam", "pew", "web", "hod",
    "hun", "gyp", "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib",
    "rub", "ere", "dig", "era", "cat", "fox", "bee", "mod", "day", "apr",
    "vie", "nev", "jam", "pam", "new", "aye", "ani", "and", "ibm", "yap",
    "can", "pyx", "tar", "kin", "fog", "hum", "pip", "cup", "dye", "lyx",
    "jog", "nun", "par", "wan", "fey", "bus", "oak", "bad", "ats", "set",
    "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six", "ila", "lao",
    "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap",
    "lop", "may", "shy", "rid", "bat", "sum", "rim", "fee", "bmw", "sky",
    "maj", "hue", "thy", "ava", "rap", "den", "fla", "auk", "cox", "ibo",
    "hey", "saw", "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva",
    "tog", "ram", "let", "see", "zit", "maw", "nix", "ate", "gig", "rep",
    "owe", "ind", "hog", "eve", "sam", "zoo", "any", "dow", "cod", "bed",
    "vet", "ham", "sis", "hex", "via", "fir", "nod", "mao", "aug", "mum",
    "hoe", "bah", "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem",
    "who", "bet", "gos", "son", "ear", "spy", "kit", "boy", "due", "sen",
    "oaf", "mix", "hep", "fur", "ada", "bin", "nil", "mia", "ewe", "hit",
    "fix", "sad", "rib", "eye", "hop", "haw", "wax", "mid", "tad", "ken",
    "wad", "rye", "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin",
    "mad", "ray", "hon", "roy", "dip", "hen", "iva", "lug", "asp", "hui",
    "yak", "bay", "poi", "yep", "bun", "try", "lad", "elm", "nat", "wyo",
    "gym", "dug", "toe", "dee", "wig", "sly", "rip", "geo", "cog", "pas",
    "zen", "odd", "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio",
    "yon", "dec", "leg", "put", "sue", "dim", "pet", "yaw", "nub", "bit",
    "bur", "sid", "sun", "oil", "red", "doc", "moe", "caw", "eel", "dix",
    "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid",
    "pun", "ton", "sol", "din", "yup", "jab", "pea", "bug", "gag", "mil",
    "jig", "hub", "low", "did", "tin", "get", "gte", "sox", "lei", "mig",
    "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir", "sty",
    "lap", "two", "ins", "con", "ant", "net", "tux", "ode", "stu", "mug",
    "cad", "nap", "gun", "fop", "tot", "sow", "sal", "sic", "ted", "wot",
    "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism",
    "err", "him", "all", "pad", "hah", "hie", "aim", "ike", "jed", "ego",
    "mac", "baa", "min", "com", "ill", "was", "cab", "ago", "ina", "big",
    "ilk", "gal", "tap", "duh", "ola", "ran", "lab", "top", "gob", "hot",
    "ora", "tia", "kip", "han", "met", "hut", "she", "sac", "fed", "goo",
    "tee", "ell", "not", "act", "gil", "rut", "ala", "ape", "rig", "cid",
    "god", "duo", "lin", "aid", "gel", "awl", "lag", "elf", "liz", "ref",
    "aha", "fib", "oho", "tho", "her", "nor", "ace", "adz", "fun", "ned",
    "coo", "win", "tao", "coy", "van", "man", "pit", "guy", "foe", "hid",
    "mai", "sup", "jay", "hob", "mow", "jot", "are", "pol", "arc", "lax",
    "aft", "alb", "len", "air", "pug", "pox", "vow", "got", "meg", "zoe",
    "amp", "ale", "bud", "gee", "pin", "dun", "pat", "ten", "mob"
]
print(find.findLadders(beginWord, endWord, wordList))
