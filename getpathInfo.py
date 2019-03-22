import os


def get_Path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path


'''
projectDir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# 路径拼接
test_dir = os.path.join(projectDir, 'api')
outHtml = os.path.join(projectDir, 'report') + os.sep
'''

if __name__ == '__main__':  # 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_Path())
