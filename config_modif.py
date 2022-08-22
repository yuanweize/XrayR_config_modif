import os,sys
def import_modules():
    try:
        from ruamel.yaml import YAML
        return True
    except ImportError:
        print('from ruamel.yaml import YAML FIALED, Try to install pyyaml and ruamel.yaml')
        if os.path.exists(r"/usr/bin/pip3")==False:
            print('RUN: apt install python3-pip -y&&pip3 install pyyaml ruamel.yaml')
            os.system("apt install python3-pip -y&&pip3 install pyyaml ruamel.yaml")
        else:
            print('RUN: pip3 install pyyaml ruamel.yaml')
            os.system("pip3 install pyyaml ruamel.yaml")
    

def add_config(TEST,ApiConfig_key,ApiConfig_value,Flag=all):
    import_modules()
    from ruamel.yaml import YAML
    # if os.path.exists(r"/etc/XrayR/rulelist")==False:os.system("wget -q https://github.yuanweize.win/raw.githubusercontent.com/yuanweize/XrayR_rulelist/master/rulelist -O /etc/XrayR/rulelist")
    if os.path.exists(path)==True:
        with open(path) as file:
            data=YAML().load(file)
            for node in data["Nodes"]:
                node["ApiConfig"][ApiConfig_key]=ApiConfig_value
        with open(path,"w") as file:
            YAML().dump(data,file)
        if TEST==False:os.system("systemctl restart XrayR")
        print('finish\nIn PATH: '+path)
    else:
        print(path+" not exist")

def del_config(TEST,ApiConfig_key):
    import_modules()
    from ruamel.yaml import YAML
    if os.path.exists(path)==True:
        with open(path) as file:
            data=YAML().load(file)
            for node in data["Nodes"]:
                if ApiConfig_key in node["ApiConfig"]:
                    del node["ApiConfig"][ApiConfig_key]
                else:
                    print(ApiConfig_key+" not exist in nodeID: "+node["ApiConfig"]["NodeID"])
        with open(path,"w") as file:
            YAML().dump(data,file)
        if TEST==False:os.system("systemctl restart XrayR")
        print('finish\nIn PATH: '+path)
    else:
        print(path+" not exist")

if __name__=="__main__":
    TEST=True
    if TEST==False:path=r"/etc/XrayR/config.yml"
    else:path=r"/Users/yuanweize/我的文档/服务器/GITHUB/PyTools/XrayR_config_mod/config.yml"
    # add_config(TEST,ApiConfig_key="AsAssdasdasdListPath",ApiConfig_value='/etc/XrayR/rulelist')
    del_config(TEST,ApiConfig_key="AAListPath")
