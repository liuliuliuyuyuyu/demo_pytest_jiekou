# coding=UTF-8

class setParameters:
    def setParameters(cls, data):
        '''
       定义变量接收值
       '''
        if '用例名' in data:
            cls.case_name = str(data['用例名'])
            setParameters.dataprint('测试用例名：%s' % cls.case_name)
        if 'result' in data:
            cls.result = str(data['result'])
        if 'method' in data:
            cls.method = str(data['method'])  # 请求方法
        if 'AddUrl' in data:
            cls.AddUrl = str(data['AddUrl'])
        if 'DeleteUrl' in data:
            cls.DeleteUrl = str(data['DeleteUrl'])
        if 'UpdateUrl' in data:
            cls.UpdateUrl = str(data['UpdateUrl'])
        if 'QueryUrl' in data:
            cls.QueryUrl = str(data['QueryUrl'])
        if 'AcceptUrl' in data:
            cls.AcceptUrl = str(data['AcceptUrl'])
        if 'BatchAcceptUrl' in data:
            cls.BatchAcceptUrl = str(data['BatchAcceptUrl'])
        if 'AcceptBillUrl' in data:
            cls.AcceptBillUrl = str(data['AcceptBillUrl'])
        if 'RebackStateUrl' in data:
            cls.RebackStateUrl = str(data['RebackStateUrl'])
        if 'code1' in data:
            cls.code1 = str(data['code1'])
        if 'code2' in data:
            cls.code2 = str(data['code2'])
            # setParameters.dataprint(cls.code2)
        if 'code3' in data:
            cls.code3 = str(data['code3'])
            # setParameters.dataprint(cls.code3)
        if 'code4' in data:
            cls.code4 = str(data['code4'])
            # setParameters.dataprint(cls.code4)
        if 'code5' in data:
            cls.code5 = str(data['code5'])
            # setParameters.dataprint(cls.code5)
        if 'code6' in data:
            cls.code6 = str(data['code6'])
            # setParameters.dataprint(cls.code6)
        if 'code7' in data:
            cls.code7 = str(data['code7'])
            # setParameters.dataprint(cls.code7)
        if 'code8' in data:
            cls.code8 = str(data['code8'])
            # setParameters.dataprint(cls.code8)
        if 'code9' in data:
            cls.code9 = str(data['code9'])
            # setParameters.dataprint(cls.code9)
        if 'code10' in data:
            cls.code10 = str(data['code10'])
            # setParameters.dataprint(cls.code10)
        if 'code11' in data:
            cls.code11 = str(data['code11'])
            # setParameters.dataprint(cls.code11)
        if 'code12' in data:
            cls.code12 = str(data['code12'])
            # setParameters.dataprint(cls.code12)
        if 'code13' in data:
            cls.code13 = str(data['code13'])
            # setParameters.dataprint(cls.code13)
        if 'code14' in data:
            cls.code14 = str(data['code14'])
            # setParameters.dataprint(cls.code14)
        if 'msg' in data:
            cls.msg = str(data['msg'])
        if 'QueryData' in data:
            cls.QueryData = str(data['QueryData'])
        if 'AddData' in data:
            cls.AddData = str(data['AddData'])
        if 'UpdateData' in data:
            cls.UpdateData = str(data['UpdateData'])
        if 'DeleteData' in data:
            cls.DeleteData = str(data['DeleteData'])
        if 'AcceptData' in data:
            cls.AcceptData = str(data['AcceptData'])
        if 'BatchAcceptData' in data:
            cls.BatchAcceptData = str(data['BatchAcceptData'])
        if 'AcceptBillData' in data:
            cls.AcceptBillData = str(data['AcceptBillData'])
        if 'RebackStateData' in data:
            cls.RebackStateData = str(data['RebackStateData'])


        cls.data = {}  # 保存传输data数据
        cls.return_json = None  # 保存响应信息
        cls.info = None  # 返回json格式的响应信息

        return cls

    @staticmethod
    def dataprint(data):
        print(data)
        # logger.info(data)

