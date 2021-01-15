import datetime

from base import common
from base.common import localConfigHttp as configHttp


def Query(cls, setparam):
    cls.logger.info("第二步：设置访问的url")
    configHttp.set_url('E_Gdzc_3/gdzc/inputAction!listGridJson.action')
    cls.logger.info("第三步：设置发送请求的参数")
    string = setparam.QueryData
    # 第一种用eval
    # if 'true' in string:
    #     string = string.replace('true', 'True')
    # if 'false' in string:
    #     string = string.replace('false', 'False')

    # data = string
    # data = eval(data)
    # 第二种用json.loads
    # data = json.loads(string)

    configHttp.set_data(string)
    cls.logger.info("第三步：设置成功，发送的请求参数为： " + str(string))
    cls.logger.info("第四步：发送请求")
    response = configHttp.post()
    return response


def Add(cls, setparam):
    cls.logger.info("第二步：设置访问的url")
    configHttp.set_url('E_Gdzc_3/gdzc/inputAction!save_new.action')
    cls.logger.info("第三步：设置发送请求的参数")
    string = setparam.AddData
    configHttp.set_data(string)
    cls.logger.info("第三步：设置成功，发送的请求参数为： " + str(string))
    cls.logger.info("第四步：发送请求")
    response = configHttp.post()
    return response


def Update(cls, setparam):
    cls.logger.info("第二步：设置访问的url")
    configHttp.set_url('E_Gdzc_3/gdzc/repairAction!modify.action')
    cls.logger.info("第三步：设置发送请求的参数")
    string = setparam.UpdateData
    configHttp.set_data(string)
    cls.logger.info("第三步：设置成功，发送的请求参数为： " + str(string))
    cls.logger.info("第四步：发送请求")
    response = configHttp.post()
    return response


def Delete(cls, setparam):
    DeleteData = Query(cls, setparam).json()['root'][0]['change_guid']
    cls.logger.info("第二步：设置访问的url")
    url = 'E_Gdzc_3/gdzc/inputAction!delete.action?change_guid=20201225171350820_35032B7E7D104BB4B56ACA480478487D'
    url = url.replace('20201225171350820_35032B7E7D104BB4B56ACA480478487D', DeleteData)
    configHttp.set_url(url)
    cls.logger.info("第三步：设置发送请求的参数")
    # string = setparam.DeleteData+DeleteData  这里没有请求参数
    # configHttp.set_data(string)
    # cls.logger.info("第三步：设置成功，发送的请求参数为： " + str(string))
    cls.logger.info("第四步：发送请求")
    response = configHttp.post()
    return response


def checkResultQuery(cls, response, setparam):
    """检查结果
    check test result
    :return:
    """
    common.show_return_msg(response)

    cls.assertEqual(response.status_code, int(setparam.code1),
                    msg='Response code error,this time responsed code is：' + str(
                        '断言code为：%s' % setparam.code1 + '   响应code为：%s' % response.status_code))
    total = len(response.json()['root']) - 2

    if setparam.result == '0':
        # 先断言是否存在查询数据
        cls.assertNotEqual(total, 0, msg='Response  error，' + str('断言查询数据条数不为：0   响应结果为：%s' % total))
        print('断言查询数据条数不为：0   响应结果为：%s' % total)

        for i in range(total):
            # 断言入库单号
            info2 = response.json()['root'][i]['str_change_id']
            cls.assertEqual(info2, setparam.code2,
                            msg='Response  error，' + str('断言入库单号为：%s' % setparam.code2 + '   响应结果为：%s' % info2))
            print('断言入库单号为：%s' % setparam.code2 + '   响应结果为：%s' % info2)

            # 断言业务时间
            info3 = response.json()['root'][i]['change_time'][:10]
            cls.assertEqual(info3, setparam.code3,
                            msg='Response  error，' + str('断言业务时间为：%s' % setparam.code3 + '   响应结果为：%s' % info3))
            print('断言业务时间为：%s' % setparam.code3 + '   响应结果为：%s' % info3)

            # # 断言资产名称 需要新接口获取
            # info4 = response.json()['root'][i]['zicmc']
            # cls.assertEqual(info4, setparam.code4,
            #                 msg='Response  error，' + str('断言资产名称为：%s' % setparam.code4 + '   响应结果为：%s' % info4))
            # print('断言资产名称为：%s' % setparam.code4 + '   响应结果为：%s' % info4)

            # 断言供应商
            info5 = response.json()['root'][i]['provider_name']
            cls.assertEqual(info5, setparam.code5,
                            msg='Response  error，' + str('断言供应商为：%s' % setparam.code5 + '   响应结果为：%s' % info5))
            print('断言供应商为：%s' % setparam.code5 + '   响应结果为：%s' % info5)

            # # 断言资产价值 需要新接口获取
            # info6 = response.json()['root'][i]['repair_state']
            # cls.assertEqual(info6, setparam.code6,
            #                 msg='Response  error，' + str('断言资产价值为：%s' % setparam.code6 + '   响应结果为：%s' % info6))
            # print('断言资产价值为：%s' % setparam.code6 + '   响应结果为：%s' % info6)

            # 断言审核状态
            info7 = str(response.json()['root'][i]['is_check'])
            cls.assertEqual(info7, setparam.code7,
                            msg='Response  error，' + str('断言审核状态为：%s' % setparam.code7 + '   响应结果为：%s' % info7))
            print('断言审核状态为：%s' % setparam.code7 + '   响应结果为：%s' % info7)

            # 断言发票号
            info8 = response.json()['root'][i]['input_fapiao_hao']
            cls.assertEqual(info8, setparam.code8,
                            msg='Response  error，' + str('断言发票号为：%s' % setparam.code8 + '   响应结果为：%s' % info8))
            print('断言发票号为：%s' % setparam.code8 + '   响应结果为：%s' % info8)

    elif setparam.result == '1':
        setparam.assertGreaterEqual(total, int(3),
                                    msg='Response  error，' + str('断言查询数据条数大于：2   响应结果为：%s' % total))
        print('断言查询数据条数大于：2   响应结果为：%s' % total)

    elif setparam.result == '2':
        setparam.assertNotEqual(total, 0, msg='Response  error，' + str('断言查询数据条数不为：0   响应结果为：%s' % total))
        print('断言查询数据条数不为：0   响应结果为：%s' % total)
        for i in range(total):
            if setparam.code2 != 'null':
                info2 = response.json()['root'][i]['str_change_id']
                cls.assertEqual(info2, setparam.code2,
                                msg='Response  error，' + str('断言入库单号为：%s' % setparam.code2 + '   响应结果为：%s' % info2))
                print('断言入库单号为：%s' % setparam.code2 + '   响应结果为：%s' % info2)
            elif setparam.code3 != 'null':
                info3 = response.json()['root'][i]['change_time'][:10]
                cls.assertEqual(info3, setparam.code3,
                                msg='Response  error，' + str('断言业务时间为：%s' % setparam.code3 + '   响应结果为：%s' % info3))
                print('断言业务时间为：%s' % setparam.code3 + '   响应结果为：%s' % info3)
            # elif setparam.code4 != 'null':
            #     info4 = response.json()['root'][i]['zicmc']
            #     cls.assertEqual(info4, setparam.code4,
            #                     msg='Response  error，' + str('断言资产名称为：%s' % setparam.code4 + '   响应结果为：%s' % info4))
            #     print('断言资产名称为：%s' % setparam.code4 + '   响应结果为：%s' % info4)
            elif setparam.code5 != 'null':
                info5 = response.json()['root'][i]['provider_name']
                cls.assertEqual(info5, setparam.code5,
                                msg='Response  error，' + str('断言供应商为：%s' % setparam.code5 + '   响应结果为：%s' % info5))
                print('断言供应商为：%s' % setparam.code5 + '   响应结果为：%s' % info5)
            # elif setparam.code6 != 'null':
            #     info6 = response.json()['root'][i]['repair_state']
            #     cls.assertEqual(info6, setparam.code6,
            #                     msg='Response  error，' + str('断言维修状态为：%s' % setparam.code6 + '   响应结果为：%s' % info6))
            #     print('断言维修状态为：%s' % setparam.code6 + '   响应结果为：%s' % info6)
            elif setparam.code7 != 'null':
                info7 = str(response.json()['root'][i]['is_check'])
                cls.assertEqual(info7, setparam.code7,
                                msg='Response  error，' + str('断言审核状态为：%s' % setparam.code7 + '   响应结果为：%s' % info7))
                print('断言审核状态为：%s' % setparam.code7 + '   响应结果为：%s' % info7)
            elif setparam.code8 != 'null':
                info8 = response.json()['root'][i]['input_fapiao_hao']
                cls.assertEqual(info8, setparam.code8,
                                msg='Response  error，' + str('断言发票号为：%s' % setparam.code8 + '   响应结果为：%s' % info8))
                print('断言发票号为：%s' % setparam.code8 + '   响应结果为：%s' % info8)

    elif setparam.result == '3':
        setparam.assertEqual(total, 0, msg='Response  error，' + str('断言查询条数为：0' + '   响应结果条数为：%s' % total))
        print('断言查询条数为：0' + '   响应结果条数为：%s' % total)


def checkResultAdd(cls, response, setparam):
    """检查结果
    check test result
    :return:
    """
    common.show_return_msg(response)

    cls.assertEqual(response.status_code, int(setparam.code1),
                    msg='Response code error,this time responsed code is：' + str(
                        '断言code为：%s' % setparam.code1 + '   响应为：%s' % response.status_code))
    cls.assertEqual(response.json()['flag'], True, msg='Response code error,this time responsed code is：' + str(
        '断言flag为：True   响应为：%s' % response.json()['flag']))
    print('断言flag为：True   响应结果为：%s' % response.json()['flag'])

    response = Query(cls, setparam)

    total = len(response.json()['root']) - 2

    cls.assertNotEqual(total, 0, msg='Response  error，' + str('断言查询到新增数据不为：0   响应结果为：%s' % total))
    print('断言查询到新增数据不为：0   响应结果为：%s' % total)

    for i in range(total):
        # 断言入库单号
        info2 = response.json()['root'][i]['str_change_id']
        cls.assertEqual(info2, setparam.code2,
                        msg='Response  error，' + str('断言入库单号为：%s' % setparam.code2 + '   响应结果为：%s' % info2))
        print('断言入库单号为：%s' % setparam.code2 + '   响应结果为：%s' % info2)

        # 断言业务时间
        info3 = response.json()['root'][i]['change_time'][:10]
        cls.assertEqual(info3, setparam.code3,
                        msg='Response  error，' + str('断言业务时间为：%s' % setparam.code3 + '   响应结果为：%s' % info3))
        print('断言业务时间为：%s' % setparam.code3 + '   响应结果为：%s' % info3)

        # # 断言资产名称 需要新接口获取
        # info4 = response.json()['root'][i]['zicmc']
        # cls.assertEqual(info4, setparam.code4,
        #                 msg='Response  error，' + str('断言资产名称为：%s' % setparam.code4 + '   响应结果为：%s' % info4))
        # print('断言资产名称为：%s' % setparam.code4 + '   响应结果为：%s' % info4)

        # 断言供应商
        info5 = response.json()['root'][i]['provider_name']
        cls.assertEqual(info5, setparam.code5,
                        msg='Response  error，' + str('断言供应商为：%s' % setparam.code5 + '   响应结果为：%s' % info5))
        print('断言供应商为：%s' % setparam.code5 + '   响应结果为：%s' % info5)

        # # 断言资产价值 需要新接口获取
        # info6 = str(int(response.json()['root'][i]['row_zicjz']))
        # cls.assertEqual(info6, setparam.code6,
        #                 msg='Response  error，' + str('断言资产价值为：%s' % setparam.code6 + '   响应结果为：%s' % info6))
        # print('断言资产价值为：%s' % setparam.code6 + '   响应结果为：%s' % info6)

        # 断言审核状态
        info7 = str(response.json()['root'][i]['is_check'])
        cls.assertEqual(info7, setparam.code7,
                        msg='Response  error，' + str('断言审核状态为：%s' % setparam.code7 + '   响应结果为：%s' % info7))
        print('断言审核状态为：%s' % setparam.code7 + '   响应结果为：%s' % info7)

        # 断言发票号
        info8 = response.json()['root'][i]['input_fapiao_hao']
        cls.assertEqual(info8, setparam.code8,
                        msg='Response  error，' + str('断言发票号为：%s' % setparam.code8 + '   响应结果为：%s' % info8))
        print('断言发票号为：%s' % setparam.code8 + '   响应结果为：%s' % info8)

    print('断言存在新增数据')


def checkResultUpdate(cls, response, setparam):
    """检查结果
    check test result
    :return:
    """
    common.show_return_msg(response)

    cls.assertEqual(response.status_code, int(setparam.code1),
                    msg='Response code error,this time responsed code is：' + str(
                        '断言code为：%s' % setparam.code1 + '   响应code为：%s' % response.status_code))
    response = Query(cls, setparam)

    total = len(response.json()['root'])

    cls.assertNotEqual(total, 0, msg='Response  error，' + str('断言查询数据条数不为：0   响应结果为：%s' % total))
    print('断言查询数据条数不为：0   响应结果为：%s' % total)

    for i in range(total):
        # 断言故障现象
        info5 = response.json()['root'][i]['guzhangxx']
        cls.assertEqual(info5, setparam.code5,
                        msg='Response  error，' + str('断言故障现象为：%s' % setparam.code5 + '   响应结果为：%s' % info5))
        print('断言故障现象为：%s' % setparam.code5 + '   响应结果为：%s' % info5)

        # 断言报修时间
        info6 = response.json()['root'][i]['startTime'][:10]
        cls.assertEqual(info6, setparam.code6,
                        msg='Response  error，' + str('断言报修时间为：%s' % setparam.code6 + '   响应结果为：%s' % info6))
        print('断言报修时间为：%s' % setparam.code6 + '   响应结果为：%s' % info6)

        # 断言紧急程度
        info7 = response.json()['root'][i]['repair_emergency']
        cls.assertEqual(info7, setparam.code7,
                        msg='Response  error，' + str('断言紧急程度为：%s' % setparam.code7 + '   响应结果为：%s' % info7))
        print('断言紧急程度为：%s' % setparam.code7 + '   响应结果为：%s' % info7)

        # 断言维修方式
        info8 = response.json()['root'][i]['repair_way']
        cls.assertEqual(info8, setparam.code8,
                        msg='Response  error，' + str('断言维修方式为：%s' % setparam.code8 + '   响应结果为：%s' % info8))
        print('断言维修方式为：%s' % setparam.code8 + '   响应结果为：%s' % info8)

        # 断言备注
        info9 = response.json()['root'][i]['remark']
        cls.assertEqual(info9, setparam.code9,
                        msg='Response  error，' + str('断言备注为：%s' % setparam.code9 + '   响应结果为：%s' % info9))
        print('断言备注为：%s' % setparam.code9 + '   响应结果为：%s' % info9)


def checkResultDelete(cls, response, setparam):
    """检查结果
    check test result
    :return:
    """
    common.show_return_msg(response)

    cls.assertEqual(response.status_code, int(setparam.code1),
                    msg='Response code error,this time responsed code is：' + str(
                        '断言code为：%s' % setparam.code1 + '   响应为：%s' % response.status_code))
    cls.assertEqual(response.json()['flag'], True, msg='Response code error,this time responsed code is：' + str(
        '断言flag为：True   响应为：%s' % response.json()['flag']))
    print('断言flag为：True   响应结果为：%s' % response.json()['flag'])
    response = Query(cls, setparam)

    total = len(response.json()['root']) - 2

    cls.assertEqual(total, 0, msg='Response  error，' + str('断言查询数据条数为：0   响应结果为：%s' % total))
    print('断言查询数据条数为：0   响应结果为：%s' % total)




