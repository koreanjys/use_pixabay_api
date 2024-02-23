# From Pixabay API get image data to Mysql

import env
import requests
import json
import time
from models.api_models import ResponseData
from sqlmodel import SQLModel, Session, create_engine
from tqdm import tqdm

# 파라미터 입력
q = input("검색어 입력:  ")
per_page = 200  # 3~200
page = 1  # default=1
params = {
    "q": q,
    "page": page,
    "per_page": per_page,
    "key": env.API_KEY,
    "lang": "ko"
}
image_data = []  # ResponseData 모델의 인스턴스들을 받아올 리스트

# pixabay api에 get 요청(per_page * 5 개의 데이터)
for page in tqdm(range(1, 6)):
    params["page"] = page
    req = requests.get(url=env.END_POINT, params=params)
    time.sleep(1)
    try:
        image_data = image_data + json.loads(req.text)["hits"]
    except:
        pass

# 데이터베이스 세팅
database_connection_string = env.DATABASE_URL
engine_url = create_engine(database_connection_string)
SQLModel.metadata.create_all(engine_url)

# DB에 저장
with Session(engine_url) as session:
    dump_count = 0
    try:
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
                dump_count += 1
                session.rollback()
    except:
        print("가져올 데이터가 없습니다.")
print("이미 있는 이미지:  ", dump_count)