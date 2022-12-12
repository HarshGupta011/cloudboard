import requests

class PasteHandler:
    """
    Handles paste operation.
    """
    def __init__(self, host, port, token):
        self.token = token
        self.endpoint = f"http://{host}:{port}"

    def cloud_paste(self, local_copy_timestamp):
        list_clipboards_url = f"{self.endpoint}/list_clipboards"
        paste_data_url = f"{self.endpoint}/paste_data"
        query_data = {
            "device_id": self.token
        }
        response = requests.get(list_clipboards_url, json=query_data)
        json_response = response.json()
        paste_response = None
        if response.status_code == 200:
            if len(json_response["clipboards"]) > 0:
                cld_timestamp = response.json()["clipboards"][0]["copied_at"]
                if cld_timestamp >= local_copy_timestamp:
                    paste_response = requests.get(paste_data_url, json=query_data)
                else:
                    pass
            else:
                paste_response = requests.get(paste_data_url, json=query_data)
            json_paste_response = paste_response.json()
        if paste_response and "copied_text" in json_paste_response:
            return(json_paste_response["copied_text"])