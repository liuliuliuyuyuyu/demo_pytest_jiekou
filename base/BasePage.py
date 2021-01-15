# coding=UTF-8

import datetime
import requests
import readConfig
from base.common import localConfigHttp as configHttp


class BasePage:
    @staticmethod
    def login():
        # print("第一步：设置header(token等)")
        # self.logger.info("第一步：设置header(token等)")
        token = readConfig.ReadConfig().get_headers("User-Agent")
        # set headers         设置请求头
        headers = {
            "User-Agent": str(token),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'  # 注意这里因为不是支持所有的格式，要在请求头中标名传输格式
        }
        url = 'http://114.115.205.214:8686/Ecan_Platform/loginAction!loginSystem.action'
        # url = 'http://127.0.0.1:8080/Ecan_Platform/loginAction!loginSystem.action'
        # cookies = localReadConfig.get_headers("cookies")
        data = {
            "hbdwbh": "3502",
            "userid": "00",
            "encodePwd": "SlNRSRNa90ieLOrgCIZfRZii2fVkI+SrAOKj3ecwAkZoMQAFLrk84kCFaQpnkMFSoP6h4wzdP0zEJYmECTvP8uhcQhNz57vCL+mwu/N5rf1fdAFO32fRZLzAHhaPZwXYrGCi33anRvLaup1dOeX4A7rCf0v2ptJyWpgx7W+FHg==",
            "operatorTime": str(datetime.datetime.now())[:10],
            "privateKey": "MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAI1FLM5y2qAmTeKDwDyg+fPedO1STmjSkQZmuLeX/cQPeb9SR8fRxRkaYEibSXs5lVQSiN9Oc048ba6ItsEZ61oBbOSBdCoLwW7h29K0x9xiXFgbjt41vpNVKcpAcLJj/0gUG8WRCLV02MDKagTMUzcAJEZzMPNcAZMzKqd8KrfpAgMBAAECgYAZRIgxHOXxwygnHb2imoBamC19zTztDsyVwoXDgNII4WO7TrI8EU8ZoFgcZHoOKkyFTxNgLZ3+HlzX3OgjPcmUeV5oQVRuNydsG3o8Vlii5xGkbg89aubHoD1Fl3A5rM8FQ9O6mIfTn/GkNlQhj0dpbMT+16NpBEcazDhdq0rCKQJBANCjU3op4vKo2rzT/PVvwCy8KlRr9ZCcr4m3kUnwkYWcvtqjJcPFg+yKZ3QFmCLGFNwCIneAvATfN6yUqGenRxsCQQCtVt/2HAg1wc43rIHUBswQ1iH9veRGK7/pkJUyTOmuGtugnkQSOMA8O+nIeSFqw5XMSV9UFpWbAg46vAr32dlLAkAvPx0zR/L90qEeK79X8UOKnd3UGlKUufbCcBB1twWtRS6vIkz2BW93jGwbCP1HuqWUoOMfPsbVL5tS+KMePfJLAkA5IqOb2c2S+pjgnQoGO19URWDa5Jaz0oPllvS2qcd0zgGKxeAmKXKj6BO9MsAjEujzd1PmwbL6bwkFrynmXHZVAkEAt6BziC21nGZ4Jx6azF3LcPFEWtcqHUEewZRnFGTCui/DkS/4o//1MeC1mhQgoRBK0cresa+l3Kz2bDzKySWfKQ==",
            "task": "encode_pwd",
            "weining_sso_userid": ""
        }
        response1 = requests.post(url=url, data=data, headers=headers)
        # response2 = session.get(url=url2,headers=headers)
        # localReadConfig.set_headers("cookies",response.cookies.get_dict())
        dic = response1.cookies.get_dict()
        dic['ys-edit_product_pmml_win'] = 'o%3Awidth%3Dn%253A1348%5Eheight%3Dn%253A662%5Ex%3Dn%253A516%5Ey%3Dn%253A210'
        # dic['JSESSIONID'] = response2.cookies.get_dict()['JSESSIONID']
        configHttp.set_headers(headers)
        configHttp.set_cookies(dic)

if __name__ == '__main__':
    dic = BasePage().login()
    print(dic)
    print(type(dic))


