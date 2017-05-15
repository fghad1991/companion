__author__ = 'JJLanMo'

class appium():
    def start(self,host,port,bootstrap_port,session_override):
        errormsg = ""
        appium_server_url = ""
        appium_log_path = ""

        # appium - a 127.0.0.1 - p4726 - -bootstrap - port 4780 - -session - override - -log "E:/appium" - -command - timeout 600
        if  self.port_is_free(host,port):
            cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' --bootstrap-port ' + str(
            bootstrap_port) + ' --session-override --log ' + '"' + appium_log_path + '" --command-timeout 600'
        else:
            print ("a")(port)