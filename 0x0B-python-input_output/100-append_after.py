#!/usr/bin/python3
""" Text appending module"""


def append_after(filename="", search_string="", new_string=""):
    """Appends text after a given text
    Args:
    search_string: string after which new strin is appended
    new_string: string to be appended
    """
    new_content = ""
    with open(filename) as fp:
        for txt in fp:
            new_content += txt
            if search_string in txt:
                new_content += new_string
                break
    with open(filename, "w") as fp2:
        fp2.write(new_content)
