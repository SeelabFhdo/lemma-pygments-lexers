"""A Pygments lexer for LEMMA's Technology Modeling Language."""
from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import *
from . import PRIMITIVE_TYPE_TOKENS

__all__ = ("LemmaTechnologyLexer")

class LemmaTechnologyLexer(RegexLexer):
    name = 'LEMMA Technology Modeling Language'
    aliases = ['lemmatechnology']
    filenames = ['*.technology']
    mimetypes = ['text/lemmatechnology']

    tokens = {
        'root': [
            (words((
                'aspect',
                'based on',
                'compatibility matrix',
                'data formats',
                'default',
                'default with format',
                'deployment technologies',
                'for fields',
                'for microservices',
                'for operations',
                'for parameters',
                'for types',
                'operation environments',
                'primitive type',
                'protocols',
                'selector',
                'service aspects',
                'service properties',
                'sync',
                'technology',
                'types'
            )+PRIMITIVE_TYPE_TOKENS, prefix=r'\b', suffix=r'\b'), Keyword),
            (r'(true|false)\b', Keyword.Constant),
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
