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

    def do_anchor(self, alias: str, command: str):
        try:
            for anchor in self.current_anchors:
                if anchor['alias'] == alias:
                    os.chdir(anchor['path'])
                    os.system(f'{command}')
        except PermissionError as PermErr:
            print('Permission denied, command must be run as root')

    def anchor_add(self, alias: str, path: str):
        pass

    def list_anchors(self):
        for index, anchor in enumerate(self.current_anchors):
            print(f"Anchor {index}: Alias: {anchor['alias']} Path: {anchor['path']}")

    def reset_anchors(self):
        with open(self.anchor_path, 'w') as anchors:
            anchors.write(yaml.safe_dump(self.default_anchors))
        
        with open(self.anchor_path, 'r') as anchors:
            self.current_anchors = yaml.safe_load(anchors)

    def set_default_anchors(self, anchor_args):
        new_default = []
        for arg in anchor_args:
            new_default.append(arg)

        self.default_anchors = new_default


def build_parser():
    parser = argparse.ArgumentParser(
        prog='AnchorCLI',
        description='''
        A tool for easily executing shell commands in directories using easy to remember and user
        configurable aliases.
        '''
        )
    parser.add_argument('-a', '--alias', 
                       action='store', 
                       type=str, 
                       help='the alias for where the command will be executed')
    parser.add_argument('-c', '--command',
                       action='store',
                       type=str,
                       help='the command to be executed')
    parser.add_argument('-R', '--reset',
                       action='store_true',
                       help='reset the default anchors list')
    parser.add_argument('-A', '--add',
                       action='store',
                       type=str,
                       default=f'{os.getcwd()}')

    args = parser.parse_args()
    return args


def main():
    args = build_parser()
    anchor = Anchor()
    anchor.do_anchor(args.alias, args.command)
