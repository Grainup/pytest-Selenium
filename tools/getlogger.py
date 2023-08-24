# 导包
import logging.handlers


# 定义类
from config import con


class GetLogger:
    logger = None

    # 获取logger的方法（类方法）
    @classmethod
    def get_logger(cls):
        # 判断logger是否存在，如存在则直接返回（单例模式）
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger("admin")  # admin可不设置，默认为root

            # 设置日志器级别
            cls.logger.setLevel(logging.INFO)

            # 获取控制台处理器
            sh = logging.StreamHandler()

            """
                filename: 文件路径（不要使用时间作为文件名称，否则只会生成一个文件）
                when: 生成文件的时间单位
                interval: 生成文件的时间间隔
                backupCount: 保留的文件数量，会保留最新的文件数量，将旧的删除
                encoding: 字符集
            """
            # 获取文本处理器（以时间分割）
            th = logging.handlers.TimedRotatingFileHandler(filename=f"{con.BASE_DIR}/log/logtime_shopping.log", when="M",
                                                           interval=1, backupCount=30, encoding="utf-8")

            # 添加格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            sh.setFormatter(fm)
            th.setFormatter(fm)

            # 将处理器添加到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)

            # 返回日志器
            return cls.logger

        # 返回日志器
        return cls.logger
