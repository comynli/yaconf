# coding=utf-8

import yaml
from utils import DotDict

__author__ = 'comyn'


class _Loader(yaml.Loader):

    def __init__(self, *args, **kwargs):
        yaml.Loader.__init__(self, *args, **kwargs)

    def construct_mapping(self, node, deep=False):
        mapping = yaml.Loader.construct_mapping(self, node, deep)
        for key in mapping:
            if type(key) == str:
                new = key.replace("-", "_")
                if new != key:
                    mapping[new] = mapping[key]
                    del mapping[key]
        return mapping


class Config(DotDict):
    _environments = {"production", "staging", "development"}
    env = "development"

    def parse(self, stream):
        d = yaml.load(stream, Loader=_Loader)
        self.update(d)

    @property
    def environments(self):
        return self._environments

    @environments.setter
    def set_environments(self, environments):
        self._environments = environments

    def add_env(self, env):
        self._environments.add(env)

    def del_env(self, env):
        self._environments.remove(env)

    def set_env(self, env):
        if env not in self._environments:
            raise RuntimeError("Unknown environment")
        DotDict.env = env

    def __getattr__(self, item):
        try:
            ret = getattr(getattr(self, DotDict.env), item)
            if not ret:
                ret = getattr(self, item)
            return ret
        except AttributeError:
            raise AttributeError("configure item %s not found" % item)



if __name__ == '__main__':
    c = Config()
    with open('/Users/xuemingli/workspace/logminitor-config/alertd/alertd.yml') as f:
        c.parse(f)
        c.set_env('production')
        print c.zookeeper.hosts
