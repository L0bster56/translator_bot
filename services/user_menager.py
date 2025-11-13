import requests

from services.base_meneger import BaseMenager

class UserMenager(BaseMenager):
    def create(self, **kwargs):
        response = requests.post(
            url=self.url + "Telegram_user",
            headers=self.headers,
            json=kwargs
        )
        print(response)

    def get(self, obj_id):
        response = requests.get(
            url=self.url+f"Telegram_user?id=eq.{obj_id}",
            headers=self.headers,
        )
        user = response.json()
        print(user)
        if len(user) == 0:
            return None
        return user[0]

    def update(self, obj_id, **kwargs):
        requests.patch(
            url=self.url+f"Telegram_user?id=eq.{obj_id}",
            headers=self.headers,
            json=kwargs
        )


