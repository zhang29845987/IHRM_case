import logging
import os
# 获取项目根目录
from logging.handlers import TimedRotatingFileHandler

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
from log import data_path

print(os.path.dirname(os.path.abspath(__file__)))


# 初始化日志配置
def init_log_config():
    #添加日志器 默认日志root
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)

    #处理器 输出到控制台
    shl=logging.StreamHandler()

    #处理器输出到文件到指定路径，when以小时为单位存文件，interval一个小时存一个文件，backcount默认保存全部文件，encoding 使用utf8编码格式
    trfhl=TimedRotatingFileHandler(filename=data_path()+"/mylog.log",when="h",interval=1,backupCount=0,encoding="utf8")

    #格式化器
    fmter=logging.Formatter(fmt="%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s")

    #处理器添加格式化器
    shl.setFormatter(fmter)
    # 处理器添加格式化器
    trfhl.setFormatter(fmter)

    #日志器添加处理器
    logger.addHandler(shl)
    #日志器添加处理器
    logger.addHandler(trfhl)