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


class Radio(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, anchor_case_sensitive=None, anchor_horizontal_alignment=None, anchor_ignore_if_not_present=None, anchor_match_whole_word=None, anchor_string=None, anchor_units=None, anchor_x_offset=None, anchor_y_offset=None, error_details=None, locked=None, page_number=None, required=None, selected=None, tab_id=None, tab_order=None, value=None, x_position=None, y_position=None):
        """
        Radio - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'anchor_case_sensitive': 'str',
            'anchor_horizontal_alignment': 'str',
            'anchor_ignore_if_not_present': 'str',
            'anchor_match_whole_word': 'str',
            'anchor_string': 'str',
            'anchor_units': 'str',
            'anchor_x_offset': 'str',
            'anchor_y_offset': 'str',
            'error_details': 'ErrorDetails',
            'locked': 'str',
            'page_number': 'str',
            'required': 'str',
            'selected': 'str',
            'tab_id': 'str',
            'tab_order': 'str',
            'value': 'str',
            'x_position': 'str',
            'y_position': 'str'
        }

        self.attribute_map = {
            'anchor_case_sensitive': 'anchorCaseSensitive',
            'anchor_horizontal_alignment': 'anchorHorizontalAlignment',
            'anchor_ignore_if_not_present': 'anchorIgnoreIfNotPresent',
            'anchor_match_whole_word': 'anchorMatchWholeWord',
            'anchor_string': 'anchorString',
            'anchor_units': 'anchorUnits',
            'anchor_x_offset': 'anchorXOffset',
            'anchor_y_offset': 'anchorYOffset',
            'error_details': 'errorDetails',
            'locked': 'locked',
            'page_number': 'pageNumber',
            'required': 'required',
            'selected': 'selected',
            'tab_id': 'tabId',
            'tab_order': 'tabOrder',
            'value': 'value',
            'x_position': 'xPosition',
            'y_position': 'yPosition'
        }

        self._anchor_case_sensitive = anchor_case_sensitive
        self._anchor_horizontal_alignment = anchor_horizontal_alignment
        self._anchor_ignore_if_not_present = anchor_ignore_if_not_present
        self._anchor_match_whole_word = anchor_match_whole_word
        self._anchor_string = anchor_string
        self._anchor_units = anchor_units
        self._anchor_x_offset = anchor_x_offset
        self._anchor_y_offset = anchor_y_offset
        self._error_details = error_details
        self._locked = locked
        self._page_number = page_number
        self._required = required
        self._selected = selected
        self._tab_id = tab_id
        self._tab_order = tab_order
        self._value = value
        self._x_position = x_position
        self._y_position = y_position

    @property
    def anchor_case_sensitive(self):
        """
        Gets the anchor_case_sensitive of this Radio.
        When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**.

        :return: The anchor_case_sensitive of this Radio.
        :rtype: str
        """
        return self._anchor_case_sensitive

    @anchor_case_sensitive.setter
    def anchor_case_sensitive(self, anchor_case_sensitive):
        """
        Sets the anchor_case_sensitive of this Radio.
        When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**.

        :param anchor_case_sensitive: The anchor_case_sensitive of this Radio.
        :type: str
        """

        self._anchor_case_sensitive = anchor_case_sensitive

    @property
    def anchor_horizontal_alignment(self):
        """
        Gets the anchor_horizontal_alignment of this Radio.
        Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**.

        :return: The anchor_horizontal_alignment of this Radio.
        :rtype: str
        """
        return self._anchor_horizontal_alignment

    @anchor_horizontal_alignment.setter
    def anchor_horizontal_alignment(self, anchor_horizontal_alignment):
        """
        Sets the anchor_horizontal_alignment of this Radio.
        Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**.

        :param anchor_horizontal_alignment: The anchor_horizontal_alignment of this Radio.
        :type: str
        """

        self._anchor_horizontal_alignment = anchor_horizontal_alignment

    @property
    def anchor_ignore_if_not_present(self):
        """
        Gets the anchor_ignore_if_not_present of this Radio.
        When set to **true**, this tab is ignored if anchorString is not found in the document.

        :return: The anchor_ignore_if_not_present of this Radio.
        :rtype: str
        """
        return self._anchor_ignore_if_not_present

    @anchor_ignore_if_not_present.setter
    def anchor_ignore_if_not_present(self, anchor_ignore_if_not_present):
        """
        Sets the anchor_ignore_if_not_present of this Radio.
        When set to **true**, this tab is ignored if anchorString is not found in the document.

        :param anchor_ignore_if_not_present: The anchor_ignore_if_not_present of this Radio.
        :type: str
        """

        self._anchor_ignore_if_not_present = anchor_ignore_if_not_present

    @property
    def anchor_match_whole_word(self):
        """
        Gets the anchor_match_whole_word of this Radio.
        When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**.

        :return: The anchor_match_whole_word of this Radio.
        :rtype: str
        """
        return self._anchor_match_whole_word

    @anchor_match_whole_word.setter
    def anchor_match_whole_word(self, anchor_match_whole_word):
        """
        Sets the anchor_match_whole_word of this Radio.
        When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**.

        :param anchor_match_whole_word: The anchor_match_whole_word of this Radio.
        :type: str
        """

        self._anchor_match_whole_word = anchor_match_whole_word

    @property
    def anchor_string(self):
        """
        Gets the anchor_string of this Radio.
        Anchor text information for a radio button.

        :return: The anchor_string of this Radio.
        :rtype: str
        """
        return self._anchor_string

    @anchor_string.setter
    def anchor_string(self, anchor_string):
        """
        Sets the anchor_string of this Radio.
        Anchor text information for a radio button.

        :param anchor_string: The anchor_string of this Radio.
        :type: str
        """

        self._anchor_string = anchor_string

    @property
    def anchor_units(self):
        """
        Gets the anchor_units of this Radio.
        Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches.

        :return: The anchor_units of this Radio.
        :rtype: str
        """
        return self._anchor_units

    @anchor_units.setter
    def anchor_units(self, anchor_units):
        """
        Sets the anchor_units of this Radio.
        Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches.

        :param anchor_units: The anchor_units of this Radio.
        :type: str
        """

        self._anchor_units = anchor_units

    @property
    def anchor_x_offset(self):
        """
        Gets the anchor_x_offset of this Radio.
        Specifies the X axis location of the tab, in anchorUnits, relative to the anchorString.

        :return: The anchor_x_offset of this Radio.
        :rtype: str
        """
        return self._anchor_x_offset

    @anchor_x_offset.setter
    def anchor_x_offset(self, anchor_x_offset):
        """
        Sets the anchor_x_offset of this Radio.
        Specifies the X axis location of the tab, in anchorUnits, relative to the anchorString.

        :param anchor_x_offset: The anchor_x_offset of this Radio.
        :type: str
        """

        self._anchor_x_offset = anchor_x_offset

    @property
    def anchor_y_offset(self):
        """
        Gets the anchor_y_offset of this Radio.
        Specifies the Y axis location of the tab, in anchorUnits, relative to the anchorString.

        :return: The anchor_y_offset of this Radio.
        :rtype: str
        """
        return self._anchor_y_offset

    @anchor_y_offset.setter
    def anchor_y_offset(self, anchor_y_offset):
        """
        Sets the anchor_y_offset of this Radio.
        Specifies the Y axis location of the tab, in anchorUnits, relative to the anchorString.

        :param anchor_y_offset: The anchor_y_offset of this Radio.
        :type: str
        """

        self._anchor_y_offset = anchor_y_offset

    @property
    def error_details(self):
        """
        Gets the error_details of this Radio.

        :return: The error_details of this Radio.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this Radio.

        :param error_details: The error_details of this Radio.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def locked(self):
        """
        Gets the locked of this Radio.
        When set to **true**, the signer cannot change the data of the custom tab.

        :return: The locked of this Radio.
        :rtype: str
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """
        Sets the locked of this Radio.
        When set to **true**, the signer cannot change the data of the custom tab.

        :param locked: The locked of this Radio.
        :type: str
        """

        self._locked = locked

    @property
    def page_number(self):
        """
        Gets the page_number of this Radio.
        Specifies the page number on which the tab is located.

        :return: The page_number of this Radio.
        :rtype: str
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """
        Sets the page_number of this Radio.
        Specifies the page number on which the tab is located.

        :param page_number: The page_number of this Radio.
        :type: str
        """

        self._page_number = page_number

    @property
    def required(self):
        """
        Gets the required of this Radio.
        When set to **true**, the signer is required to fill out this tab

        :return: The required of this Radio.
        :rtype: str
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this Radio.
        When set to **true**, the signer is required to fill out this tab

        :param required: The required of this Radio.
        :type: str
        """

        self._required = required

    @property
    def selected(self):
        """
        Gets the selected of this Radio.
        When set to **true**, the radio button is selected.

        :return: The selected of this Radio.
        :rtype: str
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """
        Sets the selected of this Radio.
        When set to **true**, the radio button is selected.

        :param selected: The selected of this Radio.
        :type: str
        """

        self._selected = selected

    @property
    def tab_id(self):
        """
        Gets the tab_id of this Radio.
        The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].     

        :return: The tab_id of this Radio.
        :rtype: str
        """
        return self._tab_id

    @tab_id.setter
    def tab_id(self, tab_id):
        """
        Sets the tab_id of this Radio.
        The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].     

        :param tab_id: The tab_id of this Radio.
        :type: str
        """

        self._tab_id = tab_id

    @property
    def tab_order(self):
        """
        Gets the tab_order of this Radio.
        

        :return: The tab_order of this Radio.
        :rtype: str
        """
        return self._tab_order

    @tab_order.setter
    def tab_order(self, tab_order):
        """
        Sets the tab_order of this Radio.
        

        :param tab_order: The tab_order of this Radio.
        :type: str
        """

        self._tab_order = tab_order

    @property
    def value(self):
        """
        Gets the value of this Radio.
        Specifies the value of the tab. 

        :return: The value of this Radio.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Radio.
        Specifies the value of the tab. 

        :param value: The value of this Radio.
        :type: str
        """

        self._value = value

    @property
    def x_position(self):
        """
        Gets the x_position of this Radio.
        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.

        :return: The x_position of this Radio.
        :rtype: str
        """
        return self._x_position

    @x_position.setter
    def x_position(self, x_position):
        """
        Sets the x_position of this Radio.
        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.

        :param x_position: The x_position of this Radio.
        :type: str
        """

        self._x_position = x_position

    @property
    def y_position(self):
        """
        Gets the y_position of this Radio.
        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.

        :return: The y_position of this Radio.
        :rtype: str
        """
        return self._y_position

    @y_position.setter
    def y_position(self, y_position):
        """
        Sets the y_position of this Radio.
        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.

        :param y_position: The y_position of this Radio.
        :type: str
        """

        self._y_position = y_position

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
