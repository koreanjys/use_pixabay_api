from sqlmodel import SQLModel, create_engine, Session, select, or_
from models.api_models import ResponseData
import requests
import os
import time
import env
from tqdm import tqdm

# 데이터베이스 세팅
database_connection_string = env.DATABASE_URL
engine_url = create_engine(database_connection_string, echo=True)

# DB 이미지데이터를 가져오기
with Session(engine_url) as session:
    keyword = input("저장된 keyword 입력:  ")  # str
    istags = input("태그도 입력 하시겠습니까?(y or n):  ")
    if istags == "y":
        tags = input("태그 입력(여러개 입력시 ','로 구분):  ").strip().split(",")  # list
    statement = select(ResponseData).where(ResponseData.keyword==keyword)
    if istags == "y":
        conditions = [ResponseData.tags.like(f"%{tag}%") for tag in tags]
        statement = statement.where(or_(*conditions))
    image_data = session.exec(statement).all()

# 이미지 다운로드
dump_count = 0
dir_name = "./images/" + keyword
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

for inst in tqdm(image_data):
    if os.path.exists(dir_name+"/"+f"{inst.image_id}.jpg"):
        dump_count += 1
        continue
    request_image = requests.get(inst.imageURL)
    time.sleep(0.5)
    file_path = os.path.join(dir_name, f"{inst.image_id}.jpg")
    with open(file_path, "wb") as f:
        f.write(request_image.content)
print("다운로드 완료, 이미 있는 이미지 개수:  ", dump_count)