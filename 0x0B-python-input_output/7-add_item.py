#!/usr/bin/python3
"""Defined a function which adds args to list"""
import sys


if _name_ == "__main__":
    save_to_json_file = _import_('5-save_to_json_file').save_to_json_file
    load_from_json_file = _import_('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_items.json")
