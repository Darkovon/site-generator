from textnode import *
from file_copy import *

def main():

    dst = "public/"
    src = "static/"
    file_copy(src, dst)

    generate_path("content/index.md", "template.html", "public/index.html")


main()
