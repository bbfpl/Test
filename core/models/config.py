# coding=utf-8
import os
import configparser
from base import base_dir

# read config class
class Config:
    # 初始化 configparser
    @classmethod
    def read_base_config(cls):
        #获取根目录下config.ini
        config_path = os.path.join(base_dir(),'config.ini')
        # 读取配置文件
        config = configparser.ConfigParser()
        config.read(config_path,'utf-8')
        return config

    @classmethod
    def get_config(cls,name=''):
        if name=='':
            print('name不能为空')
            return False
        # 获取config
        config = cls.read_base_config()
        val = config.get("Config", name)
        return val

if __name__ == '__main__':
    print(Config.get_config(''))


