# coding: utf-8

"""
    Smooch

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import smooch
from smooch.rest import ApiException
from smooch.models.secret_key import SecretKey


class TestSecretKey(unittest.TestCase):
    """ SecretKey unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretKey(self):
        """
        Test SecretKey
        """
        model = smooch.models.secret_key.SecretKey()


if __name__ == '__main__':
    unittest.main()