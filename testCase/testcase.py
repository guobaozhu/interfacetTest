import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
import pythoncom
import readExcel
pythoncom.CoInitialize()

url = geturlParams.GeturlParams().get_url()  # 调用geturlParams获取拼接的URL
shop_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'shop')


@paramunittest.parametrized(*shop_xls)
class TestGetBigLevelPrizeList(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):

        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
       # self.expect_res = str(expect_res)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        print(self.case_name+"测试开始前准备")

    def testcase(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        """
        check test result
        :return:
        """
        url1 = url + self.path
        new_url = url1 + "&" + self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        info = RunMain().run_main(method=self.method, url=url, data=data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)
        # 将响应转换为字典格式
        if self.case_name == 'test_getBigLevelPrizeList_normal':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], 200)
        if self.case_name == 'test_getBigLevelPrizeList_noUserId':  # 同上
            self.assertEqual(ss['code'], 101)
        if self.case_name == 'test_getBigLevelPrizeList_noToken':  # 同上
            self.assertEqual(ss['code'], 101)
        if self.case_name == 'test_getBigLevelPrizeList_noAll':  # 同上
            self.assertEqual(ss['code'], 101)
