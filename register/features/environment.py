
from splinter.browser import Browser
#from django.test.simple import DjangoTestSuiteRunner

def before_all(context):
#    context.runner = DjangoTestSuiteRunner()
    context.browser = Browser()

def after_all(context):
    context.browser.quit()
    context.browser = None

