import os
from time import sleep
from appium import webdriver

def before_feature(context, feature):
         context.driver = webdriver.Remote(
             command_executor='http://127.0.0.1:4723/wd/hub',
             desired_capabilities={
                 #'app' : app,
                 'platformName' : 'Android',
                 'platformVersion' : '6.0',
                 'deviceName' : '0010892885',
                 'browserName' : 'Chrome'
                 
                 #'udid' : '',
                 #'appActivity' : '',
                 #'appPackage' : ''
             }
         )
         

def after_feature(context, feature):
    sleep(1)
    context.driver.save_screenshot("features/reports/screen_final.png")
    context.driver.quit()