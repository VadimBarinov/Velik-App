from pydantic import BaseModel

class RecommendationResponse(BaseModel):
    id: int
    name: str
    slug: str
    img_url: str
    mark_id: int
    star: float
    star_count: int