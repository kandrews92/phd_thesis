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

### Task List
- [ ] Item to be done 1
- [ ] Item to be done 2

### Directory Structure
```bash
./
    clean*
    main.pdf
    main.tex
    mk*
    README.md
    togithub*
    veryclean*
    announcement/
        announcement.tex 
        clean*
        mk_announcement*
    backmatter/
        autobio.tex
    chapters/
        chapter1/
            chap1.tex
        chapter2/
            chap2.tex
        chapter3/
            chap3.tex
        chapter4/
            chap4.tex
    data/
    drafts/
    figs/
        chap1/
        chap2/
        chap3/
        chap4/
        templates/
            sidebyside.tex
            subfig_captions.tex
            subfigure.tex
    frontmatter/
        lists/
            acronyms.tex
            constants.tex
            conversions.tex
            symbols.tex
        prelims/
            abstract.tex
            copyright.tex
            quotation.tex
            title.tex
        thanks/
            acknowledgements.tex
            dedication.tex
    logs/
        tree_log.log
    macros/
        macros_custom.sty
    notes/
    old/
    outline/
        chapters/
            chap1/
                chap1_overview.tex
                mk*
            chap2/
                chap2_overview.tex
                mk*
            chap3/
                chap3_overview.tex
                mk*
            chap4/
                chap4_overview.tex
                mk*
        scripts/
            mk*
            clean*
        templates/
            overview.tex
    quotes/
        quotes.tex
    refs/
        database.bib
        database_prospectus.bib
    scripts/
        clean*
        clean_old*
        mk*
        togithub*
        tree-md*
        veryclean*
    tables/
        chap1/
        chap2/
        chap3/
        chap4/
        templates/
            table_multiline.tex
            table_simple.tex
    talk/
        powerpoint.pptx
```



