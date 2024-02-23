# From Pixabay API get image data to Mysql

import env
import requests
import json
from models.api_models import ResponseData
from sqlmodel import SQLModel, Session, create_engine

# 파라미터 입력
q = input("검색어 입력:  ")
per_page = 200

params = {
    "q": q,
    "per_page": per_page,
    "key": env.API_KEY,
    "lang": "ko"
}

# pixabay api에 get 요청
req = requests.get(url=env.END_POINT, params=params)
image_data = json.loads(req.text)["hits"]

# 데이터베이스 세팅
database_connection_string = env.DATABASE_URL
engine_url = create_engine(database_connection_string, echo=True)
SQLModel.metadata.create_all(engine_url)

# DB에 이미지 데이터 200개만 저장

with Session(engine_url) as session:
    for dat in image_data:
        
        inst = ResponseData(
            image_id=dat["id"],
            imageURL=dat["webformatURL"],
            tags=dat["tags"],
            user=dat["user"],
            type=dat["type"],
            keyword=q
        )
        session.add(inst)
        try:
            session.commit()
        except:
            print("이미 있는 이미지")
            session.rollback()