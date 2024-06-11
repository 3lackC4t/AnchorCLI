import argparse
import os
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

    def add_anchor(self, alias: str, path=os.getcwd()):
        self.current_anchors.append({'alias': f'{alias}', 'path': f'{path}'})
        with open(self.anchor_path, 'w') as anchors:
            anchors.write(yaml.safe_dump(self.current_anchors))

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
    parser = argparse.ArgumentParser(description='''Manage anchors and execute shell 
                                     commands in specified directories.''')

    optional = parser.add_mutually_exclusive_group()
    optional.add_argument('-a', 
                          '--add', 
                          metavar=('alias', 'path'), 
                          nargs=2, 
                          help='Add a new anchor')
    optional.add_argument('-r', 
                          '--reset', 
                          action='store_true', 
                          help='Reset anchors to program defaults')
    optional.add_argument('-l', 
                          '--list', 
                          action='store_true', 
                          help='List all anchors')
    parser.add_argument('alias', 
                        nargs='?', 
                        type=str, 
                        help='Alias and shell command to execute')
    parser.add_argument('shell_command',
                        nargs=argparse.REMAINDER,
                        type=str,
                        help="The shell command to be executed")

    args = parser.parse_args()

    return args


def main():
    args = build_parser()
    anchor = Anchor()

    if args.add:
        alias, path = args.add
        anchor.add_anchor(alias, path)
    elif args.reset:
        anchor.reset_anchors()
        print("anchors.yml reset to program defaults. See documentation for details")
    elif args.list:
        print("Listing all available anchors...")
        anchor.list_anchors()
    elif args.alias:
        alias = args.alias
        command = " ".join(args.shell_command)
        anchor.do_anchor(alias, command)
    else:
        parser.print_help()
