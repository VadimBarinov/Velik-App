from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import random

class Recommendations:
    def __init__(self):
        self.recommend = None
        
    def calc_recommendations(self, df, bike_id):

        # приведение слов к стему (корневому слову)
        ps = PorterStemmer()

        def stem(text):
            y = []
            for i in text.split(','):
                y.append(ps.stem(i))
            return " ".join(y)

        df['bike_characteristics_string'] = df['bike_characteristics_string'].apply(stem)

        # создание вектора слов (токенов)
        cv = CountVectorizer()
        vectors = cv.fit_transform(df['bike_characteristics_string']).toarray()

        similarity = cosine_similarity(vectors)

        bike_index = df[df['id'] == bike_id].index[0]
        distances = similarity[bike_index]

        # получаем рекомендации, исключая переданный велик
        bike_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
        
        recommend_df = []
        df = df.loc[:, df.columns != 'bike_characteristics_string']
        
        for i in bike_list[:3]:
            if len(recommend_df) >= 2:
                break
            
            current_item = df.iloc[i[0]]
            if current_item['id'] != bike_id:
                recommend_df.append(current_item.to_dict())
            bike_list.remove(i)

        # добавляем 3-ий велик из первой половины списка рекомендаций
        recommend_df.append(df.iloc[random.choice(bike_list[:len(bike_list) // 2 + 1])[0]].to_dict())
        random.shuffle(recommend_df)
        
        self.recommend = recommend_df