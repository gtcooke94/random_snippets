"""Say you have a set of urls and you want to sort them just during a debug
log. Doing the sorted(urls) inside of logging.debug will sort the urls
regardless of whether or not logging.debug is actually needed. This is a
problem, how do you get around it?
"""

import logging

urls = {"google.com", "facebook.com", "apple.com", "netflix.com", "hulu.com",
        "reddit.com"}
logging.debug("Found urls: {}".format(sorted(urls)))



###############################################################################
""" Answer, lazily sort the urls """
class LazySort:
    def __init__(self, to_sort):
        self.to_sort = to_sort
    
    def __str__(self):
        return str(sorted(to_sort))

logging.debug("Found urls: {}".format(LazySort(urls)))


###############################################################################
""" An even more generalized answer """
class DelayDebugProcessing:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    
    def __str__(self):
        return str(self.func(*self.args, **self.kwargs))

logging.debug("Found urls: {}".format(DelayDebugProcessing(urls)))
