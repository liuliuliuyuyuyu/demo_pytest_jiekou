import allure
import pytest

from base.BasePage import BasePage
from base import common
from base.common import logger
from base.setParameters import setParameters
from testcase.page.ZcZcrkPage import  Query,checkResultQuery,Add,checkResultAdd,Update,checkResultUpdate,Delete,checkResultDelete

yml_data = common.get_yml("ZcZcrk_data.yml")             #根据yml文件名和对应测试用例名获取数据


@allure.testcase("资产入库模块的testcase",name="testcase_link")#testcase、link、issue会出现在测试报告的link
@allure.feature("资产入库模块的feature")          #也可以根据功能名执行测试用例
@allure.severity(allure.severity_level.CRITICAL)    #重要程度，到时候可以根据重要程度筛选执行测试用例
class Test_ZcZcrk():
    @classmethod
    def setup_class(self):              #unittest是使用setUpClass(self)，一定要区分好，要不然没用
        """测试开始前的准备工作"""
        self.logger = logger  # 获取数据
        self.logger.info("测试开始前准备")
        BasePage.login()        #先获取登录cookie和设置好请求头

    @pytest.mark.run(order=1)   #测试用例执行顺序，在有需要的时候再用，还有其他使用方法具体用到再看
    @allure.story("资产入库查询的story")
    @pytest.mark.parametrize("data", yml_data['query'])  # 通过yml_data字典key值获取各自接口的数据，如这里的query对应的是查询接口的数据
    def test_AQuery(self, data):
        """资产入库--查询"""  #这个信息会出现在测试报告的Description中，相当于@allure.description
        with allure.step('初始化数据'):
            self.setparam = setParameters.setParameters(self,data)
            self.logger.info("初始化数据")
        with allure.step('发送请求'):
            self.return_json = Query(self, self.setparam)
            self.logger.info("第四步：发送请求成功")
        with allure.step('检查结果,响应断言'):
            self.logger.info("第五步：检查结果,响应断言")
            checkResultQuery(self,self.return_json,self.setparam)

    # def test_BAdd(self, data):
    #     """资产入库--新增"""
    #     # 初始化
    #     self.setparam = setParameters.setParameters(self, data)
    #     # 发送请求获取响应数据
    #     self.return_json = Add(self, self.setparam)
    #     self.logger.info("第四步：发送请求成功")
    #     # print("第四步：发送请求成功")
    #     print("*******************************************************************************************************")
    #     print("检查结果,响应断言")
    #     self.logger.info("第五步：检查结果,响应断言")
    #     # 响应断言
    #     checkResultAdd(self, self.return_json, self.setparam)
    #     print("\n第五步：断言结束")
    #     self.logger.info("第五步：断言结束")
    #
    # def test_CUpdate(self, data):
    #     """资产入库--修改"""
    #     # 初始化
    #     self.setparam = setParameters.setParameters(self, data)
    #     # 发送请求获取响应数据
    #     self.return_json = Update(self, self.setparam)
    #     self.logger.info("第四步：发送请求成功")
    #     # print("第四步：发送请求成功")
    #     print("*******************************************************************************************************")
    #     print("检查结果,响应断言")
    #     self.logger.info("第五步：检查结果,响应断言")
    #     # 响应断言
    #     checkResultUpdate(self, self.return_json, self.setparam)
    #     print("\n第五步：断言结束")
    #     self.logger.info("第五步：断言结束")
    #
    # def test_DDelete(self, data):
    #     """资产入库--删除"""
    #     # 初始化
    #     self.setparam = setParameters.setParameters(self, data)
    #     # 发送请求获取响应数据
    #     self.return_json = Delete(self, self.setparam)
    #     self.logger.info("第四步：发送请求成功")
    #     # print("第四步：发送请求成功")
    #     print("*******************************************************************************************************")
    #     print("检查结果,响应断言")
    #     self.logger.info("第五步：检查结果,响应断言")
    #     # 响应断言
    #     checkResultDelete(self, self.return_json, self.setparam)
    #     print("\n第五步：断言结束")
    #     self.logger.info("第五步：断言结束")

    @classmethod
    def teardown_class(self):
        self.logger.info("*********CASE END*********")
        print("*******************************************************************************************************")
        print("测试结束，输出log完结\n\n")

if __name__ == '__main__':
    pytest.main('test_ZcZcrk.py')

