# hw_2_2

1. 새로운 app instance를 생성하여 아이디가 app인 container에 mount 하시오.
   - CDN 가져와서 vue 환경 만들기
   - 사용할 함수 가져오기 (createdApp, ref)
   - app에 mount하기
2. 사용자가 입력한 색상 명이 colorType 변수에 할당 될 수 있도록 양방향 바인딩 directive를 사용하시오.
   - 양방향 바인딩? => 'v-model'을 통해 원하는 곳에 colorType 변수를 할당
   - 우리가 원하는 곳? 색을 입력 받을 input
3. 사용자가 입력한 글꼴 명이 fontType 변수에 할당 될 수 있도록 양방향 바인딩 directive를 사용하시오.
   - 'v-model'을 통해 원하는 곳에 fontType 변수를 할당
   - 우리가 원하는 곳? 폰트를 입력 받을 input
4. 첫 번째 p 태그의 style에 적용할 stlyeObject 변수를 만들고, 단방향 바인딩 directive를 사용하여 연결하시오.
   - 단방향 바인딩? => 'v-bind'를 사용해 원하는 곳에 styleObject 변수를 할당
   - 우리가 원하는 곳? 첫 번째 p 태그
   - style에 적용해야하므로 style 지정 후 사용
5. 값을 모두 입력 한 후, enter를 입력하거나, `변경!` 버튼을 클릭하면, changeStyle 함수가 실행되도록 이벤트 핸들러 directive를 사용하시오. 
   - button의 클릭 이벤트를 위해서 @click 이벤트를 다는데 기본 이벤트 동작 중단을 위해 prevent를 같이 써준다.
   - enter버튼을 누르면 changeStyle 함수가 실행되어야 하니까 @click이 되었을 때 changeStyle이 실행되도록 연결한다.
   - input으로 입력받은 colorType과 fontType을 color와 font-family 키에 할당한다. 이 때, colorType와 fontType는 ref를 통해 만들었으니 value에 값을 넣어주고, 새로 만든 객체에 이 둘을 넣어준다.
   - 생성된 객체를 p태그에 연결되어 있는, 원하는 곳인 styleObject에 할당한다. 이 때, styleObject도 ref로 만들었으니 value에 넣어준다.
   - 할당이 모두 완료되면 colorType과 fontType의 값을 빈 문자열로 초기화 하기 위해 changeStyle 함수 마지막에 둘의 value 값을 빈 문자열로 초기화한다.