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


class BillingPlanPreview(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, currency_code=None, invoice=None, is_prorated=None, subtotal_amount=None, tax_amount=None, total_amount=None):
        """
        BillingPlanPreview - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'currency_code': 'str',
            'invoice': 'BillingInvoice',
            'is_prorated': 'str',
            'subtotal_amount': 'str',
            'tax_amount': 'str',
            'total_amount': 'str'
        }

        self.attribute_map = {
            'currency_code': 'currencyCode',
            'invoice': 'invoice',
            'is_prorated': 'isProrated',
            'subtotal_amount': 'subtotalAmount',
            'tax_amount': 'taxAmount',
            'total_amount': 'totalAmount'
        }

        self._currency_code = currency_code
        self._invoice = invoice
        self._is_prorated = is_prorated
        self._subtotal_amount = subtotal_amount
        self._tax_amount = tax_amount
        self._total_amount = total_amount

    @property
    def currency_code(self):
        """
        Gets the currency_code of this BillingPlanPreview.
        Specifies the ISO currency code for the account.

        :return: The currency_code of this BillingPlanPreview.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this BillingPlanPreview.
        Specifies the ISO currency code for the account.

        :param currency_code: The currency_code of this BillingPlanPreview.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def invoice(self):
        """
        Gets the invoice of this BillingPlanPreview.

        :return: The invoice of this BillingPlanPreview.
        :rtype: BillingInvoice
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """
        Sets the invoice of this BillingPlanPreview.

        :param invoice: The invoice of this BillingPlanPreview.
        :type: BillingInvoice
        """

        self._invoice = invoice

    @property
    def is_prorated(self):
        """
        Gets the is_prorated of this BillingPlanPreview.
        

        :return: The is_prorated of this BillingPlanPreview.
        :rtype: str
        """
        return self._is_prorated

    @is_prorated.setter
    def is_prorated(self, is_prorated):
        """
        Sets the is_prorated of this BillingPlanPreview.
        

        :param is_prorated: The is_prorated of this BillingPlanPreview.
        :type: str
        """

        self._is_prorated = is_prorated

    @property
    def subtotal_amount(self):
        """
        Gets the subtotal_amount of this BillingPlanPreview.
        

        :return: The subtotal_amount of this BillingPlanPreview.
        :rtype: str
        """
        return self._subtotal_amount

    @subtotal_amount.setter
    def subtotal_amount(self, subtotal_amount):
        """
        Sets the subtotal_amount of this BillingPlanPreview.
        

        :param subtotal_amount: The subtotal_amount of this BillingPlanPreview.
        :type: str
        """

        self._subtotal_amount = subtotal_amount

    @property
    def tax_amount(self):
        """
        Gets the tax_amount of this BillingPlanPreview.
        

        :return: The tax_amount of this BillingPlanPreview.
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """
        Sets the tax_amount of this BillingPlanPreview.
        

        :param tax_amount: The tax_amount of this BillingPlanPreview.
        :type: str
        """

        self._tax_amount = tax_amount

    @property
    def total_amount(self):
        """
        Gets the total_amount of this BillingPlanPreview.
        

        :return: The total_amount of this BillingPlanPreview.
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """
        Sets the total_amount of this BillingPlanPreview.
        

        :param total_amount: The total_amount of this BillingPlanPreview.
        :type: str
        """

        self._total_amount = total_amount

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
