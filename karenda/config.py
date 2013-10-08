'''
Created on 17.02.2012

@author: flocki
'''
import os
import yaml


def get_config_path():
    os.path.join(os.path.expanduser("~"), "config", "gnomeshell-karenda", "config.yaml")


def set(parameter, value):
    config = get(None)
    config[parameter] = value
    with open(get_config_path(), 'w') as fp:
        yaml.dumps(config, fp)


def get(parameter):
    try:
        with open(get_config_path(), 'r') as fp:
            config = yaml.load(fp)
    except:
        config = dict()

    if parameter is None:
        return config
    if parameter in config:
        return config.get(parameter)
    else:
        config[parameter] = None
