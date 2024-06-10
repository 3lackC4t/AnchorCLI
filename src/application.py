import argparse
import os
import pprint
import yaml

class Anchor:
    def __init__(self):
        self.default_anchors = [{'alias': 'home', 'path': f'/home/{os.getlogin()}'},
                                {'alias': 'config', 'path': f'/home/{os.getlogin()}/.config'}]
        
        if not os.path.exists(f'/home/{os.getlogin()}/.config/AnchorCLI/anchors.yml'):
            os.makedirs(f'/home/{os.getlogin()}/.config/AnchorCLI', exist_ok=True)
            with open(f'/home/{os.getlogin()}/.config/AnchorCLI/anchors.yml', 'w') as anchors:
                anchors.write(yaml.safe_dump(self.default_anchors))

            self.anchor_path = os.path.join(f'/home/{os.getlogin()}/.config/AnchorCLI', 'anchors.yml')
        else:
            self.anchor_path = os.path.join(f'/home/{os.getlogin()}/.config/AnchorCLI', 'anchors.yml')
        
        with open(self.anchor_path, 'r') as anchors:
            self.current_anchors = yaml.safe_load(anchors)

    def anchor_move(self, alias):
        for anchor in self.current_anchors:
            if anchor['alias'] == alias:
                print(anchor['path'])
                os.chdir(anchor['path'])

    def anchor_add(self, alias, path):
        pass

def initialize():
    pass

def main():
    anchor = Anchor()
    print(os.getcwd())
    anchor.anchor_move('config')
    print(os.getcwd())

