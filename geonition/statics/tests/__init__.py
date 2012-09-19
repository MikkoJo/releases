from django.conf import global_settings, settings
from django.test.simple import DjangoTestSuiteRunner
from django.test.simple import build_suite, build_test
from django.utils import unittest

from optparse import make_option

class GeonitionTestSuiteRunner(DjangoTestSuiteRunner):
    # option_list = (
        # make_option('--modeltranslation', action='store_true', default=False,
            # help='Test modeltranslation application, default is False'),
    # )
    # def __init__(self, verbosity=1, interactive=True, failfast=True, modeltranslation=False, **kwargs):
        # super(GeonitionTestSuiteRunner, self).__init__(
            # verbosity=verbosity, interactive=interactive, failfast=failfast, **kwargs)
        # self.modeltranslation = modeltranslation
#         
    def setup_test_environment(self, **kwargs):
        super(GeonitionTestSuiteRunner, self).setup_test_environment(**kwargs)
        
        self.old_login_redict_url = getattr(settings, 'LOGIN_REDIRECT_URL', None)
        self.old_login_url = getattr(settings, 'LOGIN_URL', None)
        self.old_logout_url = getattr(settings, 'LOGOUT_URL', None)
        
#        settings.LOGIN_REDIRECT_URL = getattr(global_settings, 'LOGIN_REDIRECT_URL')
#        settings.LOGIN_URL = getattr(global_settings, 'LOGIN_URL')
#        settings.LOGOUT_URL = getattr(global_settings, 'LOGOUT_URL')
        
        # self.old_installed_apps = getattr(settings, 'INSTALLED_APPS', None)
#         
        # new_installed_apps= []
# 
        # if self.modeltranslation:
            # new_installed_apps.append('modeltranslation')
#             
        # else:
            # for app in self.old_installed_apps:
                # if not app == 'modeltranslation':
                    # new_installed_apps.append(app)
#                 
        # settings.INSTALLED_APPS = tuple(new_installed_apps)
        # print (settings.INSTALLED_APPS)
        # import ipdb; ipdb.set_trace()
#
    def teardown_test_environment(self, **kwargs):
        super(GeonitionTestSuiteRunner, self).teardown_test_environment(**kwargs)

        settings.LOGIN_REDIRECT_URL = self.old_login_redict_url
        settings.LOGIN_URL = self.old_login_url
        settings.LOGOUT_URL = self.old_logout_url
        # settings.INSTALLED_APPS = self.old_installed_apps
        
    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        # from django.db.models import get_app
        
        # suite = unittest.TestSuite()
        
        if 'auth' in test_labels or 'django.contrib.auth' in settings.INSTALLED_APPS:
            settings.LOGIN_REDIRECT_URL = getattr(global_settings, 'LOGIN_REDIRECT_URL')
            settings.LOGIN_URL = getattr(global_settings, 'LOGIN_URL')
            settings.LOGOUT_URL = getattr(global_settings, 'LOGOUT_URL')
            
        if test_labels:
            return super(GeonitionTestSuiteRunner, self).build_suite(
                     test_labels, extra_tests=extra_tests, **kwargs)

        new_test_labels = []
        for app in settings.INSTALLED_APPS:
            parts = app.split('.')
            app_name = parts[-1]
            if not app_name == 'modeltranslation':
                new_test_labels.append(app_name)

        return super(GeonitionTestSuiteRunner, self).build_suite(
                 tuple(new_test_labels), extra_tests=extra_tests, **kwargs)
            
        
        