"""A Pygments lexer for LEMMA's Domain Data Modeling Language."""
from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import *

__all__ = ("LemmaDomainDataLexer", "PRIMITIVE_TYPE_TOKENS")

PRIMITIVE_TYPE_TOKENS = (
    'byte',
    'char',
    'date',
    'double',
    'boolean',
    'float',
    'int',
    'long',
    'short',
    'string',
    'unspecified',
)

class LemmaDomainDataLexer(RegexLexer):
    name = 'LEMMA Domain Data Modeling Language'
    aliases = ['lemmadomaindata']
    filenames = ['*.data']
    mimetypes = ['text/lemmadomaindata']

    tokens = {
        'root': [
            (words((
                'collection',
                'context',
                'enum',
                'hide',
                'immutable',
                'list',
                'structure',
                'unspecified'
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
