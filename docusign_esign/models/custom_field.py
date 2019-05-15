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


class CustomField(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, custom_field_type=None, error_details=None, field_id=None, list_items=None, name=None, required=None, show=None, value=None):
        """
        CustomField - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'custom_field_type': 'str',
            'error_details': 'ErrorDetails',
            'field_id': 'str',
            'list_items': 'list[str]',
            'name': 'str',
            'required': 'str',
            'show': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'custom_field_type': 'customFieldType',
            'error_details': 'errorDetails',
            'field_id': 'fieldId',
            'list_items': 'listItems',
            'name': 'name',
            'required': 'required',
            'show': 'show',
            'value': 'value'
        }

        self._custom_field_type = custom_field_type
        self._error_details = error_details
        self._field_id = field_id
        self._list_items = list_items
        self._name = name
        self._required = required
        self._show = show
        self._value = value

    @property
    def custom_field_type(self):
        """
        Gets the custom_field_type of this CustomField.
        

        :return: The custom_field_type of this CustomField.
        :rtype: str
        """
        return self._custom_field_type

    @custom_field_type.setter
    def custom_field_type(self, custom_field_type):
        """
        Sets the custom_field_type of this CustomField.
        

        :param custom_field_type: The custom_field_type of this CustomField.
        :type: str
        """

        self._custom_field_type = custom_field_type

    @property
    def error_details(self):
        """
        Gets the error_details of this CustomField.

        :return: The error_details of this CustomField.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this CustomField.

        :param error_details: The error_details of this CustomField.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def field_id(self):
        """
        Gets the field_id of this CustomField.
        

        :return: The field_id of this CustomField.
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """
        Sets the field_id of this CustomField.
        

        :param field_id: The field_id of this CustomField.
        :type: str
        """

        self._field_id = field_id

    @property
    def list_items(self):
        """
        Gets the list_items of this CustomField.
        

        :return: The list_items of this CustomField.
        :rtype: list[str]
        """
        return self._list_items

    @list_items.setter
    def list_items(self, list_items):
        """
        Sets the list_items of this CustomField.
        

        :param list_items: The list_items of this CustomField.
        :type: list[str]
        """

        self._list_items = list_items

    @property
    def name(self):
        """
        Gets the name of this CustomField.
        

        :return: The name of this CustomField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CustomField.
        

        :param name: The name of this CustomField.
        :type: str
        """

        self._name = name

    @property
    def required(self):
        """
        Gets the required of this CustomField.
        When set to **true**, the signer is required to fill out this tab

        :return: The required of this CustomField.
        :rtype: str
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this CustomField.
        When set to **true**, the signer is required to fill out this tab

        :param required: The required of this CustomField.
        :type: str
        """

        self._required = required

    @property
    def show(self):
        """
        Gets the show of this CustomField.
        

        :return: The show of this CustomField.
        :rtype: str
        """
        return self._show

    @show.setter
    def show(self, show):
        """
        Sets the show of this CustomField.
        

        :param show: The show of this CustomField.
        :type: str
        """

        self._show = show

    @property
    def value(self):
        """
        Gets the value of this CustomField.
        Specifies the value of the tab. 

        :return: The value of this CustomField.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CustomField.
        Specifies the value of the tab. 

        :param value: The value of this CustomField.
        :type: str
        """

        self._value = value

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
