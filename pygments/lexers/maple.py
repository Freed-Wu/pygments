"""
    pygments.lexers.maple
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for Maple.

    :copyright: Copyright 2024-2024 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, words, bygroups
from pygments.token import Comment, Name, String, Whitespace, Operator, Punctuation, Number, Text, Keyword

__all__ = ['MapleLexer']


class MapleLexer(RegexLexer):
    """
    Lexer for Maple.
    """

    name = 'Maple'
    aliases = ['maple']
    filenames = ['*.mpl', '*.mi', '*.mm']
    mimetypes = ['text/x-maple']
    url = 'https://www.maplesoft.com/products/Maple/'
    version_added = ''

    keywords = ('and',
                'assuming',
                'break',
                'by',
                'catch',
                'description',
                'do',
                'done',
                'elif',
                'else',
                'end',
                'error',
                'export',
                'fi',
                'finally',
                'for',
                'from',
                'global',
                'if',
                'implies',
                'in',
                'intersect',
                'local',
                'minus',
                'mod',
                'module',
                'next',
                'not',
                'od',
                'option',
                'options',
                'or',
                'proc',
                'quit',
                'read',
                'return',
                'save',
                'stop',
                'subset',
                'then',
                'to',
                'try',
                'union',
                'use',
                'uses',
                'while',
                'xor')

    builtins = ('abs',
                'add',
                'addressof',
                'anames',
                'and',
                'andmap',
                'andseq',
                'appendto',
                'Array',
                'array',
                'ArrayOptions',
                'assemble',
                'ASSERT',
                'assign',
                'assigned',
                'attributes',
                'cat',
                'ceil',
                'coeff',
                'coeffs',
                'conjugate',
                'convert',
                'CopySign',
                'DEBUG',
                'debugopts',
                'Default0',
                'DefaultOverflow',
                'DefaultUnderflow',
                'degree',
                'denom',
                'diff',
                'disassemble',
                'divide',
                'done',
                'entries',
                'EqualEntries',
                'eval',
                'evalb',
                'evalf',
                'evalhf',
                'evalindets',
                'evaln',
                'expand',
                'exports',
                'factorial',
                'floor',
                'frac',
                'frem',
                'FromInert',
                'frontend',
                'gc',
                'genpoly',
                'has',
                'hastype',
                'hfarray',
                'icontent',
                'igcd',
                'ilcm',
                'ilog10',
                'Im',
                'implies',
                'indets',
                'indices',
                'intersect',
                'iolib',
                'iquo',
                'irem',
                'iroot',
                'iroot',
                'isqrt',
                'kernelopts',
                'lcoeff',
                'ldegree',
                'length',
                'lexorder',
                'lhs',
                'lowerbound',
                'lprint',
                'macro',
                'map',
                'max',
                'maxnorm',
                'member',
                'membertype',
                'min',
                'minus',
                'mod',
                'modp',
                'modp1',
                'modp2',
                'mods',
                'mul',
                'NextAfter',
                'nops',
                'normal',
                'not',
                'numboccur',
                'numelems',
                'numer',
                'NumericClass',
                'NumericEvent',
                'NumericEventHandler',
                'NumericStatus',
                'op',
                'or',
                'order',
                'OrderedNE',
                'ormap',
                'orseq',
                'parse',
                'piecewise',
                'pointto',
                'print',
                'quit',
                'Re',
                'readlib',
                'Record',
                'remove',
                'rhs',
                'round',
                'rtable',
                'rtable_elems',
                'rtable_eval',
                'rtable_indfns',
                'rtable_num_elems',
                'rtable_options',
                'rtable_redim',
                'rtable_scanblock',
                'rtable_set_indfn',
                'rtable_split_unit',
                'savelib',
                'Scale10',
                'Scale2',
                'SDMPolynom',
                'searchtext',
                'SearchText',
                'select',
                'selectremove',
                'seq',
                'series',
                'setattribute',
                'SFloatExponent',
                'SFloatMantissa',
                'sign',
                'sort',
                'ssystem',
                'stop',
                'String',
                'subs',
                'subset',
                'subsindets',
                'subsop',
                'substring',
                'system',
                'table',
                'taylor',
                'tcoeff',
                'time',
                'timelimit',
                'ToInert',
                'traperror',
                'trunc',
                'type',
                'typematch',
                'unames',
                'unassign',
                'union',
                'Unordered',
                'upperbound',
                'userinfo',
                'writeto',
                'xor',
                'xormap',
                'xorseq')
    tokens = {
        'root': [
            (r'#.*\n', Comment.Single),
            (r'\(\*', Comment.Multiline, 'comment'),
            (r'"(\\.|.|\s)*?"', String),
            (r"('+)(.|\n)*?\1", String),
            (words(keywords, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(builtins, prefix=r'\b', suffix=r'\b'), Name.Builtin),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', Name),
            (r'`(\\`|.)*?`', Name),
            (r'(:=|\*\*|@@|<=|>=|<>|->|::|\.\.|&\+|[\+\-\*\.\^\$/@&,:=<>%~])', Operator),
            (r'[;^!@$\(\)\[\]{}|_\\#?]', Punctuation),
            (r'(\d+)(\.\.)', bygroups(Number.Integer, Punctuation)),
            (r'(\d*\.\d+|\d+\.\d*)([eE][+-]?\d+)?', Number.Float),
            (r'\d+', Number.Integer),
            (r'\n', Whitespace),
            (r'[^\S\n]+', Whitespace),
            (r'\s+', Text),

        ],
        'comment': [
            (r'.*\(\*', Comment.Multiline, '#push'),
            (r'.*\*\)', Comment.Multiline, '#pop'),
            (r'.*\n', Comment.Multiline),
        ]
    }
