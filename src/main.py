from textnode import *
from file_copy import *
import sys


def main():

    if len(sys.argv) > 1:
            basepath = sys.argv[1]
    else:
        basepath = "/"  # Default for local testing

    dst = "docs/"
    src = "static/"
    file_copy(src, dst)

    generate_pages_recursive("content", "template.html", "docs", basepath)


main()
