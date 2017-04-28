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
.
    README.md
    main.tex
    main.pdf
    mk*
    clean*
    veryclean*
    announcement/
        announcement.tex 
        clean*
        mk_announcement*
