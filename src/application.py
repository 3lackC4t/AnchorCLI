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

    def anchor_add(self, path: str, alias: str):
        with open(self.anchor_path, 'a') as anchors:
            anchors.write(yaml.safe_dump({'alias': f'{alias}', 'path': f'{path}'}))

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

    general = parser.add_argument_group('group')
    yml_config = parser.add_mutually_exclusive_group()

    yml_config.add_argument('-n', '--new',
                        type=str,
                        action='store',
                        nargs=2,
                        default=f"{os.getcwd()}",
                        help='''Takes two arguments, an alias and a filepath, 
                                and stores it in anchors.yml''')
    yml_config.add_argument('-r', '--remove',
                            type=str,
                            action='store',
                            help='remove an anchor from anchors.yml')
    general.add_argument('do',
                        type=str,
                        action='store',
                        nargs=2,
                        help='''takes two arguments, an alias and a command, 
                                and executes the command in the chosen directory''')
    yml_config.add_argument('-l', '--list',
                         action='store_true',
                         help='lists currently saved anchors')

    args = parser.parse_args()
    return args


def main():
    args = build_parser()
    anchor = Anchor()
    print(args)
    anchor.do_anchor(args.do[0], args.do[1])
   

