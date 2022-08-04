import os
import sys

import yaml
def import_pyyaml():
    try:
        import yaml
    except ImportError:
        if os.path.exists(r"/usr/bin/pip3")==False:
            os.system("apt install python3-pip -y&&pip3 install pyyaml")
        else:
            os.system("pip3 install pyyaml")
        import yaml
def add_rule():
    if os.path.exists(r"/etc/XrayR/config.yml")==True:
        with open(r"/etc/XrayR/config.yml") as file:
            data=yaml.load(file)
            print(data)

    else:
        print("XrayR/config.yml not exist")


if __name__=="__main__":
    import_pyyaml()
    add_rule()