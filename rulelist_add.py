import os,yaml
def add_rule():
    if os.path.exists(r"/etc/XrayR/config.yml")==True:
        print("yes")
    else:
        print("no")


if __name__=="__main__":
    add_rule()