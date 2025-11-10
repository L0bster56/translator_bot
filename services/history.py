import requests

from services.base_meneger import BaseMenager

class HistoryMenager(BaseMenager):
    def create(self, **kwargs):
        requests.post(
            url=self.url+"History",
            headers=self.headers,
            json=kwargs
        )

    def list(self, **kwargs):
        response = requests.get(
            url=self.url + f"History?user_id=eq.{kwargs['user_id']}",
            headers=self.headers,
        )
        return response.json()






