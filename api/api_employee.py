# 导包
import requests
# 导入公用方法
import api


# api层

# 创建员工类
class employee(object):
    # 初始类
    def __init__(self):
        # 设置添加员工接口地址
        self.post_url = api.url + "/api/sys/user"
        # 设置修改与员工删除员工查询员工接口地址
        self.url = api.url + "/api/sys/user/{}"

    # 添加员工数据从外部接收三个参数
    def post_employee(self, username, mobile, workNumber):
        # 以字段的形式接收外部传入的值
        data = {"username": username, "mobile": mobile, "workNumber": workNumber}
        # 把post请求方法返回到函数中方便外部调用函数
        return requests.post(url=self.post_url, json=data, headers=api.Headers)

    # 修改员工
    def put_employee(self, username):
        # 外部调用方法传入想要修改的数据
        data = {"username": username}
        # 把put请求方法返回到函数中方便外部调用
        # api.user_id的意思吧添加好的用户id保存到api __init__这个文件中的user_id中的变量调用出来
        return requests.put(url=self.url.format(api.user_id), json=data, headers=api.Headers)

    # 查询员工
    def get_employee(self):
        # 调用存储的api.user_id来查询员工并把结果返回到查询员工函数中
        return requests.get(url=self.url.format(api.user_id), headers=api.Headers)

    # 删除员工
    def delete_employee(self):
        # 调用存储的api.user_id来删除员工并把接口返回到删除员工的函数中
        return requests.delete(url=self.url.format(api.user_id), headers=api.Headers)

    # 测试代码
# if __name__ == '__main__':
#     cc=employee()
#     r=cc.post_employee("叮叮车嘤嘤嘤","18279795858","4466")
#     print(r.text)
