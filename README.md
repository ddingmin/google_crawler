# google_crawler
* 입력된 키워드를 구글 이미지 크롤링

## Run method
*     pip install -r requirements.txt
*     keywords.txt     
파일에 가져올 이미지 차례로 기입
*     python main.py
## 기능
* keywords.txt에 입력된 검색어들의 이미지를 크롤링
* 검색어별로 폴더를 만들어서 해당 폴더에 이미지가 저장된다.
### 에러
*     urllib.error.URLError:
    파이썬이 설치된 경로의 Install Certificates.command 파일을 실행하여 해결 출처 - https://blog.minamiland.com/551
