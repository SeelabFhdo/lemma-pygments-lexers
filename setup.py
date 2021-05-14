#!/usr/bin/env python
from setuptools import setup, find_packages

entry_points = '''
[pygments.lexers]
lemmadomaindata=lemma_pygments_lexers:LemmaDomainDataLexer
'''

setup(
    name='lemma-pygments-lexers',
    version='0.0.1',
    description='Pygments lexer package for LEMMA.',
    author='Florian Rademacher',
    author_email='florian.rademacher@fh-dortmund.de',
    url='https://github.com/SeelabFhdo/lemma-pygments-lexers/',
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=[
        'Pygments>=2.0.1'
    ],
    zip_safe=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: Markdown'
    ]
)
