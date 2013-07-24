#!/usr/bin/env python
#-*- coding:utf-8 -*-

import logging
import threading
import time

import rflib.ipc.IPC as IPC
import rflib.ipc.MongoIPC as MongoIPC
from rflib.ipc.RFProtocol import *
from rflib.ipc.RFProtocolFactory import RFProtocolFactory
from rflib.defs import *
from rflib.types.Match import *
from rflib.types.Action import *
from rflib.types.Option import *


class RFMonitor(RFProtocolFactory, IPC.IPCMessageProcessor):
    """Monitors all the controller instances for failiure"""
    def __init__(self, *arg, **kwargs):
        self.controllers = dict()
        self.ipc = MongoIPC.MongoIPCMessageService(MONGO_ADDRESS,
                                                   MONGO_DB_NAME,
                                                   RFMONITOR_ID,
                                                   threading.Thread,
                                                   time.sleep)
        self.ipc.listen(RFMONITOR_RFPROXY_CHANNEL, self, self, False)
        self.log = logging.getLogger("rfmonitor")
        self.log.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
        self.log.addHandler(ch)

    def process(self, _from, to, channel, msg):
        type_ = msg.get_type()
        if type_ == CONTROLLER_REGISTER:
            self.controllers[str(msg.get_ct_addr()) + ':'
                             + str(msg.get_ct_port())] = msg.get_ct_role()
            self.log.info("A %s controller at %s:%s is up", msg.get_ct_role(),
                          msg.get_ct_addr(), msg.get_ct_port())

    def test():
        pass


class Monitor(object):
    """Monitors each controller individually"""
    def __init__(self, host, port, callback_time):
        super(Monitor, self).__init__()
        self.host = host
        self.port = port
        self.callback_time = callback_time

    def start_test():
        pass

    def stop_test():
        pass

    def schedule_test():
        pass

    def run_test():
        pass

if __name__ == "__main__":
    description = 'RFMonitor monitors RFProxy instances for failiure'
    epilog = 'Report bugs to: https://github.com/routeflow/RouteFlow/issues'
    RFMonitor()
