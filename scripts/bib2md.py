#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# Convert bibtex to markdown
#
# - Author: Dongdong Tian @ USTC
# - Date: 2017-09-30
#
import re
import sys
from datetime import date

# bibitextparser>=1.0.0
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *

# get journal abbreviations from
# http://woodward.library.ubc.ca/research-help/journal-abbreviations/
abbr = {
    'Acta Geophysica Sinica': 'Acta Geophysica Sinica',
    'Bulletin of the Seismological Society of America': 'Bull. Seismol. Soc. Am.',
    'Earth and Planetary Science Letters': 'Earth Planet. Sci. Lett.',
    'EOS, Transactions American Geophysical Union': 'EOS Trans. AGU',
    'Geophysical Journal International': 'Geophys. J. Int.',
    'Geophysical Research Letters': 'Geophys. Res. Lett.',
    'Journal of Geophysical Research': 'J. Geophys. Res.',
    'Journal of Geophysical Research: Solid Earth': 'J. Geophys. Res. Solid Earth',
    'Physics of the Earth and Planetary Interiors': 'Phys. Earth Planet. Inter.',
    'Proceedings of the National Academy of Sciences': 'Proc. Natl. Acad. Sci.',
    'Science': 'Science',
    'Scientific Reports': 'Sci. Rep.',
    'Seismological Research Letters': 'Seismol. Res. Lett.',
    'Surveys in Geophysics': 'Surv. Geophys.',
    'Nature Communications': 'Nat. Commun.',
    'Nature': 'Nature',
}


def author(record):

    # Do nothing for Chinese papers
    if re.findall(r'[\u4e00-\u9fff]+', record['author']):
        record['author'] = ", ".join(record['author'].split(" and "))
        return record

    # precess of English papers
    authors = []
    for author in getnames(record['author'].split(" and ")):
        name = splitname(author)
        authors.append(name['last'][0] + ", " + name['first'][0][0] + ".")

    for i, author in enumerate(authors):
        if author == 'Wen, L.':
            authors[i] = '**Wen, L.**'
            break


    if len(authors) == 1:
        record['author'] = authors[0]
    else:
        record['author'] = " and ".join([", ".join(authors[:-1]), authors[-1]])
    return record


def journal(record):

    if record['journal'] in abbr:
        record['journal'] = abbr[record['journal']]
    else:
        print("Warning: Journal '{}' abbr not found.".format(record['journal']))

    return record


def title(record):
    text = record['title']
    text = text.replace("{\\textendash}", '–')
    text = text.replace("{\\textquotesingle}", "'")
    text = text.replace("{\\textquotedblleft}", '"')
    text = text.replace("{\\textquotedblright}", '"')
    text = text.replace("{", '')
    text = text.replace("}", '')

    record['title'] = text
    return record


def customizations(record):
    """Use some functions delivered by the library

    :param record: a record
    :returns: -- customized record
    """
    record = author(record)
    record = journal(record)
    record = title(record)
    return record


def entry2md(entry):
    bibitem = "{author}, {year}, {title}, ***{journal}***".format(
                    author=entry['author'],
                    year=entry['year'],
                    title=entry['title'],
                    journal=entry['journal'])

    if 'volume' in entry:
        bibitem += ", {}".format(entry['volume'])
    if 'number' in entry:
        bibitem += "({})".format(entry['number'])
    if 'pages' in entry:
        bibitem += ", {}".format(entry['pages'])
    if 'doi' in entry:
        bibitem += ", doi:[{doi}](https://dx.doi.org/{doi})".format(doi=entry['doi'])

    if 'status' in entry:
        bibitem += ', (*{}*)'.format(entry['status'])

    bibitem += '.'

    if 'reprint' in entry:
        bibitem += " [(Reprint pdf)]({})".format(entry['reprint'])

    if 'information' in entry:
        bibitem += " [General Information]({})".format(entry['information'])

    return bibitem


if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Usage: python {} bibfile markdownfile".format(sys.argv[0]))
        sys.exit()
    bibfile, mdfile = sys.argv[1:]

    startyear, endyear = 1994, 2020

    biblist = {}
    for year in range(startyear, endyear+1):
        biblist[year] = []

    # convert bib items to markdown list
    with open(bibfile, 'r') as bibtex:
        # prepare bibtex parser
        parser = BibTexParser()
        parser.customization = customizations
        bib_database = bibtexparser.load(bibtex, parser=parser)

        for entry in bib_database.entries:
            item = entry2md(entry)
            biblist[int(entry['year'])].append(item)

    # write all items to markdown file
    with open(mdfile, 'w') as md:
        # write markdown frontmatter
        md.write("---\n")
        md.write("title: 历年发表文献\n")
        md.write("date: {:s}\n".format(date.today().strftime("%Y-%m-%d")))
        md.write("---\n")

        for year in reversed(range(startyear, endyear+1)):
            if not biblist[year]:
                continue

            md.write("\n## {}\n\n".format(year))
            for item in biblist[year]:
                md.write('- ' + item + '\n')
