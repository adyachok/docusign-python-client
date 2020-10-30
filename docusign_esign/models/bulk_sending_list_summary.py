# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BulkSendingListSummary(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bulk_send_list_id': 'str',
        'created_by_user': 'str',
        'created_date': 'str',
        'name': 'str'
    }

    attribute_map = {
        'bulk_send_list_id': 'bulkSendListId',
        'created_by_user': 'createdByUser',
        'created_date': 'createdDate',
        'name': 'name'
    }

    def __init__(self, bulk_send_list_id=None, created_by_user=None, created_date=None, name=None):  # noqa: E501
        """BulkSendingListSummary - a model defined in Swagger"""  # noqa: E501

        self._bulk_send_list_id = None
        self._created_by_user = None
        self._created_date = None
        self._name = None
        self.discriminator = None

        if bulk_send_list_id is not None:
            self.bulk_send_list_id = bulk_send_list_id
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if created_date is not None:
            self.created_date = created_date
        if name is not None:
            self.name = name

    @property
    def bulk_send_list_id(self):
        """Gets the bulk_send_list_id of this BulkSendingListSummary.  # noqa: E501

          # noqa: E501

        :return: The bulk_send_list_id of this BulkSendingListSummary.  # noqa: E501
        :rtype: str
        """
        return self._bulk_send_list_id

    @bulk_send_list_id.setter
    def bulk_send_list_id(self, bulk_send_list_id):
        """Sets the bulk_send_list_id of this BulkSendingListSummary.

          # noqa: E501

        :param bulk_send_list_id: The bulk_send_list_id of this BulkSendingListSummary.  # noqa: E501
        :type: str
        """

        self._bulk_send_list_id = bulk_send_list_id

    @property
    def created_by_user(self):
        """Gets the created_by_user of this BulkSendingListSummary.  # noqa: E501

          # noqa: E501

        :return: The created_by_user of this BulkSendingListSummary.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this BulkSendingListSummary.

          # noqa: E501

        :param created_by_user: The created_by_user of this BulkSendingListSummary.  # noqa: E501
        :type: str
        """

        self._created_by_user = created_by_user

    @property
    def created_date(self):
        """Gets the created_date of this BulkSendingListSummary.  # noqa: E501

          # noqa: E501

        :return: The created_date of this BulkSendingListSummary.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this BulkSendingListSummary.

          # noqa: E501

        :param created_date: The created_date of this BulkSendingListSummary.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def name(self):
        """Gets the name of this BulkSendingListSummary.  # noqa: E501

          # noqa: E501

        :return: The name of this BulkSendingListSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BulkSendingListSummary.

          # noqa: E501

        :param name: The name of this BulkSendingListSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(BulkSendingListSummary, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BulkSendingListSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other