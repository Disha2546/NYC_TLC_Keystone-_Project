from pydantic import BaseModel


class HotspotRequest(BaseModel):
    top_n: int = 20