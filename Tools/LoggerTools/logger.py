# -*- coding: utf-8 -*-
"""
@Time    : 2019/12/13 14:47
@Author  : shaopengwei@hotmail.com
@File    : logger.py
"""

import logging
import logging.handlers

class Logger:
    """
    @desc: class logger
    @feature1: 实现debug/info/warning/fatal日志的分开打印
    @feature2: 实现handler多样性
    """
    _logger = None

    def __init__(self, name, log_dir, formatter, level = 'NOTSET'):
        """
        @:param self
        """
        self._logger = logging.getLogger(name)
        log_formatter = logging.Formatter(formatter)
        handler_list = []
        if logging._levelNames[level] <= logging.CRITICAL:
            handler_list.append(self._gen_handler(logging.CRITICAL, log_dir + '.fatal', log_formatter, 'D', 1, 10))
        if logging._levelNames[level] <= logging.ERROR:
            handler_list.append(self._gen_handler(logging.ERROR, log_dir + '.error', log_formatter, 'D', 1, 10))
        if logging._levelNames[level] <= logging.WARNING:
            handler_list.append(self._gen_handler(logging.WARNING, log_dir + '.warning', log_formatter, 'D', 1, 10))
        if logging._levelNames[level] <= logging.INFO:
            handler_list.append(self._gen_handler(logging.INFO, log_dir + '.info', log_formatter, 'D', 1, 10))
        if logging._levelNames[level] <= logging.DEBUG:
            handler_list.append(self._gen_handler(logging.DEBUG, log_dir + '.debug', log_formatter, 'D', 1, 10))
        for item in handler_list:
            self._logger.addHandler(item)
        self._logger.setLevel(level)


    def _gen_handler(self, level, log_dir, formatter, when, interval, backupCount):
        """
        :param level:
        :param log_dir:
        :param when:
        :param interval:
        :param backupCount:
        :return: handler
        """
        filter = logging.Filter()
        filter.filter = lambda record: record.levelno == level
        handler = logging.handlers.TimedRotatingFileHandler(filename = log_dir, when = when,
                                        interval = interval, backupCount = backupCount, encoding = 'utf-8')
        handler.addFilter(filter)
        handler.setLevel(level)
        handler.setFormatter(formatter)
        return handler


    def debug(self, msg):
        """
        :param msg:
        :return:
        """
        self._logger.debug(msg)


    def info(self, msg):
        """
        :param msg:
        :return:
        """
        self._logger.info(msg)


    def warning(self, msg):
        """
        :param msg:
        :return:
        """
        self._logger.warning(msg)


    def error(self, msg):
        """
        :param msg:
        :return:
        """
        self._logger.error(msg)


    def critical(self, msg):
        """
        :param msg:
        :return:
        """
        self._logger.critical(msg)