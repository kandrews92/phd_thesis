Author: Kraig J. Andrews

**************************************************************
   ## Basic commands for compiling:
**************************************************************

-To build pdf(s):
    $ pdflatex filename.tex
    $ pdflatex filename.tex
    $ bibtex filename.aux
    $ pdflatex filename.tex
    or
    $ ./mk

-To clean top directory:
    $ ./clean

-To commit changes to github:
    $ git add -A 
    $ git commit -m "message..."
    $ git push

**************************************************************
   ## File structure:
**************************************************************

announcement/:
    announcement.tex
    clean
    mk_announcement

frontmatter/:
    lists/:
        acronyms.tex 
        constants.tex
        coversions.tex
        symbols.tex
    prelims/:
        abstract.tex
        copyright.tex
        quotation.tex
        title.tex
    thanks/:
        acknowledgements.tex
        dedication.tex

backmatter/:
    autobio.tex

refs/:
    database.bib
    database_prospectus.bib

chapters/:
    chapter1/:
        chap1.tex
    chapter2/:
        chap2.tex
    chapter3/:
        chap3.tex
    chapter4/:
        chap4.tex

macros/:
    macros_custom.sty

data/:

figs/:

quotes/:
    quotes.tex

drafts/:

outline/:
    chapters/:
        chap1/:
            chap1_overview.tex
            mk
        chap2/:
            chap2_overview.tex
            mk
        chap3/:
            chap3_overview.tex
            mk
        chap4/:
            chap4_overview.tex
            mk
    scripts/:
        mk
        clean
    template/:
        overview.tex

talk/:
    powerpoint.pptx

./mk:
    make script for latex files

./clean:
    clean script for top directory, for use before using commit
    to github
***************************************************************