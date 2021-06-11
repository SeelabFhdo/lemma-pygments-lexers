"""A Pygments lexer for LEMMA's Operation Modeling Language."""
from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import *

__all__ = ("LemmaOperationLexer")

class LemmaOperationLexer(RegexLexer):
    name = 'LEMMA Operation Modeling Language'
    aliases = ['lemmaoperation']
    filenames = ['*.operation']
    mimetypes = ['text/lemmaoperation']

    tokens = {
        'root': [
            (words((
                'as',
                'basic endpoints',
                'container',
                'default values',
                'deployment technology',
                'deploys',
                'from',
                'import',
                'microservices',
                'technology'
            ), prefix=r'\b', suffix=r'\b'), Keyword),
            (r'@\w+((::_)\w+\.\w+)?', Name.Builtin.Pseudo),
            (r'(true|false)\b', Keyword.Constant),
            (r'\".*?\"', String)
        ]
    }
