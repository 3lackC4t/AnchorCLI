import argparse
import os
import pprint
import yaml

class Anchor:
    def __init__(self):
        self.default_anchors = [{'alias': 'home', 'path': '~/'},
                                {'alias': 'config', 'path': '~/.config'}]


def initialize():
    pass

def main():
    print(os.path.exists('~/.config/AnchorCLI/anchors.yml'))
    

