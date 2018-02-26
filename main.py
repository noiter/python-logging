#!/usr/bin/env python

import logging

import logging_settings
import test_module

def main():
    test_module.foo()
    bar = test_module.Bar()
    bar.bar()

if __name__ == '__main__':
    logging_settings.configure()

    main()