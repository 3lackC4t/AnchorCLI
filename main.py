import argparse
import os
import pprint
import yaml


class Anchors:
  def __init__(self) -> None:
    self.anchor_path = os.path.join('~/.config/Anchors', 'Anchors.yml')
    
    with open(self.anchor_path, 'r') as anchors:
      self.anchors = yaml.safe_load(anchors)
    
  def anchor_yank(self, alias):
    if alias in self.anchors:
      os.system(f'cd {self.anchors[alias]}')

  def anchor_add(self, alias, path):
    with open(self.acnhor_path, 'a') as anchors:
      new_anchor = {'alias': alias, 'path': path}
      anchors.write(yaml.safe_dump(new_anchor))

  def anchor_remove(self):
    pass

class AnchorConfigurator(Anchors):
  def __init__(self):
    super().__init__()
    self.default_config = [{'alias': 'home', 'path': '~/'},
                          {'alias':'config', 'path':'~/.config'}]
    
  def creat_config(self):
    if os.path.exists(self.anchor_path):
      print("anchor.yml already exists. Checking for configurations...")
      with open(self.anchor_path, 'r') as anchors:
        if yaml.safe_load(anchors):
          print("Configurations found. Skipping creation of anchor.yml")
          exit()
        else:
          print('No configuration found. Configuring anchors.yml')
          with open(self.anchor_path, 'a') as anchors:
            anchors.write(yaml.safe_dump(self.default_config))
    else:
      print('anchor.yml does not exist, configuring anchor.yml...')      
      with open(self.anchor_path, 'w') as anchors:
        anchors.write(yaml.safe_dump(self.default_config))

  def check_config(self):
    if os.path.exists(self.anchor_path):
      with open(self.anchor_path) as anchors:
        if yaml.safe_load(anchors):
          return
        else:
          print("No configuration found. Configuring anchors.yml")
          self.creat_config()

  def print_anchor_list(self):
    with open(self.anchor_path) as anchors:
      pprint.pp(anchors, indent=2, width=60)


def build_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-a', '--add', type=str, default=os.getcwd(), 
                      action='store_true', help='Add an anchor')
  parser.add_argument('-r', '--remove', type=str, help='Remove an anchor')
  parser.add_argument('-y', '--yank', type=str, default='home', 
                      help="Move to the anchors directory"
  parser.add_arguement('-l', '--list', type=str, 
                       action='store_true',help='list current anchors and their paths')

  args = parser.parse_args()
  return args

def main():
  args = build_parser()
  anchor = Anchors()
  anchor_config = AnchorConfigurator()

  # Check if config exists
  anchor_config.check_config()

  if args.add:
    anchor.anchor_add(args.add)
  elif args.remove:
    pass
  elif args.yank:
    anchor.anchor_yank(args.yank)
  

if __name__ == "__main__":
  pass
