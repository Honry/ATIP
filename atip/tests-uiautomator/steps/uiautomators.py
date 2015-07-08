# Copyright (c) 2014 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this list
#   of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Yang, Yunlong <yunlongx.yang@intel.com>

import os
import sys
import time
import subprocess
import json
import signal
from atip.common import common
from uiautomator import *
reload(sys)
sys.setdefaultencoding('utf-8')
DEFAULT_CMD_TIMEOUT = 60

class UIAutomator(common.APP):

    def __init__(self, app_config=None, app_name=None,
                 apk_pkg_name=None, apk_activity_name=None):
        self.app_name = app_name
        app_config_str = json.dumps(app_config).replace(
                "TEST_APP_NAME", self.app_name)
        if apk_pkg_name and apk_activity_name:
            app_config_str = json.dumps(app_config).replace(
                app_config["TEST_PKG_NAME"], apk_pkg_name).replace(
                app_config["TEST_ACTIVITY_NAME"], apk_activity_name)
        self.app_config = json.loads(app_config_str)
        self.device_id = self.app_config["platform"]["device"]
        self.adb = "adb -s %s shell" % self.device_id
        self.d = Device(self.device_id)
        
    def launch_app(self):
        cmd = self.adb + \
                " am start -n " + \
                self.app_config["TEST_PKG_NAME"] + "/" + \
                self.app_config["TEST_PKG_NAME"] + "." + \
                self.app_config["TEST_ACTIVITY_NAME"]
        try:
            (return_code, output) = self.doCMD(cmd)
            if return_code == 0:
                self.d.screen.on()
            else:
                print("\n".join(output))
                return False
        except Exception as e:
            return False
        return self.checkLauncher()

    def quit(self):
        check_cmd = self.adb + \
                " ps | grep " + \
                self.app_config["TEST_PKG_NAME"]
        stop_cmd = self.adb + \
                " am force-stop " + \
                self.app_config["TEST_PKG_NAME"]
        (return_code, output) = self.doCMD(check_cmd)
        if return_code == 0 and output:
            self.doCMD(stop_cmd)
            if self.doCMD(check_cmd)[1] != []:
                print("Please check your cmd: %s" % stop_cmd)


    def doCMD(self, cmd, time_out=DEFAULT_CMD_TIMEOUT):
        # print("Doing CMD: [ %s ]" % cmd)
        pre_time = time.time()
        output = []
        cmd_return_code = 1
        cmd_proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

        while True:
            output_line = cmd_proc.stdout.readline().strip("\r\n")
            cmd_return_code = cmd_proc.poll()
            elapsed_time = time.time() - pre_time
            if cmd_return_code is None:
                if elapsed_time >= time_out:
                    self.killProcesses(ppid=cmd_proc.pid)
                    # print("Timeout to exe CMD")
                    return (None, None)
            elif output_line == '' and cmd_return_code is not None:
                break

            output.append(output_line)
        if cmd_return_code != 0:
            pass
            # print("Fail to exe CMD")

        return (cmd_return_code, output)

    def killProcesses (self, ppid=None):
        ppid = str(ppid)
        pidgrp = []

        def GetChildPids(ppid):
            command = "ps -ef | awk '{if ($3 ==%s) print $2;}'" % str(ppid)
            pids = os.popen(command).read()
            pids = pids.split()
            return pids

        pidgrp.extend(GetChildPids(ppid))
        for pid in pidgrp:
            pidgrp.extend(GetChildPids(pid))

        pidgrp.insert(0, ppid)
        while len(pidgrp) > 0:
            pid = pidgrp.pop()
            try:
                os.kill(int(pid), signal.SIGKILL)
                return True
            except OSError:
                try:
                    os.popen("kill -9 %d" % int(pid))
                    return True
                except Exception:
                    return False

    def checkLauncher(self):
        currentPackageName = self.d.info["currentPackageName"]
        if currentPackageName == self.app_config["TEST_PKG_NAME"]:
            return True
        return False

    def registerWatcher(self, watcherName, whenText1, clickText, whenText2=None):
        if watcherName in self.d.watchers:
            self.d.watcher(watcherName).remove()
        if whenText2:
            self.d.watcher(watcherName).when(text=whenText1).when(whenText2) \
                                        .click(text=clickText)
        else:
            self.d.watcher(watcherName).when(text=whenText1) \
                                        .click(text=clickText)            

    def removeAllWatchers(self):
        self.d.watchers.remove()

    def resetAllWatchers(self):
        self.d.watchers.reset()

    def runAllWatchers(self):
        self.d.watchers.run()

    def selectTvObjectBy(self, value, key="textContains"):
        if key == "text":
            return self.d(text=value, className='android.widget.TextView')
        elif key == "textContains":
            return self.d(textContains=value, className='android.widget.TextView')
        elif key == "description":
            return self.d(description=value, className='android.widget.TextView')
        elif key == "descriptionContains":
            return self.d(descriptionContains=value, className='android.widget.TextView')
        else:
            return None

    def selectBtnObjectBy(self, value, key="textContains"):
        if key == "text":
            return self.d(text=value, className='android.widget.Button')
        elif key == "textContains":
            return self.d(textContains=value, className='android.widget.Button')
        elif key == "description":
            return self.d(description=value, className='android.widget.Button')
        elif key == "descriptionContains":
            return self.d(descriptionContains=value, className='android.widget.Button')
        else:
            return None        
        
    def selectEdtObjectBy(self, value, key="textContains"):
        if key == "text":
            return self.d(text=value, className='android.widget.EditText')
        elif key == "textContains":
            return self.d(textContains=value, className='android.widget.EditText')
        elif key == "description":
            return self.d(description=value, className='android.widget.EditText')
        elif key == "descriptionContains":
            return self.d(descriptionContains=value, className='android.widget.EditText')
        else:
            return None

    def selectViewObjectBy(self, value):
        return self.d(description=value, className='android.view.View')

    def selectWebObjectBy(self, web_name):
        return self.d(description=web_name, className='android.webkit.WebView')            

    def getTvObjectInfo(self, ob):
        if ob.exists:
            return ob.info["text"]
        return None

    def clickBtnObject(self, ob):
        if ob.exists:
            ob.click()
            return True
        return False

    def setEditText(self, ob, text):
        if ob.exists:        
            ob.set_text(text)
            return True
        return False    


def launch_app_by_name(
        context, app_name, apk_pkg_name=None, apk_activity_name=None):
    if not context.uiautomator_config:
        assert False

    if app_name in context.apps:
        context.apps[app_name].quit()
    context.apps.update(
        {app_name: UIAutomator(context.uiautomator_config, app_name, apk_pkg_name, apk_activity_name)})
    context.app = context.apps[app_name]
    if not context.app.launch_app():
        assert False
    assert True     