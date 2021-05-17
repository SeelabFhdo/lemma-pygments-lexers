"""A Pygments lexer for LEMMA's Domain Data Modeling Language."""
from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import *

__all__ = ("LemmaDomainDataLexer")

class LemmaDomainDataLexer(RegexLexer):
    name = 'LEMMA Domain Data Modeling Language'
    aliases = ['lemmadomaindata']
    filenames = ['*.data']
    mimetypes = ['text/lemmadomaindata']

    tokens = {
        'root': [
            (words((
                'context',
                'double',
                'hide',
                'immutable',
                'string',
                'list',
                'structure',
                'unspecified'
            ), prefix=r'\b', suffix=r'\b'), Keyword),
            (r'(true|false)\b', Keyword.Constant),
            (r'(<)(\w+)(>)', bygroups(Text, Name.Builtin.Pseudo, Text)),
            (r'\".*?\"', String)
        ]
    }
