#!/usr/bin/python3
"""Locked class module"""


class LockedClass:
    """Allows first_name attribute instantiation only"""
    __slots__ = ["first_name"]
