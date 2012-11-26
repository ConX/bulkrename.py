Description
===========

A python script to rename all the files in a directory
using a certain pattern.

If the files have an extension it will be preseved.

Use the --dry-run option to make sure for the result and
backup before exuting it for a directory containing critical
files.

Help
====

Usage: bulkrename.py [options] <directory>

Options:

    -h, --help            show this help message and exit  
    -p PREFIX, --prefix=PREFIX  
			  Add the prefix string.  
    -s SUFFIX, --suffix=SUFFIX  
			  Add the suffix string.  
    -d, --dry-run         Run without actually renaming any files.  


Examples
========

**Files without extensions, using prefix and suffix:**

```sh
$ ls test
bar  foo  tmp  tmp2

$ <path>/bulkrename.py -p "test_[" -s "]" test
Renaming /tmp/test/bar -> /tmp/test/test_[0]
Renaming /tmp/test/foo -> /tmp/test/test_[1]
Renaming /tmp/test/tmp -> /tmp/test/test_[2]
Renaming /tmp/test/tmp2 -> /tmp/test/test_[3]
    
$ ls test
test_[0]  test_[1]  test_[2]  test_[3]
```

**Files with extensions, using prefix and suffix:**

```sh
$ ls test
bar.sh  foo.txt,  lala.jpg

$ <path>/bulkrename.py -p "file (" -s ")" test
Renaming /tmp/test/bar.sh -> /tmp/test/file (0).sh
Renaming /tmp/test/foo.txt -> /tmp/test/file (1).txt
Renaming /tmp/test/lala.jpg -> /tmp/test/file (2).jpg

$ ls test
file (0).sh  file (1).txt  file (2).jpg
```
