# -*- coding: utf-8 -*-
"""
@Time    : 2019/12/26 20:56
@Author  : shaopengwei@baidu.com
@File    : logger_test.py
"""
import sys
sys.path.append('../lib/')
from logger import Logger

if __name__ == "__main__":
    logger = Logger(__name__, './log/test',
                    '%(asctime)s %(levelname)s %(name)s %(filename)s %(message)s',
                    'DEBUG')
    logger.debug('test debug')
    logger.info('test info')
    logger.warning('test warning')
    logger.error('test error')
    logger.critical('test fatal')