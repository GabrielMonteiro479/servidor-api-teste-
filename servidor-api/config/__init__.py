import json
import signal
import sys, os
import threading
import time
import atexit
import requests
import socket


class ServiceConfig(object):
    __api_name = None
    __api_socket = None
    __api_port = None
    __eureka_url = 'http://172.28.97.46:8761/eureka/apps/'

    @staticmethod
    def __get_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))
        return str(s.getsockname()[0])

    @classmethod
    def configure(cls, api_name, port):
        cls.__api_name = api_name
        cls.__api_socket = cls.__get_ip()
        cls.__api_port = str(port)

        if os.getenv('ENV') and os.getenv('ENV') != 'test':
            while cls.register() is False:
                time.sleep(5)

    @classmethod
    def register(cls):
        print('Trying to register service: %s' % cls.__api_name)
        register_app = cls.__eureka_url + cls.__api_name
        data = {
            "instance": {
                "hostName": cls.__api_socket,
                "app": cls.__api_name,
                "ipAddr": cls.__api_socket,
                "vipAddress": cls.__api_name,
                "status": "UP",
                "port": {"$": cls.__api_port, "@enabled": "true"},
                "securePort": {"$": "443", "@enabled": "false"},
                "homePageUrl": "http://" + cls.__api_socket + ":" + cls.__api_port,
                "statusPageUrl": "http://" + cls.__api_socket + ":" + cls.__api_port + "/info/",
                "healthCheckUrl": "http://" + cls.__api_socket + ":" + cls.__api_port + "/health/",
                "dataCenterInfo": {
                    "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
                    "name": "MyOwn"
                },
                "metadata": {
                    "instanceId": cls.__api_socket + ":" + cls.__api_name + ":" + cls.__api_port
                }
            }
        }
        headers = {'Content-Type': 'application/json'}

        r = requests.post(register_app, data=json.dumps(data), headers=headers)
        if r.status_code == 204:
            cls.__configure_de_register()
            cls.__start_heartbeat()
            print('Service %s successfully registered!' % cls.__api_name)
            print("IP Address: " + cls.__api_socket)
            return True
        else:
            print('Failed to register service: %s' % cls.__api_name)
            return False

    @classmethod
    def __configure_de_register(cls):
        atexit.register(cls.de_register)
        signal.signal(signal.SIGINT, cls.__signal_handler)
        signal.signal(signal.SIGTERM, cls.__signal_handler)

    @classmethod
    def de_register(cls):
        if not cls.__api_socket:
            raise RuntimeError('No service registered.')

        delete = cls.__eureka_url + cls.__api_name + '/' + cls.__api_socket + ':' + \
                 cls.__api_name + ':' + cls.__api_port
        data = {}
        headers = {}
        response = requests.delete(delete, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    def __signal_handler(signum, frame):
        print('Signal handler called with signal', signum)
        ServiceConfig.de_register()
        sys.exit(0)
        os.kill()

    @classmethod
    def heartbeat(cls):
        put = cls.__eureka_url + cls.__api_name + '/' + cls.__api_socket + ':' + cls.__api_name + ':' + cls.__api_port
        data = {}
        headers = {}

        while True:
            time.sleep(30)
            response = requests.put(put, data=json.dumps(data), headers=headers)
            if not response.status_code == 200:
                ServiceConfig.register()

    @classmethod
    def __start_heartbeat(cls):
        threads = []
        t = threading.Thread(target=cls.heartbeat)
        threads.append(t)
        t.daemon = True
        t.start()
