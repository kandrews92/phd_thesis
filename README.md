#---------------------------------------------------------------------------#
# thesis github repo                                                        #
#                                                                           #
# author: Kraig Andrews                                                     #
#                                                                           #
# date created: 04/27/2017                                                  #
#---------------------------------------------------------------------------#



# Basic commands for compiling documents:

   -to build pdf(s):
    ```
      $ pdflatex [filename].tex
    ```
    ```
      $ pdflatex [filename].tex
    ```
    ```
      $ bibtex [filename].aux
    ```
    ```
      $ pdflatex [filename].tex
    ```
   -or-
   ```
      $ ./mk
    ```

  -to clean top directory:
    ```
      $ ./clean
    ```

  -to clean top directory and all subdirs:
    ```
      $ ./veryclean
    ```
//
/*-------------------------------------------------------------------------*/

/*-------------------------------------------------------------------------*/
//
## Basic commands for GitHub commits:
//
//  -to add changed docs to queue:
//      $ git add -A
//
//  -to commit changes to queue:
//      $ git commit -m "[message]"
//
//  -to push changes to repo:
//      $ git push
//
//  -or-
//
//  -use aliases
//      -alisases are stored in file: .git/config
//
//  [aliases]:
//      p = push
//      c = commit
//      ca = commit -a
//      cm = commit -m
//      cam = commit -am
//
//  examples of alias usage:
// 
//  -to commit all changes:
//      $ git cam "[message]"
//
//  -to push all changes:
//      $ git p
//
/*-------------------------------------------------------------------------*/

