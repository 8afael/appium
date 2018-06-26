from behave import *
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

@given('authentication')
def step_impl(context):
    context.driver.get('https://admin:admin@ccstore-test-zbna.oracleoutsourcing.com/')
    sleep(10)

@given('click in FAQ')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="clHeader"]/div/nav/div[2]/div[1]/ul/li[1]/label/span[4]').click()
    context.driver.find_element_by_xpath('//*[@id="clHeader"]/div/nav/div[2]/div[2]/div/ul[2]/li[7]/a/span[2]').click()
    context.driver.find_element_by_xpath('//*[@id="accordion-faq"]/div[20]/div[1]').click()
    context.driver.find_element_by_xpath('//*[@id="accordion-faq"]/div[18]/div[1]').click()

@then('text should be in the results')
def step_impl(context):
    sleep(10)
    body = '<html><body><span>reuse</span></body></html>'
    response = HtmlResponse(url='https://ccstore-test-zbna.oracleoutsourcing.com/', body=body)
    #Selector(response=response).xpath
    text_app = response.selector.xpath('#faq-collapse-17 > div:nth-child(1) > p:nth-child(1)').extract()
    #text_app = context.driver.find_element_by_xpath('#faq-collapse-17 > div:nth-child(1)')
    print text_app
    text_origin = 'CoreLogic enables you to reuse your credit/debit card for future payments. While your credit/debit card is available for future orders, CoreLogic does not store this information. All card information is stored with our payment processor in a secured environment.'
    print '============================================================================================'
    print text_app
    els = context.driver.find_elements_by_xpath(text_app)
    context.assertEqual(text_origin, els[0].text)



