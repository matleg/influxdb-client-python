# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Axis(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'bounds': 'list[str]',
        'label': 'str',
        'prefix': 'str',
        'suffix': 'str',
        'base': 'str',
        'scale': 'AxisScale'
    }

    attribute_map = {
        'bounds': 'bounds',
        'label': 'label',
        'prefix': 'prefix',
        'suffix': 'suffix',
        'base': 'base',
        'scale': 'scale'
    }

    def __init__(self, bounds=None, label=None, prefix=None, suffix=None, base=None, scale=None):  # noqa: E501
        """Axis - a model defined in OpenAPI"""  # noqa: E501

        self._bounds = None
        self._label = None
        self._prefix = None
        self._suffix = None
        self._base = None
        self._scale = None
        self.discriminator = None

        if bounds is not None:
            self.bounds = bounds
        if label is not None:
            self.label = label
        if prefix is not None:
            self.prefix = prefix
        if suffix is not None:
            self.suffix = suffix
        if base is not None:
            self.base = base
        if scale is not None:
            self.scale = scale

    @property
    def bounds(self):
        """Gets the bounds of this Axis.  # noqa: E501

        The extents of an axis in the form [lower, upper]. Clients determine whether bounds are to be inclusive or exclusive of their limits  # noqa: E501

        :return: The bounds of this Axis.  # noqa: E501
        :rtype: list[str]
        """
        return self._bounds

    @bounds.setter
    def bounds(self, bounds):
        """Sets the bounds of this Axis.

        The extents of an axis in the form [lower, upper]. Clients determine whether bounds are to be inclusive or exclusive of their limits  # noqa: E501

        :param bounds: The bounds of this Axis.  # noqa: E501
        :type: list[str]
        """

        self._bounds = bounds

    @property
    def label(self):
        """Gets the label of this Axis.  # noqa: E501

        label is a description of this Axis  # noqa: E501

        :return: The label of this Axis.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Axis.

        label is a description of this Axis  # noqa: E501

        :param label: The label of this Axis.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def prefix(self):
        """Gets the prefix of this Axis.  # noqa: E501

        Prefix represents a label prefix for formatting axis values.  # noqa: E501

        :return: The prefix of this Axis.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this Axis.

        Prefix represents a label prefix for formatting axis values.  # noqa: E501

        :param prefix: The prefix of this Axis.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def suffix(self):
        """Gets the suffix of this Axis.  # noqa: E501

        Suffix represents a label suffix for formatting axis values.  # noqa: E501

        :return: The suffix of this Axis.  # noqa: E501
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this Axis.

        Suffix represents a label suffix for formatting axis values.  # noqa: E501

        :param suffix: The suffix of this Axis.  # noqa: E501
        :type: str
        """

        self._suffix = suffix

    @property
    def base(self):
        """Gets the base of this Axis.  # noqa: E501

        Base represents the radix for formatting axis values.  # noqa: E501

        :return: The base of this Axis.  # noqa: E501
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this Axis.

        Base represents the radix for formatting axis values.  # noqa: E501

        :param base: The base of this Axis.  # noqa: E501
        :type: str
        """

        self._base = base

    @property
    def scale(self):
        """Gets the scale of this Axis.  # noqa: E501


        :return: The scale of this Axis.  # noqa: E501
        :rtype: AxisScale
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this Axis.


        :param scale: The scale of this Axis.  # noqa: E501
        :type: AxisScale
        """

        self._scale = scale

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Axis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other