import os
from HTMLTestReportCN import HTMLTestRunner
import unittest
# import common.HTMLTestRunner as HTMLTestRunner


suite = unittest.defaultTestLoader.discover("./")

f = open("report.html", 'wb')
HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="duke").run(suite)
f.close()
