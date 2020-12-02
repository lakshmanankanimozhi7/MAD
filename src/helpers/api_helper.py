import requests

class APIHelper(object):
    def api_response(
        self, method, url, payload={}, query={}, headers={}, auth_token=None, files=None
    ):

        if headers is None:
            headers = {"Content-Type": "application/json"}


        response = requests.request(
            method=method,
            url=url,
            data=payload,
            params=query,
            headers=headers,
            files=files,
            auth=auth_token
        )

        return response




