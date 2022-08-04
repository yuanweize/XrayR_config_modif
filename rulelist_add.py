import os
import sys
def import_yaml():
    try:
        import yaml
    except ImportError:
        if os.path.exists(r"/usr/bin/pip3")==False:
            print("yes")
        # os.system("apt install python3-pip&&pip3 install pyyaml")

def add_rule():
    if os.path.exists(r"/etc/XrayR/config.yml")==True:
        print("yes")
    else:
        print(sys.modules)
    # print(sys.modules)

if __name__=="__main__":
    import_yaml()
    # add_rule()