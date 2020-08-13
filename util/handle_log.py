# coding=utf-8
import os
import sys
import logbook
import os

sys.path.append('../')
sys.path.append('D:/ApiAuto/Apiautomation')
curPath = os.path.abspath(os.path.dirname(__file__))
BasePath = curPath[:curPath.find("Apiautomation\\") + len("Apiautomation\\")]
from logbook import Logger, StreamHandler, FileHandler, TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler


def log_type(record, handler):
    log = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
        date=record.time,  # 日志时间
        level=record.level_name,  # 日志等级
        filename=os.path.split(record.filename)[-1],  # 文件名
        func_name=record.func_name,  # 函数名
        lineno=record.lineno,  # 行号
        msg=record.message  # 日志内容
    )
    return log


# 日志存放路径
LOG_DIR = BasePath + '/log'
print(LOG_DIR)
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
# 日志打印到屏幕
log_std = ColorizedStderrHandler(bubble=True)
log_std.formatter = log_type
# 日志打印到文件
log_file = TimedRotatingFileHandler(
    os.path.join(LOG_DIR, '%s.log' % 'log'), date_format='%Y-%m-%d', bubble=True, encoding='utf-8')
log_file.formatter = log_type

# 脚本日志
run_log = Logger("global_log")


def init_logger():
    logbook.set_datetime_format("local")
    run_log.handlers = []
    run_log.handlers.append(log_file)
    run_log.handlers.append(log_std)
    return ""


'''
日志等级：
critical    严重错误，会导致程序退出
error	    可控范围内的错误
warning	    警告信息
notice	    大多情况下希望看到的记录
info	    大多情况不希望看到的记录
debug	    调试程序时详细输出的记录
'''
# 实例化，默认调用
logger = init_logger()

# if __name__ == "__main__":
#     run_log.info("测试日志模块")
