# coding: utf-8
import copy

def to_unicode(text, encoding):
    """
    Return a unicode from any import string format.

    Keyword arguments:
    text -- Original source that will be transformed.
    encoding -- Encode used to transform to unicode. 
    """
    pass

def to_list(text, encoding=None):
    """
    Returns a unicode list from a text.


    Keyword arguments:
    text -- Text in string or unicode format.
    encoding -- Encode to be used in string case (default None).
    """
    result = copy.copy(text)
    if type(text) is str:
        result = text.encode(encoding)
    if type(result) is unicode:
        result = result.split()
    if type(result) not is list:
        raise Exception('Text need to be string or unicode.')
    return result
