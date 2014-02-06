# coding: utf-8

from __future__ import unicode_literals
import sys
import os.path as op

from fabric.api import env, local, run, cd, lcd, settings, sudo, put, task
from fabric.colors import red, green
from fabric.contrib.files import exists

@task
def gen():
    """
        Generate the slides
    """

    with lcd("slides"):
        local("landslide presentation.cfg")

@task
def demo():
    """
    Runs the src/db.py file
    """
    with lcd("src"):
        local("python db.py")