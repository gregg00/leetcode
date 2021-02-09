# Read from the file file.txt and output all valid phone numbers to stdout.
#You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
#You may also assume each line in the text file must not contain leading or trailing white spaces.

#!/bin/bash

grep '^\([0-9]\{3\}-\|([0-9]\{3\}) \)[0-9]\{3\}-[0-9]\{4\}$' file.txt
