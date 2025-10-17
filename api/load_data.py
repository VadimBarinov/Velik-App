from sqlalchemy import text
import pandas as pd


class LoadData:
    
    def __init__(self):
        self.df = None
    
    def load_bikes_data(self, db_session):
        get_bikes = text("""
                    SELECT 
                        bikemodel.*, 
                        GROUP_CONCAT(bikecharacteristic.value  SEPARATOR ', ') AS bike_characteristics_string
                    FROM 
                        catalog_bikemodel bikemodel, 
                        catalog_bikecharacteristicvalue bikecharacteristic, 
                        catalog_bikemodification bikemodification
                    WHERE 
                        bikemodel.id = bikemodification.bike_model_id AND
                        bikemodification.id = bikecharacteristic.bike_modification_id
                    GROUP BY bikemodel.id;
                """)

        self.df = pd.read_sql(get_bikes, con=db_session.bind)
    
    def data_preparation(self):
        self.df['bike_characteristics_string'] = self.df['bike_characteristics_string'].str.replace(' ', ',')
        self.df['bike_characteristics_string'] = self.df['bike_characteristics_string'].str.replace(',,', ',')
        self.df['bike_characteristics_string'] = self.df['bike_characteristics_string'].str.replace(':', '')
        self.df['bike_characteristics_string'] = self.df['bike_characteristics_string'].str.replace('_', '')
        self.df['bike_characteristics_string'] = self.df['bike_characteristics_string'].str.replace('(', '')
        self.df['bike_characteristics_string'] = self.df['bike_characteristics_string'].str.replace(')', '')
        self.df['bike_characteristics_string'] = self.df['bike_characteristics_string'].apply(lambda x: x.lower())