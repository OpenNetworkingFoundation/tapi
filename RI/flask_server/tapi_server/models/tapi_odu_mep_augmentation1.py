# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_odu_odu_connection_end_point_spec import TapiOduOduConnectionEndPointSpec  # noqa: F401,E501
from tapi_server import util


class TapiOduMepAugmentation1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, odu_connection_end_point_spec=None):  # noqa: E501
        """TapiOduMepAugmentation1 - a model defined in OpenAPI

        :param odu_connection_end_point_spec: The odu_connection_end_point_spec of this TapiOduMepAugmentation1.  # noqa: E501
        :type odu_connection_end_point_spec: TapiOduOduConnectionEndPointSpec
        """
        self.openapi_types = {
            'odu_connection_end_point_spec': TapiOduOduConnectionEndPointSpec
        }

        self.attribute_map = {
            'odu_connection_end_point_spec': 'odu-connection-end-point-spec'
        }

        self._odu_connection_end_point_spec = odu_connection_end_point_spec

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOduMepAugmentation1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.odu.MepAugmentation1 of this TapiOduMepAugmentation1.  # noqa: E501
        :rtype: TapiOduMepAugmentation1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def odu_connection_end_point_spec(self):
        """Gets the odu_connection_end_point_spec of this TapiOduMepAugmentation1.


        :return: The odu_connection_end_point_spec of this TapiOduMepAugmentation1.
        :rtype: TapiOduOduConnectionEndPointSpec
        """
        return self._odu_connection_end_point_spec

    @odu_connection_end_point_spec.setter
    def odu_connection_end_point_spec(self, odu_connection_end_point_spec):
        """Sets the odu_connection_end_point_spec of this TapiOduMepAugmentation1.


        :param odu_connection_end_point_spec: The odu_connection_end_point_spec of this TapiOduMepAugmentation1.
        :type odu_connection_end_point_spec: TapiOduOduConnectionEndPointSpec
        """

        self._odu_connection_end_point_spec = odu_connection_end_point_spec
