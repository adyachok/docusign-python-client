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


class BrandsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, brands=None, recipient_brand_id_default=None, sender_brand_id_default=None):
        """
        BrandsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'brands': 'list[Brand]',
            'recipient_brand_id_default': 'str',
            'sender_brand_id_default': 'str'
        }

        self.attribute_map = {
            'brands': 'brands',
            'recipient_brand_id_default': 'recipientBrandIdDefault',
            'sender_brand_id_default': 'senderBrandIdDefault'
        }

        self._brands = brands
        self._recipient_brand_id_default = recipient_brand_id_default
        self._sender_brand_id_default = sender_brand_id_default

    @property
    def brands(self):
        """
        Gets the brands of this BrandsResponse.
        The list of brands.

        :return: The brands of this BrandsResponse.
        :rtype: list[Brand]
        """
        return self._brands

    @brands.setter
    def brands(self, brands):
        """
        Sets the brands of this BrandsResponse.
        The list of brands.

        :param brands: The brands of this BrandsResponse.
        :type: list[Brand]
        """

        self._brands = brands

    @property
    def recipient_brand_id_default(self):
        """
        Gets the recipient_brand_id_default of this BrandsResponse.
        The brand seen by envelope recipients when a brand is not explicitly set.

        :return: The recipient_brand_id_default of this BrandsResponse.
        :rtype: str
        """
        return self._recipient_brand_id_default

    @recipient_brand_id_default.setter
    def recipient_brand_id_default(self, recipient_brand_id_default):
        """
        Sets the recipient_brand_id_default of this BrandsResponse.
        The brand seen by envelope recipients when a brand is not explicitly set.

        :param recipient_brand_id_default: The recipient_brand_id_default of this BrandsResponse.
        :type: str
        """

        self._recipient_brand_id_default = recipient_brand_id_default

    @property
    def sender_brand_id_default(self):
        """
        Gets the sender_brand_id_default of this BrandsResponse.
        The brand seen by envelope senders when a brand is not explicitly set.

        :return: The sender_brand_id_default of this BrandsResponse.
        :rtype: str
        """
        return self._sender_brand_id_default

    @sender_brand_id_default.setter
    def sender_brand_id_default(self, sender_brand_id_default):
        """
        Sets the sender_brand_id_default of this BrandsResponse.
        The brand seen by envelope senders when a brand is not explicitly set.

        :param sender_brand_id_default: The sender_brand_id_default of this BrandsResponse.
        :type: str
        """

        self._sender_brand_id_default = sender_brand_id_default

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
