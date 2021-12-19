import requests


class Requester:

    def send_results(self, results) -> dict:
        """Send results to Elecard API"""
        response = requests.post(
            url="http://contest.elecard.ru/api",
            json={
                "key": "Rt0bdC5HmzvNOK1/V3SOHBhfbiFEBLgrYSGh6TLHhvwXjjBx6kPb3lsCICfCRXVTJsa9LRYpra0g+gSfEhg2Vg==",
                "method": "CheckResults",
                "params": results
            }
        )
        return response.json()

    def get_tasks(self) -> dict:
        """Get tasks from Elecard API"""
        response = requests.post(
            url="http://contest.elecard.ru/api",
            json={
                "key": "Rt0bdC5HmzvNOK1/V3SOHBhfbiFEBLgrYSGh6TLHhvwXjjBx6kPb3lsCICfCRXVTJsa9LRYpra0g+gSfEhg2Vg==",
                "method": "GetTasks",
                "params": None
            }
        )
        return response.json()['result']
