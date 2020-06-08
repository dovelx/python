#!/usr/bin/env python
# -*- coding:GBK -*-
__author__ = ''

import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
import mimetypes
import os

def host():
    config = configparser.ConfigParser()
    host_config_file = './case/hosts.conf'
    config.read(host_config_file, encoding='utf-8')

    ip = config.get('host', 'ip')
    port = config.get('host', 'port')
    path = ip+":"+port
    return path