# Sizzle-Chat

### 파일 구성

```
auto-reserve-with-chat/ (다른 플젝 하던 거 그대로 클론하고 폴더명 안 바꿈요 미안 . . .)
    	/.devcontainer/ :streamlit 배포하면서 생긴듯? 무슨 폴더인지 모르겠네
    	/.streamlit/ :streamlit 배포 관련 폴더
    		/config.toml :배포 설정 파일
		# /secrets.toml :개발용 파일. git에는 올리지 않음. API key 같은 보안이 필요한 내용이 있으며, 배포 후 streamlit cloud 설정에서 따로 값을 입력하여 동작함.
	/.gitignore :git에 안 올릴 파일(업데이트 무시할 파일) 모음
	/GPT.py :GPT API를 불러서 쓰기 위한 모듈. ** 이 파일의 내용은 되도록 공개하지 말것**
	/main.py :streamlit이 돌아가는 메인 파일. Streamlit 화면을 그리고, 이벤트가 발생하면 GPT API를 부른다.
	/README.md :지금 읽고있는 이거
	/requirements.txt :이 프로젝트를 실행하기 위한 최소 실행 환경. streamlit cloud에 배포 후 구동할 때 필요로 한다.
```


### 사용 라이브러리

python==3.9.20 (사유: 내가 맨날 쓰던 버전임)

* [Streamlit](https://docs.streamlit.io/)
  * 챗봇 프론트엔드
* [OpenAI](https://platform.openai.com/docs/concepts)
  * 챗봇 엔진에 활용, 모델은 GPT-4o mini
* [tenacity](https://tenacity.readthedocs.io/en/latest/)
  * 코드를 실행하다 실패하더라도 바로 재실행하는 걸 쉽게 만들어주는 라이브러리.
    여기서는 GPT API를 호출할 때 예상치 못한 오류를 무시하기 위해 삽입.
    GPT.py의 45~50번째 줄 참조-넣어놓은 옵션은 대충
    * 실패하면 1에서 30초 중 랜덤한 시간을 기다렸다가 재실행할 것
    * 최대 5번까지만 재시도할 것
    * 어떤 유형의 에러(뭐... 통신 에러든 응답을 처리하다 생긴 에러든...)가 발생해도 재실행할 것
    * 마지막 재실행 후에도 에러가 뜬다면, 그 에러를 그대로 raise할 것
  * 45번째줄이 @retry(...)라고 되어있는... 다소 생소한 문법일 텐데 데코레이터라고 하는... 함수 등을 꾸며주는 역할을 하는 녀석임. 이 retry라는 함수로 아래에 있는 chat이라는 함수를 감싼다(tenacity에서 임포트한 retry라는 함수에 chat을 집어넣었다)는 느낌으로 이해하면 될 듯...? 궁금한데 이해 안 가면 연락 ㄱ

### 배포 방식

[streamlit cloud](https://streamlit.io/cloud) 사용. Streamlit 공식에서 제공하는 배포 플랫폼으로, 무료로 사용 가능하며 배포 및 유지보수가 ㅈㄴ 간편하다는 장점이 있음. git repository와 연결해두면 내가 git에 push할 때마다 알아서 코드 업데이트 및 재배포를 시도함. 


### main.py 설명

n~m번째 줄 / 줄 설명 이렇게 보면 됨

* 1~23
  * 부처님의 힘을 빌어 버그가 없길 바라는 주석 (코드에 영향 없음)
* 와 이 뒤로 여기다 쓰기 힘들겟다 그냥 파일에 주석 다 달아놓을게

### 왜 GPT.py 공개하면 안 됨?

이 파일... 나의 마더소스. 나의 seed 코드. 어디서 공개된 게 아니고 내가 스스로 내 입맛대로 짠 거라; 회사에서도 나만... 쓰던 거거든

***극히 일부 공개하는 정도는 괜찮은데 한 클래스/함수를 통째로 공개하는 건 지양***
