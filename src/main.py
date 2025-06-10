from textnode import *
from file_copy import *

def main():

    dst = "public/"
    src = "static/"
    file_copy(src, dst)

    generate_pages_recursive("content", "template.html", "public")


main()
