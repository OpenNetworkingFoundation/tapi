# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_connectivity_getconnectivityservicedetails_output import TapiConnectivityGetconnectivityservicedetailsOutput  # noqa: F401,E501
from tapi_server import util


class TapiConnectivityGetConnectivityServiceDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, output=None):  # noqa: E501
        """TapiConnectivityGetConnectivityServiceDetails - a model defined in OpenAPI

        :param output: The output of this TapiConnectivityGetConnectivityServiceDetails.  # noqa: E501
        :type output: TapiConnectivityGetconnectivityservicedetailsOutput
        """
        self.openapi_types = {
            'output': TapiConnectivityGetconnectivityservicedetailsOutput
        }

        self.attribute_map = {
            'output': 'output'
        }

        self._output = output

    @classmethod
    def from_dict(cls, dikt) -> 'TapiConnectivityGetConnectivityServiceDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.connectivity.GetConnectivityServiceDetails of this TapiConnectivityGetConnectivityServiceDetails.  # noqa: E501
        :rtype: TapiConnectivityGetConnectivityServiceDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output(self):
        """Gets the output of this TapiConnectivityGetConnectivityServiceDetails.


        :return: The output of this TapiConnectivityGetConnectivityServiceDetails.
        :rtype: TapiConnectivityGetconnectivityservicedetailsOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TapiConnectivityGetConnectivityServiceDetails.


        :param output: The output of this TapiConnectivityGetConnectivityServiceDetails.
        :type output: TapiConnectivityGetconnectivityservicedetailsOutput
        """

        self._output = output
