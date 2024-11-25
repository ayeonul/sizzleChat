# ┌─────────────────────────────────────────────────────────┐
# │                   Buddha bless no bug                   │
# │                                                         │
# │                        _oo0oo_                          │
# │                       o8888888o                         │
# │                       88" . "88                         │
# │                      (|  -_-  |)                        │
# │                       0\  =  /0                         │
# │                     ___/`---'\___                       │
# │                   .' \\|     |// `.                     │
# │                  /  \\|||  :  |||// \                   │
# │                 /  _||||| -:- |||||- \                  │
# │                 |   | \\\  -  /// |   |                 │
# │                 | \_|  ''\---/''  |_/ |                 │
# │                 \  .-\__   `-`   ___/-./                │
# │               ___`. .'   /--.--\   `. .___              │
# │            ."" '<   `.___\_<|>_/___.' >' "".            │
# │           | | :   `- \`.;`\ _ /`;.`/  :    | |          │
# │           \  \ `_.    \_ __\ /__ _/ .-`   /  /          │
# │            `-.____`.___  \_____/___.-`____.-'           │
# │                                                         │
# │                 佛祖保佑         永无BUG                 │
# └─────────────────────────────────────────────────────────┘

import streamlit as st
from GPT import ChatGPT

# 외부에 공개되어서는 안 되는 API key를 들고옴.
# 배포판에서는 웹에서 설정해놓은 문자열을, 개발섭에서는 따로 저장해놓은 파일(secrets.toml)에서 값을 들고온다
OPENAI_KEY = st.secrets["OPENAI_KEY"] 

# 챗봇에 설정 부여. 영어로 하는 이유는 이래야 더 잘 알아들음
concept = "You are 'Sizzle(시즐)', a chatbot that provides guidance on cooking and ingredients."

# 챗봇 initialize
assistant = ChatGPT(
    api_key=OPENAI_KEY,
    model_name="gpt-4o-mini",
    concept=concept,
)

# streamlit이 화면을 그렸는데 messages라는 변수가 없다면(:= 화면을 처음 그릴 때 실행함.)
# st.session_state가 vuex랑 같은 개념이더라 vuex states에 messages라는 값을 초기화하는 거랑 같음
# 첫 인사말은 고정. 이렇게 하면 빠르게 챗봇의 응답 말투랑 사용 언어를 거의 통제할 수 있음
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "오늘의 날씨나 기분은 어떠신가요? 씨즐이 상황에 맞게 추천해 드릴게요!",
        }
    ]

# 채팅 입력창 그리는 코드
user_input = st.chat_input("무엇이든 물어보세요!")
# 유저 입력창에 무언가 내용이 있고, 유저가 전송 버튼을 눌렀을 때
if user_input:
    # session_state(vuex state 같은 놈)의 messages에 유저가 이런 말을 했다! 라고 추가한다
    st.session_state.messages.append({"role": "user", "content": user_input})
    # 유저가 방금 한 말까지 더해서 GPT API에 전송하고 값을 받아옴
    result = assistant.chat(st.session_state.messages)
    res = res = result["res"][0]["res"]
    # GPT API 응답값을 챗봇이 이렇게 말했다! 라고 session_state messages에 추가함
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": res,
        }
    )


# session_state의 messages에 있는 내용을 전부 화면이 뿌려주는 코드.
# 왜 채팅 입력창 코드가 채팅 내역 코드보다 위에 있냐면...
# streamlit은 데이터에 변화가 생기면 이 페이지의 전체 코드를 재실행함으로써 반응성을 보임
# 그니까 messages에 변동을 주는 코드 다음에-messages를 표시하는 코드가 와야 정상작동함
# 하지만 일반적인 채팅은 유저 인풋이 맨 아래에 오니까! streamlit 라이브러리 자체에서 유저 인풋 div를 맨 아래로 보내버리는 것
# 이상 tmi였읍니다 재미있지요?
for msg in st.session_state.messages:
    message_view = st.chat_message(msg["role"])
    message_view.write(msg["content"])
