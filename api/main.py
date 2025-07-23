from fastapi import FastAPI, Depends
from database import get_db
from load_data import LoadData
from recommendations import Recommendations
from sqlalchemy.orm import Session
from typing import List
from schemas import RecommendationResponse

app = FastAPI(
    title="Система рекомендаций",
    description="REST API для получения рекомендаций",
)

@app.get("/recommendations/", response_model=List[RecommendationResponse])
async def get_recommend(bike_id: int, db: Session = Depends(get_db)):
    """
        # Получение рекомендаций на основе переданного велосипеда

        ## Args:

            bike_id: id велосипеда

            db: Сессия базы данных

        ## Returns:

            Список объектов таблицы BikeModel
    """
    load_data = LoadData()
    load_data.load_bikes_data(db)
    load_data.data_preparation()

    recommendations = Recommendations()
    recommendations.calc_recommendations(load_data.df, bike_id)

    return recommendations.recommend