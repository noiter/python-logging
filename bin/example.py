#!/usr/bin/env python
import os
import sys
import logging

sys.path.insert(0, os.getcwd())
from customlogging import LoggingSettings
from tmodule import TModule

def main():
    bar = TModule()
    bar.bar()

if __name__ == '__main__':
    LoggingSettings().configure()

    main()