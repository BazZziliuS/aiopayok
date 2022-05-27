import ssl
import json

import certifi
from aiohttp import ClientSession, TCPConnector
from aiohttp.typedefs import StrOrURL


from typing import Optional


class BaseClient:
    '''Base aiohttp client'''

    def __init__(self) -> None:
        '''
        Set defaults on object init.

            By default `self._session` is None.
            It will be created on a first API request.
            The second request will use the same `self._session`.
        '''
        self._session: Optional[ClientSession] = None
    
    def get_session(self):
        '''Get cached session. One session per instance.'''
        if isinstance(self._session, ClientSession) and not self._session.closed:
            return self._session

        ssl_context = ssl.create_default_context(cafile=certifi.where())
        connector = TCPConnector(ssl=ssl_context)

        self._session = ClientSession(connector=connector)
        return self._session
    
    async def _make_request(self, method: str, url: StrOrURL, **kwargs) -> dict:
        '''
        Make a request.

            :param method: HTTP Method
            :param url: endpoint link
            :param kwargs: data, params, json and other...
            :return: status and result or exception
        '''
        session = self.get_session()

        async with session.request(method, url, **kwargs) as response:
            data = await response.text()
            return json.loads(data)
        

