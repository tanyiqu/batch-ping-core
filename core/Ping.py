import subprocess
import re


class Ping:

    def __init__(self, ip):
        self.ip = ip
        pass

    def test_ping(self):
        ftp_ret = subprocess.Popen(
            'ping %s -n 2' % self.ip, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        ret = ftp_ret.stdout.read()

        str_ret = ret.decode("gbk")

        # print()
        # print(str_ret)
        # print()

        # 检查输出里面有没有TTL，有的话就先认为连通
        ret_s = re.search("TTL", str_ret)
        if ret_s:
            return True
        return False

    pass
