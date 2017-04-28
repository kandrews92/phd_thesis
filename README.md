### document building commands

The simpliest way to compile:
```bash
    $ ./mk
```

For  the masochists:
```base
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
```base
$ ./veryclean
```

### commit changes to repo
```base
$ git add -A
$ git commit -m "[message]"
$ git push