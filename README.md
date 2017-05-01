### document info
* Author
    * Kraig Andrews
* Date Created
    * 27 Apr 2017

### document building commands

The simpliest way to compile:
```bash
$ ./mk
```

For  the masochists:
```bash
$ pdflatex [main file].tex
$ pdflatex [main file].tex
$ bibtex [main file].aux
$ pdflatex [main file].tex
```

### cleaning the dirs

To clean the top dir:
```bash
$ ./clean
```

To clean all subdirs:
```bash
$ ./veryclean
```

### commit changes to repo

Without using `[alias]`
```bash
$ git add -A
$ git commit -m "[message]"
$ git push
```

Avaible aliases in `.git/config`
```bash
[alias]
    p = push
    c = commit
    ca = commit -a
    cm = commit -m
    cam = commit -am
```

Using aliases examples
```bash
$ git cam "[message]"
$ git p
```

Using `togithub` script
```bash
$ ./togithub "[mandatory message]"
```

### Directory Structure
```bash
.
|-- clean*
|-- main.pdf
|-- main.tex
|-- mk*
|-- README.md
|-- TODO.md
|-- togithub*
|-- veryclean*
|-- announcement/
|   |-- announcement.tex 
|   |-- clean*
|   |-- mk*
|	|-- veryclean*
|-- backmatter/
|   |-- autobio.tex
|-- chapters/
|   |-- chapter1/
|       |-- chap1.tex
|   |-- chapter2/
|       |-- chap2.tex
|   |-- chapter3/
|       |-- chap3.tex
|   |-- chapter4/
|       |-- chap4.tex
|    data/
|    drafts/
|    figs/
|        chap1/
|        chap2/
|        chap3/
|        chap4/
|        templates/
|            sidebyside.tex
|            subfig_captions.tex
|            subfigure.tex
|    frontmatter/
|        lists/
|            acronyms.tex
|            constants.tex
|            conversions.tex
|            symbols.tex
|        prelims/
|            abstract.tex
|            copyright.tex
|            quotation.tex
|            title.tex
|        thanks/
|            acknowledgements.tex
|            dedication.tex
|    logs/
|        tree_log.log
|    macros/
|        macros_custom.sty
|    notes/
|    old/
|    outline/
|        chapters/
|            chap1/
|                chap1_overview.tex
|		clean*
|                mk*
|		veryclean*
|            chap2/
|                chap2_overview.tex
|		clean*
|                mk*
|		veryclean*
|            chap3/
|                chap3_overview.tex
|		clean*
|                mk*
|		veryclean*
|            chap4/
|                chap4_overview.tex
|		clean*
|                mk*
|		veryclean*
|        templates/
|            overview.tex
|    quotes/
|        quotes.tex
|    refs/
|        database.bib
|        database_prospectus.bib
|    scripts/
|        clean*
|        clean_old*
|        mk*
|        togithub*
|        tree-md*
|        veryclean*
|    tables/
|        chap1/
|        chap2/
|        chap3/
|        chap4/
|	tikz/
|		mk*
|		pnj.tex
|		pnj.pdf
|	refpdfs/
|	    guide-tables.pdf
|	    booktabs.pdf
|        templates/
|            table_multiline.tex
|            table_simple.tex
|    talk/
|    	beamer/
|	    beamertemplate/
|            clean*
|            figs/
|                wsu_logo.jpg
|            slides.tex
|            veryclean*
|    	ppt/
|	    powerpoint.pptx
```



