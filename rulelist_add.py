import os,sys
def import_modules():
    try:
        from ruamel.yaml import YAML
    except ImportError:
        if os.path.exists(r"/usr/bin/pip3")==False:
            os.system("apt install python3-pip -y&&pip3 install pyyaml ruamel.yaml")
        else:
            os.system("pip3 install pyyaml ruamel.yaml")
    

def add_rule():
    import_modules()
    from ruamel.yaml import YAML
    if os.path.exists(r"/etc/XrayR/config.yml")==True:
        if os.path.exists(r"/etc/XrayR/rulelist")==False:os.system("wget -q https://github.yuanweize.win/raw.githubusercontent.com/yuanweize/XrayR_rulelist/master/rulelist -O /etc/XrayR/rulelist")
        with open(r"/etc/XrayR/config.yml") as file:
            data=YAML().load(file)
            for node in data["Nodes"]:
                node["ApiConfig"]["RuleListPath"]='/etc/XrayR/rulelist'
        with open(r"/etc/XrayR/config.yml","w") as file:
            YAML().dump(data,file)
        print('finish')
    else:
        print("XrayR/config.yml not exist")


if __name__=="__main__":
    add_rule()

