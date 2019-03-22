import readConfig as readConfig
readconfig = readConfig.ReadConfig()


# 定义一个方法，将从配置文件中读取的进行拼接
class GeturlParams():
    def get_url(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('serverurl') + '?'
        return new_url


# 验证拼接后的正确性
if __name__ == '__main__':
    print(GeturlParams().get_url())
