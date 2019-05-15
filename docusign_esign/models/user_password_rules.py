# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserPasswordRules(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, password_rules=None, user_id=None):
        """
        UserPasswordRules - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'password_rules': 'AccountPasswordRules',
            'user_id': 'str'
        }

        self.attribute_map = {
            'password_rules': 'passwordRules',
            'user_id': 'userId'
        }

        self._password_rules = password_rules
        self._user_id = user_id

    @property
    def password_rules(self):
        """
        Gets the password_rules of this UserPasswordRules.

        :return: The password_rules of this UserPasswordRules.
        :rtype: AccountPasswordRules
        """
        return self._password_rules

    @password_rules.setter
    def password_rules(self, password_rules):
        """
        Sets the password_rules of this UserPasswordRules.

        :param password_rules: The password_rules of this UserPasswordRules.
        :type: AccountPasswordRules
        """

        self._password_rules = password_rules

    @property
    def user_id(self):
        """
        Gets the user_id of this UserPasswordRules.
        

        :return: The user_id of this UserPasswordRules.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserPasswordRules.
        

        :param user_id: The user_id of this UserPasswordRules.
        :type: str
        """

        self._user_id = user_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
