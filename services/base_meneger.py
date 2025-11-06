from configs import API_URL, API_KEY


class BaseMenager:
    url: str = API_URL
    headers: dict = {
        "apikey": API_KEY,
    }

    def create(self, **kwargs):
        pass

    def get(self, obj_id):
        pass

    def update(self, obj_id, **kwargs):
        pass

    def list(self,**kwargs):
        pass