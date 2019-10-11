# Bonus 1 - just reverse attributes. Last item updated in a dict takes precedence, so by reversing the dict we ensure the first instance of an attribute/value pair is the value that sticks
def parse_tag(html_tag):
    """Return tuple of tag name and sorted attributes."""
    tag_name, *attr_strings = html_tag[1:-1].lower().split()
    attributes = dict(
        attr.split('=')
        for attr in reversed(attr_strings)
    )
    return tag_name, attributes

################################################################################
# Bonus 2 - smarter parsing for if there isn't an equal
def parse_attributes(strings):
    """Return key-value attribute pairs, ignoring duplicates."""
    return (
        (a.split('=') if '=' in a else [a, None])
        for a in reversed(strings)
    )

# OR USE PARTITION
def parse_attributes(strings):
    """Return key-value attribute pairs, ignoring duplicates."""
    partitions = (
        a.partition('=')
        for a in reversed(strings)
    )
    return ((key, value) for key, _, value in partitions)

def parse_tag(html_tag):
    """Return tuple of tag name and sorted attributes."""
    tag_name, *attr_strings = html_tag[1:-1].lower().split()
    attributes = dict(parse_attributes(attr_strings))
    return tag_name, attributes

################################################################################
# Bonus 3
# First option use shlex, in standard library. Quote aware string splitting
"""
In [26]: a = "Hello this 'is a' test"

In [27]: a.split(" ")
Out[27]: ['Hello', 'this', "'is", "a'", 'test']

In [28]: shlex.split(a)
Out[28]: ['Hello', 'this', 'is a', 'test']
"""
import shlex

def parse_attributes(strings):
    """Return key-value attribute pairs, ignoring duplicates."""
    return (
        (a.split('=') if '=' in a else [a, None])
        for a in reversed(strings)
    )

def parse_tag(html_tag):
    """Return tuple of tag name and sorted attributes."""
    tag_name, *attr_strings = shlex.split(html_tag[1:-1].lower())
    return tag_name, dict(parse_attributes(attr_strings))

# Second option - use html.parser's HTMLParser from standard library. It has a handle_starttag function that gets called on the opening tag. This is hacky, worse than shlex
from html.parser import HTMLParser

class TagParser(HTMLParser):
    def handle_starttag(self, tag, attr_pairs):
        """Return tuple of tag and attr dict, ignoring duplicates."""
        self.value = (tag, dict(reversed(attr_pairs)))

def parse_tag(html_tag):
    """Return tuple of tag name and sorted attributes."""
    parser = TagParser()
    parser.feed(html_tag)
    return parser.value
