import os
import configparser
import getpathInfo

path = getpathInfo.get_Path()
# 调用实例化，还记得这个类返回的路径为D:\interfacetTest
config_path = os.path.join(path, 'config.ini')
# 这句话是在path路径下再加一级，最后变成D:\interfacetTest\config.ini
config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')
print(config_path)

class ReadConfig():
    def get_http(self, name):
        value = config.get('HTTP', name)
        return value
        print(value)

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

# 写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value


# 测试一下，我们读取配置文件的方法是否可用
if __name__ == '__main__':
    print('HTTP中的serverUrl值为：', ReadConfig().get_http('serverUrl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))

