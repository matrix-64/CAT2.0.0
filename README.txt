CAT2.0.0
실행을 위해 추가적으로 설치되어야 하는 모듈들 :
- Numpy
- OpenCV
- MediaPipe
- pynput

[사용법]
※아래에서 나오는 '모양'은 shape_names파일에 따라 표현한다.
※기본적으로 손 모양은 (왼손 모양,오른손 모양)으로 표기한다.
CAT에는 기본적으로 아래의 세 가지 모드가 있다.
1) 대기 모드
    아무 동작도 수행하지 않는다. 대신, 모드를 전환하는 동작만은 가능하다. 아래의 두 모드에서 다른 모드로 전환하기 위해서는 반드시 이 모드를 거쳐야 한다.
    마우스 모드로 전환하기 위해서는 손 모양을 (29,29)로, 키보드 모드로 전환하기 위해서는 (25,25)로 만들어야 한다.
2) 마우스 모드
    기존의 CAT이 가지고 있던 기능을 그대로 가져왔다. 대신 왼손의 모양을 29,25,24 또는 17,1로 할 때 감도를 순서대로 조절하도록 했다. 나머지 모양의 감도는 0이다.
    대기 모드로 전환하기 위해서는 손 모양을 (31,31)로 만들어야 한다.
4) 키보드 모드(미완성)
     키보드 모드로 전환하면 CAT의 실행 창에 키보드 화면이 뜬다. 각 손의 모양을 29로 했을 때 검지의 끝과 좌표가 겹치는 키를 입력한다. 손의 모양을 28과 29로만 사용하는 것이 편할 것이다.






++++++이유는 모르겠으나 내 컴퓨터는 더블클릭으로 실행했을 때 실행이 되지 않는다. 대신 IDLE등에서 f5로 실행하면 잘 돌아간다.
