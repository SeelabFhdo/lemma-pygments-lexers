"""A Pygments lexer for Xtend."""
from pygments.lexer import RegexLexer, words
from pygments.lexers.jvm import JavaLexer
from pygments.token import *

import re

__all__ = ("XtendLexer")

class XtendLexer(RegexLexer):
    name = 'Xtend'
    aliases = ['lemmaxtend']
    filenames = ['*.xtend']
    mimetypes = ['text/lemmaxtend']
    
    flags = re.MULTILINE | re.DOTALL | re.UNICODE

    tokens = JavaLexer.tokens
    xtendKeywords = {
        'def',
        'false',
        'null',
        'true',
        'val'
    }

    def get_tokens_unprocessed(self, text):
        for index, token, value in JavaLexer.get_tokens_unprocessed(self, text):
            if value in self.xtendKeywords:
                yield index, Keyword, value
            elif token is Name.Attribute:
                yield index, Name.Builtin.Pseudo, value
            else:
                yield index, token, value
