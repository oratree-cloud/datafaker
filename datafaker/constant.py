#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__version__ = '0.0.9'

# 每次插入mysql数据条数
BATCH_SIZE = 1000

# 产生流数据间隔时间(秒)
DEFAULT_INTERVAL = 1

# 输出数据格式
TEXT_FORMAT = 'text'
JSON_FORMAT = 'json'
DEFAULT_FORMAT = TEXT_FORMAT

# 语言类型
DEFAULT_LOCALE = 'zh_CN'

# ENUM类型，从文件中读取枚举值
ENUM_FILE = 'file://'

# 判断哪些需要加上引号
STR_TYPES = ['date', 'time', 'datetime', 'char', 'varchar', 'tinyblob',
             'tinytext', 'text', 'mediumtext', 'longtext', 'string']


INT_TYPES = ['tinyint', 'smallint', 'mediumint', 'int', 'integer', 'bigint', ]

FLOAT_TYPES = ['float', 'double', 'decimal', ]
