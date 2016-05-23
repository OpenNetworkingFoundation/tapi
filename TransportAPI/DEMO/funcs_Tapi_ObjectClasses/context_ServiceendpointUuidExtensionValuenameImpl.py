import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_ServiceendpointUuidExtensionValuenameImpl:

    @classmethod
    def get(cls, uuid, valueName):
        print 'handling get'
        if uuid in Context._serviceEndPoint:
            if valueName in Context._serviceEndPoint[uuid].extension:
                return Context._serviceEndPoint[uuid].extension[valueName]
            else:
                raise KeyError('valueName')
        else:
            raise KeyError('uuid')
