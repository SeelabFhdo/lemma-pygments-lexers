"""A Pygments lexer for LEMMA's Service Modeling Language."""
from pygments.lexer import RegexLexer, bygroups, include, words
from pygments.token import *
from . import PRIMITIVE_TYPE_TOKENS

__all__ = ("LemmaServicesLexer")

class LemmaServicesLexer(RegexLexer):
    name = 'LEMMA Service Modeling Language'
    aliases = ['lemmaservices']
    filenames = ['*.services']
    mimetypes = ['text/lemmaservices']

    tokens = {
        'comments': [
            (r'[^*/]', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline)
        ],
        'api_comments': [
            (r'@required', Name.Builtin.Pseudo, 'api_comments_refparams'),
            (r'@returns', Name.Builtin.Pseudo, 'api_comments_refparams'),
            (r'[^---]', Name.Function),
            (r'---', Name.Function, '#pop')
        ],
        'api_comments_refparams': [
            (r'\s*\w+\s*', Text, '#pop')
        ],
        'root': [
            (r'/\*', Comment.Multiline, 'comments'),
            (r'//.*?$', Comment.Singleline),
            (r'---', Name.Function, 'api_comments'),
            (words((
                'as',
                'datatypes',
                'fault',
                'from',
                'functional',
                'import',
                'in',
                'interface',
                'microservice',
                'out',
                'public',
                'sync',
                'technology'
            )+PRIMITIVE_TYPE_TOKENS, prefix=r'\b', suffix=r'\b'), Keyword),
            (r'@\w+((::_)\w+\.\w+)?', Name.Builtin.Pseudo),
            # Features with one or two components, e.g., "<aggregate>" or
            # "<aggregate, entity>"
            (r'(<)(?:(\w+)(,))?(\s*)(\w+)(>)', bygroups(Text,
                Name.Builtin.Pseudo, Text, Text, Name.Builtin.Pseudo, Text)),
            # Features with three components, e.g., "<aggregate,entity,factory>"
            (r'(<)(\w+)(,)(\s*)(\w+)(,)(\s*)(\w+)(>)', bygroups(Text,
                Name.Builtin.Pseudo, Text, Text, Name.Builtin.Pseudo, Text,
                Text, Name.Builtin.Pseudo, Text)),
            (r'\".*?\"', String)
        ]
    }