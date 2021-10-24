## 🔗 접속 URL 소개

- /enrollment - 수강신청 페이지. uuid 쿠키를 이곳에서 발급하도록 했습니다.
- /roadmap - 현재 유저의 진도에 맞춰 진도표가 변하고, 아직 미치지 못한 진도에는 접근할 수 없도록 했습니다.
- /lecture - 데이터를 vimeo 로 주셔서 쉽게 작업했습니다. 아직 버튼의 기능 구현은 미미합니다.

## 🎃 RESTFULL API

- 비슷한 기능을 하는 api 를 router 로 묶어 다루기 편하도록 했습니다.
- /api/enrollment GET POST
    - 선택한 강의에 맞는 가격 정보가 수강신청란에 표시 GET
    - 수강신청 데이터 서버로 전송. POST
- /api/courses GET POST
    - 유저에 따라 강의 목록과 진도 상황을 로드해주는 조회 api GET
    - 유저가 특정한 강의를 수강하려 할 때 현재 진도에 맞는지 체크합니다. POST
- /api/lecture GET POST
    - 강의실 페이지에 접속했을 때 강의의 링크 정보를 전송받고, 현재 수강 기록을 네비게이션 바에서 확인 가능하게 합니다 GET
    - 다음 강의로 넘어가려 하거나, 이미 수강한 강의를 넘어가려 할 때 받습니다. 아직 수강하지 않은 강의는 바로 볼 수 없게 합니다. POST

## ⏲️ 개발기간

- 2021-10-22 16:23 - 2021-10-24 23:59

## 🧙 개발자

- 유동민 (2021-03-01~)

## 📌 기술 선택 이유

- flask: 장고에 비해 지원하는 기능이 적지만 많은 익스텐션이 있어 다용도로 활용
- uuid: 로그인 기능 없이 세 페이지를 구현하면서, enrollment 페이지에서

### 보안이슈

- 미흡하지만 최대한 데이터가 url을 통해 전송되거나 개발자 도구에서 쉽게 확인할 수 있는 형태로 주고받아지지 않도록 신경을 썼습니다. 이 과정에서 로그인 관련 구현을 위해 모델을 만들고 flask-login
  모듈도 이용하려 했으나 아직 경험이 부족하여 도입하지 못했습니다.

### 뷰 구성

- 과제에 있어서 어느 정도로 기존의 리소스를 활용해도 될지를 여쭤보지 못해, 기존 강의실과 진도기록표의 일부 스타일시트 구성을 차용했습니다.

### 문제를 느꼈던 부분

- flask-login 라이브러리를 사용해 유저의 정보를 간단하게 주고받고자 했으나 경험과 자료의 부족으로 완성하지 못해 제외했습니다.
- 지시 사항에 말씀해주신 REST-full 한 api를 구성하기 위해 작업 시작 후 API 메소드부터 정리하고 시작했지만, 중복된 기능을 다른 api 에서 구현하게 되는 부분들이 발생해 이를 수정하는 과정에서 한
  페이지에서 사용하는 api 를 다른 페이지에서도 가져다 쓰는 부분들이 있었습니다. 좀 더 고민해보겠습니다.
- 적재적소에서 에러를 발생시키고 미리 정의한 에러 화면으로 사용자를 이동시켜야 하고자 했는데 테스트를 많이 해보지 못해 모든 에러 페이지를 확인하지 못한 부분이 아쉽습니다.

## 📌 주요 느낀 점

- 여태 어떤 스택을 공부하고 싶다거나 어떤 기술을 사용하는 곳에서 일하고 싶다 같은 말을 쉽게 해 왔는데, 아직도 기본기와 실력이 많이 부족하다는 것을 이번에 또 느꼈고, 또 그만큼 채워나가는 과정들을 눈앞에 두고
  있다 생각하니 아무래도 흥미가 쉬이 사그라들지 않습니다.
- 부트캠프에 휴일에 해당하는 시간에 참여했지만 무엇보다 몰입할 수 있는 과제를 주셔서 감사했습니다.

