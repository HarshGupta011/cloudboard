import time
import pyperclip
import uuid
import requests


class CopyHandler:
    """
    Handles copy operation
    """

    def __init__(self, host, port, token):
        """
        1. Maintain a unique ID for each copy operation
        """
        self.copy_uid = None
        self.data = None
        self.timestamp = float('-inf')
        self.token = token
        self.endpoint = f"http://{host}:{port}"

    def update_local_state(self):
        self.uid = uuid.uuid4().hex  # COPY id
        self.data = pyperclip.paste()
        self.timestamp = time.time()

    def update_remote_state(self):
        list_clipboards_url = f"{self.endpoint}/list_clipboards"
        copy_data_url = f"{self.endpoint}/copy_data"
        query_data = {
            "device_id": self.token
        }
        copy_data = {
            "device_id": self.token,
            "copy_data": self.data,
            "timestamp": self.timestamp,
            "is_file": False
        }
        response = requests.get(list_clipboards_url, json=query_data)
        json_response = response.json()
        if response.status_code == 200:
            if len(json_response["clipboards"]) > 0:
                cld_timestamp = response.json()["clipboards"][0]["copied_at"]
                if cld_timestamp < self.timestamp:
                    response = requests.post(copy_data_url, json=copy_data)
                else:
                    pass
            else:
                response = requests.post(copy_data_url, json=copy_data)