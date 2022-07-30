import os
import sys
import subprocess
from libptsd import *
""" This is the official build library file. This is also a part of PyBuild. """

def usage(use):
    UsageText = use
    printf("Usage: %s\n" % UsageText)

def cmd(command):
    subprocess.run(command, shell=True)
