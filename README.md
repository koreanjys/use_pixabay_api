# use_pixabay_api

Pixabay API의 이미지 데이터를 가져오고, 이미지를 다운로드 하는 어플리케이션

## 1. 환경설정

### 1.1 설치 파일
- python 버전 3.8.9
- mysql은 버전 8.0.36

### 1.2 설치 라이브러리
requirements.txt 파일로 설치 가능
```
annotated-types==0.6.0
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
colorama==0.4.6
cryptography==42.0.2
greenlet==3.0.3
idna==3.6
pycparser==2.21
pydantic==2.6.1
pydantic-core==2.16.2
PyMySQL==1.1.0
python-dotenv==1.0.1
requests==2.31.0
SQLAlchemy==2.0.27
sqlmodel==0.0.16
tqdm==4.66.2
typing-extensions==4.9.0
urllib3==2.2.1
```

### 1.3 .env파일 및 API_KEY
- pixabay api key 필요 [pixabay_api_docs](https://pixabay.com/api/docs/)
- 환경변수는 프로젝트 디렉터리에 **.env** 파일 생성
- .env파일 예시
```
API_KEY="***-***"
DATABASE_URL="mysql+pymysql://{user}:{password}@127.0.0.1:3306/{db_name}"
END_POINT="https://pixabay.com/api/"
```

## 2. 실행파일 설명

### 2.1 get_image_data.py
- 실행 후 "keyword"를 입력 -> 해당 keyword와 관련된 이미지 데이터를 MySQL DB에 저장

```
# keyword 입력 예시(나무, 나무+땅, 나무+물+돌)

$ python get_image_data.py
검색할 keyword 입력: 나무+땅
```

- 플로우 차트

![alt text](get_image_data-1.png)

### 2.2 download_images.py
- DB에 저장된 imageURL을 읽어서 해당 url 이미지를 다운받음. keyword 입력 필요(DB에 저장된 데이터 중에 해당 keyword를 가진 rows의 imageURL을 불러옴, 태그 입력은 선택)

```
$ python download_images.py
저장된 keyword 입력: 나무+땅
태그도 입력 하시겠습니까?(y or n):
```

- 플로우 차트

![alt text](download_images.png)

## 3. responsedata 테이블 설명

![alt text](responsedata.png)

## 4. request GET 쿼리
<br>
endpoint = "https://pixabay.com/api/"

<h3>Parameters</h3>
<table class="api_properties params">
<tbody>
<tr>
<th>key <span style="color:#d33228">(required)</span></th>
<td>str</td>
<td id="api_key">
Your API key: <b class="inline" style="background:#02be6e;color:#fff;padding:1px 8px">***-***</b>
</td>
</tr>
<tr>
<th>q</th>
<td>str</td>
<td>
A URL encoded search term. If omitted, <i>all images</i> are returned. This value may not exceed 100 characters.
<br>Example: "yellow+flower"
</td>
</tr>
<tr>
<th>lang</th>
<td>str</td>
<td>
<a target="_blank" href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">Language code</a> of the language to be searched in.
<br>Accepted values: cs, da, de, en, es, fr, id, it, hu, nl, no, pl, pt, ro, sk, fi, sv, tr, vi, th, bg, ru, el, ja, ko, zh
<br>Default: "en"
</td>
</tr>
<tr>
<th>id</th>
<td>str</td>
<td>Retrieve individual images by ID.</td>
</tr>
<tr>
<th>image_type</th>
<td>str</td>
<td>
Filter results by image type.
<br>Accepted values: "all", "photo", "illustration", "vector"
<br>Default: "all"
</td>
</tr>
<tr>
<th>orientation</th>
<td>str</td>
<td>
Whether an image is wider than it is tall, or taller than it is wide.
<br>Accepted values: "all", "horizontal", "vertical"
<br>Default: "all"
</td>
</tr>
<tr>
<th>category</th>
<td>str</td>
<td>
Filter results by category.
<br>Accepted values: backgrounds, fashion, nature, science, education, feelings, health, people, religion, places, animals, industry, computer, food, sports, transportation, travel, buildings, business, music
</td>
</tr>
<tr>
<th>min_width</th>
<td>int</td>
<td>
Minimum image width.
<br>Default: "0"
</td>
</tr>
<tr>
<th>min_height</th>
<td>int</td>
<td>
Minimum image height.
<br>Default: "0"
</td>
</tr>
<tr>
<th>colors</th>
<td>str</td>
<td>
Filter images by color properties. A comma separated list of values may be used to select multiple properties.
<br>Accepted values: "grayscale", "transparent", "red", "orange", "yellow", "green", "turquoise", "blue", "lilac", "pink", "white", "gray", "black", "brown"
</td>
</tr>
<tr>
<th>editors_choice</th>
<td>bool</td>
<td>
Select images that have received an <a href="/editors_choice/">Editor's Choice</a> award.
<br>Accepted values: "true", "false"
<br>Default: "false"
</td>
</tr>
<tr>
<th>safesearch</th>
<td>bool</td>
<td>
A flag indicating that only images suitable for all ages should be returned.
<br>Accepted values: "true", "false"
<br>Default: "false"
</td>
</tr>
<tr>
<th>order</th>
<td>str</td>
<td>
How the results should be ordered.
<br>Accepted values: "popular", "latest"
<br>Default: "popular"
</td>
</tr>
<tr>
<th>page</th>
<td>int</td>
<td>
Returned search results are paginated. Use this parameter to select the page number.
<br>Default: 1
</td>
</tr>
<tr>
<th>per_page</th>
<td>int</td>
<td>
Determine the number of results per page.
<br>Accepted values: 3 - 200
<br>Default: 20
</td>
</tr>
<tr>
<th>callback</th>
<td>string</td>
<td>
JSONP callback function name
</td>
</tr>
<tr>
<th>pretty</th>
<td>bool</td>
<td>
Indent JSON output. This option should not be used in production.
<br>Accepted values: "true", "false"
<br>Default: "false"
</td>
</tr>
</tbody></table>

<br>

## 5. response 예제
<br>
<p>
Retrieving photos of "yellow flowers". The search term <b class="inline">q</b> needs to be URL encoded:
</p>
<div class="example_url"><a href="/api/?key=***-***&amp;q=yellow+flowers&amp;image_type=photo&amp;pretty=true" target="_blank">https://pixabay.com/api/?key=***-***&amp;q=yellow+flowers&amp;image_type=photo</a></div>
<br>
<p>Response for this request:</p>
<pre class="prettyprint rainbow" data-language="javascript"><table class="rainbow" data-language="javascript"><tbody><tr class="line line-1"><td class="line-number" data-line-number="1"></td><td class="line-code">{</td></tr><tr class="line line-2"><td class="line-number" data-line-number="2"></td><td class="line-code"><span class="string">"total"</span>: <span class="constant numeric">4692</span>,</td></tr><tr class="line line-3"><td class="line-number" data-line-number="3"></td><td class="line-code"><span class="string">"totalHits"</span>: <span class="constant numeric">500</span>,</td></tr><tr class="line line-4"><td class="line-number" data-line-number="4"></td><td class="line-code"><span class="string">"hits"</span>: [</td></tr><tr class="line line-5"><td class="line-number" data-line-number="5"></td><td class="line-code">    {</td></tr><tr class="line line-6"><td class="line-number" data-line-number="6"></td><td class="line-code">        <span class="string">"id"</span>: <span class="constant numeric">195893</span>,</td></tr><tr class="line line-7"><td class="line-number" data-line-number="7"></td><td class="line-code">        <span class="string">"pageURL"</span>: <span class="string">"https://pixabay.com/en/blossom-bloom-flower-195893/"</span>,</td></tr><tr class="line line-8"><td class="line-number" data-line-number="8"></td><td class="line-code">        <span class="string">"type"</span>: <span class="string">"photo"</span>,</td></tr><tr class="line line-9"><td class="line-number" data-line-number="9"></td><td class="line-code">        <span class="string">"tags"</span>: <span class="string">"blossom, bloom, flower"</span>,</td></tr><tr class="line line-10"><td class="line-number" data-line-number="10"></td><td class="line-code">        <span class="string">"previewURL"</span>: <span class="string">"https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg"</span></td></tr><tr class="line line-11"><td class="line-number" data-line-number="11"></td><td class="line-code">        <span class="string">"previewWidth"</span>: <span class="constant numeric">150</span>,</td></tr><tr class="line line-12"><td class="line-number" data-line-number="12"></td><td class="line-code">        <span class="string">"previewHeight"</span>: <span class="constant numeric">84</span>,</td></tr><tr class="line line-13"><td class="line-number" data-line-number="13"></td><td class="line-code">        <span class="string">"webformatURL"</span>: <span class="string">"https://pixabay.com/get/35bbf209e13e39d2_640.jpg"</span>,</td></tr><tr class="line line-14"><td class="line-number" data-line-number="14"></td><td class="line-code">        <span class="string">"webformatWidth"</span>: <span class="constant numeric">640</span>,</td></tr><tr class="line line-15"><td class="line-number" data-line-number="15"></td><td class="line-code">        <span class="string">"webformatHeight"</span>: <span class="constant numeric">360</span>,</td></tr><tr class="line line-16"><td class="line-number" data-line-number="16"></td><td class="line-code">        <span class="string">"largeImageURL"</span>: <span class="string">"https://pixabay.com/get/ed6a99fd0a76647_1280.jpg"</span>,</td></tr><tr class="line line-17"><td class="line-number" data-line-number="17"></td><td class="line-code">        <span class="string">"fullHDURL"</span>: <span class="string">"https://pixabay.com/get/ed6a9369fd0a76647_1920.jpg"</span>,</td></tr><tr class="line line-18"><td class="line-number" data-line-number="18"></td><td class="line-code">        <span class="string">"imageURL"</span>: <span class="string">"https://pixabay.com/get/ed6a9364a9fd0a76647.jpg"</span>,</td></tr><tr class="line line-19"><td class="line-number" data-line-number="19"></td><td class="line-code">        <span class="string">"imageWidth"</span>: <span class="constant numeric">4000</span>,</td></tr><tr class="line line-20"><td class="line-number" data-line-number="20"></td><td class="line-code">        <span class="string">"imageHeight"</span>: <span class="constant numeric">2250</span>,</td></tr><tr class="line line-21"><td class="line-number" data-line-number="21"></td><td class="line-code">        <span class="string">"imageSize"</span>: <span class="constant numeric">4731420</span>,</td></tr><tr class="line line-22"><td class="line-number" data-line-number="22"></td><td class="line-code">        <span class="string">"views"</span>: <span class="constant numeric">7671</span>,</td></tr><tr class="line line-23"><td class="line-number" data-line-number="23"></td><td class="line-code">        <span class="string">"downloads"</span>: <span class="constant numeric">6439</span>,</td></tr><tr class="line line-24"><td class="line-number" data-line-number="24"></td><td class="line-code">        <span class="string">"likes"</span>: <span class="constant numeric">5</span>,</td></tr><tr class="line line-25"><td class="line-number" data-line-number="25"></td><td class="line-code">        <span class="string">"comments"</span>: <span class="constant numeric">2</span>,</td></tr><tr class="line line-26"><td class="line-number" data-line-number="26"></td><td class="line-code">        <span class="string">"user_id"</span>: <span class="constant numeric">48777</span>,</td></tr><tr class="line line-27"><td class="line-number" data-line-number="27"></td><td class="line-code">        <span class="string">"user"</span>: <span class="string">"Josch13"</span>,</td></tr><tr class="line line-28"><td class="line-number" data-line-number="28"></td><td class="line-code">        <span class="string">"userImageURL"</span>: <span class="string">"https://cdn.pixabay.com/user/2013/11/05/02-10-23-764_250x250.jpg"</span>,</td></tr><tr class="line line-29"><td class="line-number" data-line-number="29"></td><td class="line-code">    },</td></tr><tr class="line line-30"><td class="line-number" data-line-number="30"></td><td class="line-code">    {</td></tr><tr class="line line-31"><td class="line-number" data-line-number="31"></td><td class="line-code">        <span class="string">"id"</span>: <span class="constant numeric">73424</span>,</td></tr><tr class="line line-32"><td class="line-number" data-line-number="32"></td><td class="line-code">        ...</td></tr><tr class="line line-33"><td class="line-number" data-line-number="33"></td><td class="line-code">    },</td></tr><tr class="line line-34"><td class="line-number" data-line-number="34"></td><td class="line-code">    ...</td></tr><tr class="line line-35"><td class="line-number" data-line-number="35"></td><td class="line-code">]</td></tr><tr class="line line-36"><td class="line-number" data-line-number="36"></td><td class="line-code">}</td></tr></tbody></table></pre>

<table class="api_properties">
<tbody><tr><th>Response key</th><th>Description</th></tr>
<tr><td>total</td><td>The total number of hits.</td></tr>
<tr><td>totalHits</td><td>The number of images accessible through the API. By default, the API is limited to return a maximum of 500 images per query.</td></tr>
<tr><td>id</td><td>A unique identifier for this image.</td></tr>
<tr><td>pageURL</td><td>Source page on Pixabay, which provides a download link for the original image of the dimension imageWidth x imageHeight and the file size imageSize.</td></tr>
<tr><td>previewURL</td><td>Low resolution images with a maximum width or height of 150 px (previewWidth x previewHeight).</td></tr>
<tr>
<td>webformatURL</td>
<td>
<p>Medium sized image with a maximum width or height of 640 px (webformatWidth x webformatHeight). URL valid for 24 hours.</p>
<b>Replace '_640' in any webformatURL value to access other image sizes:</b>
<br>Replace with '_180' or '_340' to get a 180 or 340 px tall version of the image, respectively.
Replace with '_960' to get the image in a maximum dimension of 960 x 720 px.
</td>
</tr>
<tr><td>largeImageURL</td><td>Scaled image with a maximum width/height of 1280px.</td></tr>
<tr><td>views</td><td>Total number of views.</td></tr>
<tr><td>downloads</td><td>Total number of downloads.</td></tr>
<tr><td>likes</td><td>Total number of likes.</td></tr>
<tr><td>comments</td><td>Total number of comments.</td></tr>
<tr><td>user_id, user</td><td>User ID and name of the contributor. Profile URL: https://pixabay.com/users/{ USERNAME }-{ ID }/</td></tr>
<tr><td>userImageURL</td><td>Profile picture URL (250 x 250 px).</td></tr>
</tbody></table>

<p><span class="remove_if_full_access_granted" style="font-weight:bold">The following response key/value pairs are only available if your account has been <a href="#" class="modal" data-href="/api/request_full_access/" data-w="560">approved for full API access</a>.</span> These URLs give you access to the original images in full resolution and - if available - in vector format:</p>

<table class="api_properties">
<tbody><tr><th>Response key</th><th>Description</th></tr>
<tr><td>fullHDURL</td><td>Full HD scaled image with a maximum width/height of 1920px.</td></tr>
<tr><td>imageURL</td><td>URL to the original image (imageWidth x imageHeight).</td></tr>
<tr><td>vectorURL</td><td>URL to a vector resource if available, else omitted.</td></tr>
</tbody></table>