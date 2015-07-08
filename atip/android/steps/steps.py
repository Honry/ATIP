# Copyright (c) 2015 Intel Corporation.
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

import android
import time
import sys
from behave import step
reload(sys)
sys.setdefaultencoding('utf-8')


@step(u'launch "{app_name}" on android')
def launch_app_by_name(context, app_name):
    android.launch_app_by_name(context, app_name)

@step(u'I launch "{app_name}" with "{apk_pkg_name}" and "{apk_activity_name}" on android')
def launch_app_by_names(context, app_name, apk_pkg_name, apk_activity_name):
    android.launch_app_by_name(
        context,
        app_name,
        apk_pkg_name,
        apk_activity_name)

@step(u'I wait {n:d} seconds')
def wait_senconds(context, n):
    time.sleep(n)    

@step(u'I force to run all watchers')
def force_run_watchers(context):
	context.app.runAllWatchers()

@step(u'I remove all watchers')
def clear_all_watchers(context):
	context.app.removeAllWatchers()

@step(u'I register watcher "{watcher_name}" when "{when_text}" click "{click_text}"')
def register_watcher_when(context, watcher_name, when_text, click_text):
	context.app.registerWatcher(watcher_name, when_text, click_text)

@step(u'I register watcher2 "{watcher_name}" when "{when_text1}" and "{when_text2}" click "{click_text}"')
def register_watcher_when2(context, watcher_name, when_text1, when_text2, click_text):
	context.app.registerWatcher(watcher_name, when_text1, click_text, when_text2)

@step(u'I should see text "{text_name}"')
def select_text_object(context, text_name):
	assert context.app.selectTvObjectBy(text_name).exists

@step(u'I should see web "{web_name}"')
def select_web_object(context, web_name):
	assert context.app.selectWebObjectBy(web_name).exists

@step(u'I should see view "{view_name}"')
def select_view_object(context, view_name):
	assert context.app.selectViewObjectBy(view_name).exists

@step(u'I click "{button_name}"')
def click_button_object(context, button_name):
	ob = context.app.selectBtnObjectBy(button_name)
	if ob.exists:
		assert context.app.clickBtnObject(ob)
	else:
		ob = context.app.selectImageBtnObjectBy(button_name)
		assert ob.exists
		assert context.app.clickBtnObject(ob)

@step(u'I edit text "{edit_text}" to input "{text}"')
def set_edittext_object(context, edit_text, text):
	ob = context.app.selectEdtObjectBy(edit_text)
	assert ob.exists
	assert context.app.setEditText(ob, text)

@step(u'I edit index "{which}" text to input "{text}"')
def set_edittext_object(context, which, text):
	ob = context.app.selectEdtObjectBy("")[int(which)]
	assert ob.exists
	assert context.app.setEditText(ob, text)
