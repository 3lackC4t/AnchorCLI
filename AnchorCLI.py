import argparse
import os
import pprint
import yaml

class Anchor:
  def __init__(self):
    self.anchor_dirs = '/etc/opt/AnchorCLI'
    self.anchor_path = os.path.join(self.anchor_dirs, 'Anchors.yml')
    self.default_config = [{'alias': 'home', 'path': '/home'}, 
                           {'alias': 'config', 'path': '~/.config'}]
    try:
      with open(self.anchor_path, 'r') as anchors:
        self.anchors = yaml.safe_load(anchors)
    except FileNotFoundError:
      self.create_config()

  def create_config(self):
    if os.path.exists(self.anchor_path):
      try:
        with open(self.anchor_path, 'r') as anchors:
          if yaml.safe_load(anchors):
            return
      except FileNotFoundError:
        with open(self.anchor_path, 'w') as anchors:
          anchors.write(yaml.safe_dump(self.default_config))
      except PermissionError:
        print('Permission denied, run as root')
    else:
      try:
        os.makedirs(os.path.dirname(self.anchor_dirs))
        with open(self.anchor_path, 'w') as anchors:
          anchors.write(yaml.safe_dump(self.default_config))
      except PermissionError:
        print('Permission denied, run as root')

  def anchor_add(self, alias, path):
    new_anchor = {'alias': alias, 'path': path}
    if os.path.exists(path):
      self.anchors.append({'alias': alias, 'path': path})
      with open(self.anchor_path, 'a') as anchors:
        anchors.write(yaml.safe_dump(new_anchor))
    else:
      print('Path does not exist')

  def anchor_move(self, alias):
    for anchors in self.anchors:
      if alias in anchors:
        os.system(f'cd {anchors[alias]}')


def build_parser():
  pass

def main():
  pass

if __name__ == "__main__":
  anchor = Anchor()
  anchor.create_config()
  anchor.anchor_move(alias='config')

