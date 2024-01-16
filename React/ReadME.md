# Remind about React

## 24.01.08

-   React.memo

React.memo는 고차 컴포넌트(Higher Order Component)입니다.  
컴포넌트가 동일한 props로 동일한 결과를 렌더링해낸다면, React.memo를 호출하고 결과를 메모이징(Memoizing)하도록 래핑하여 경우에 따라 성능 향상을 누릴 수 있습니다.  
 즉, React는 컴포넌트를 렌더링하지 않고 마지막으로 렌더링된 결과를 재사용합니다.

```
const MyComponent = React.memo(function MyComponent(props) {
/* props를 사용하여 렌더링 */
});
```

https://ko.reactjs.org/docs/react-api.html#reactmemo

---

-   PropTypes

PropTypes는 전달받은 데이터의 유효성을 검증하기 위해서 다양한 유효성 검사기를 내보냅니다.
prop에 유효하지 않은 값이 전달 되었을 때, 경고문이 JS 콘솔을 통해 보일 것입니다.
propTypes는 성능상의 이유로 개발 모드에서만 확인될 것입니다.

```
<script src="https://unpkg.com/prop-types@15.7.2/prop-types.js"></script>
// propTypes 사용하려면 prop-types 라이브러리를 사용해야함
MyComponent.propTypes = {
  // prop가 특정 JS 형식임을 선언할 수 있습니다.
  // 이것들은 기본적으로 모두 선택 사항입니다.
  optionalArray: PropTypes.array,
  optionalBool: PropTypes.bool,
  optionalFunc: PropTypes.func,
  optionalNumber: PropTypes.number,
  optionalObject: PropTypes.object,
  optionalString: PropTypes.string,
  optionalSymbol: PropTypes.symbol,

  // 렌더링 될 수 있는 것들은 다음과 같습니다.
  // 숫자(numbers), 문자(strings), 엘리먼트(elements), 또는 이러한 타입들(types)을 포함하고 있는 배열(array) (혹은 배열의 fragment)
```

https://ko.legacy.reactjs.org/docs/typechecking-with-proptypes.html#proptypes

## 24.01.09

-   react 앱 생성하기

```
원하는 디렉토리에 앱 생성 ( 앱 이름 이후 한 칸 띄우고 .찍기 )
npx create-react-app app_name .

생성된 앱 이름의 폴더로 이동
cd app_name

실행
npm start
```

-   생성 시 에러 뜰 때

```
npm install -g npm@latest
실행하고 진행해보기
```

-   react jsx 작성 시, html 태그 자동완성 안될 때  
    https://doishalf.tistory.com/59
-   useEffect 적용 시, console log가 2 번씩 실행 될 때  
    index.js의 <React.StrictMode></React.StrictMode> 태그로 감싸져 있어서 그렇다. 해당 태그는 React에서 기본 제공하는 검사 도구인데, 개발 모드일 때만 디버그를 하여 해당 태그로 감싸져 있는 부분은 자손까지 검사를 진행하게 된다.  
    https://velog.io/@hyes-y-tag/React-useEffect%EA%B0%80-%EB%91%90%EB%B2%88-%EC%8B%A4%ED%96%89%EB%90%9C%EB%8B%A4%EA%B3%A0
-   Memo 대신 useEffect를 사용하는 이유?  
    가장 큰 차이점은 useEffect는 해당 컴포넌트의 렌더링이 완료된 후에 실행되고, useMemo는 렌더링 중에 실행된다.  
    렌더링이 계속 된다면, 특히 특정 api를 불러오게 되는 경우 계속해서 불러오는 문제가 생길 수 있다.  
    state를 변경할 때, 계속해서 렌더링 되는 문제점이 존재한다. 많은 state가 존재한다면 성능 저하 문제가 발생할 수 있다. 이런 문제를 해결하기 위해 사용한다.
    https://velog.io/@jellyjw/React-useMemo%EC%99%80-useEffect-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0
-   그래서 useEffect가 정확하게 뭔데?  
     useEffect는 화면이 다 그려지고 나서 실행됩니다. 즉 화면을 먼저 그리고 그다음 실행
    따로 생명주기는 언급안하셔서 글 남깁니다. memo랑 헷갈리시는 분이 계시는데 이건 라이프 사이클이랑 연관이 있는 함수이고, 최초 실행만 할 것이냐, 아님 props, state에 따라(언급한 마법) 렌더링시 다시 그릴것이냐 판단하는 함수인듯 합니다.
    class 문법 라이프 사이클 펑션을 함축해놓은게 useEffect 입니다.

## 24.01.10

-   useEffect 사용 방법
    ```
    useEffect (() => {}, [keyword]);
    ```
    keyword가 변화 할 때마다 useEffect 안의 코드 실행한다.  
    대괄호 안이 비어 있을 경우, React가 지켜 볼 게 없으므로 처음 한 번만 실행한다.  
    https://nomadcoders.co/react-for-beginners/lectures/3284/comments/74216
-   Clean-up을 사용하는 이유  
    clean-up이 필요한 경우가 있는데, 대표적인 예가 외부 데이터에 구독 ( subscription )을 설정해야 하는 경우이다. 이런 경우 메모리 누수가 발생하지 않도록 정리 ( clean-up )하는 것이 중요하다.  
    effect에서 함수를 반환하는 이유는 추가적인 정리 ( clean up ) 메커니즘이다. 모든 effect는 정리를 위한 함수를 반환할 수 있다.
-   React가 effect를 Clean-up하는 시점은 언제?  
    React는 컴포넌트가 마운트 해제되는 때에 정리를 실행한다. effect는 한 번이 아니라 렌더링이 실행되는 때마다 실행된다. React가 다음 차례의 effect를 실행하기 전에 이전의 렌더링에서 파생된 effect 또한 정리하는 이유가 바로 이 때문이다.  
    https://ko.reactjs.org/docs/hooks-effect.html#effects-with-cleanup

## 24.01.16

-   Todo List 만들기

    input 밖에 form을 만들고 form에 submit이라는 이벤트를 이용할 거임  
    toDo가 비어있으면 함수가 작동하지않도록 return을 하고, 마지막에 setToDo("")을 통해
    Addtodo버튼을 누르면 toDo를 빈칸으로 만들도록한다.  
    그 다음은 여러 toDo를 저장할 array를 만들 것이다.  
    새로운 state를 만들고 toDos를 array로해서 직접적으로 State를 수정하는 방식이아닌
    함수를 통해 State를 수정하는 방식을 택한다.  
    즉 array에 직접적으로 수정하지 않고 element를 추가하는 방법이 필요하다.  
    1번 방법 line12에서 toDo의 값을 공백으로 직접 바꾼(함수를 통해) 방법
    2번 방법 setToDos안에 함수를 넣는 것 이 함수는 첫번째 argument로 현재의 state를 받아옴  
    -> 현재의 state가 들어간 새로운 array를 리턴해주는 역할을 한다.  
    즉 이 array에는 todo와 이전의 toDos를 가지게 됨  
    array안에 다른 array의 요소들을 넣고 싶음  
    number = [1,2,3]을 newNumber[4]에 넣고싶음 [4, ...number]을 사용  
    즉 setToDos를 통해 현재의 배열ToDos(지금까지 넣은 엘리먼트 포함된 array)를 가져와 toDo를 추가하는 역할을 한다.  
    마지막엔 toDos.length를 통해 array의 엘리먼트들의 개수를 h1태그를 통해 보여줌

-   map()과 key값  
    JavaScript map() 함수를 사용하여 numbers 배열을 반복 실행합니다. 각 항목에 대해 \<li> 엘리먼트를 반환하고 엘리먼트 배열의 결과를 listItems에 저장합니다.
    ```
    const numbers = [1, 2, 3, 4, 5];
    const listItems = numbers.map((number) =>
    <li>{number}</li>
    );
    ```
    그러면 \<ul> 엘리먼트 안에 전체 listItems 배열을 포함할 수 있습니다.
    ```
    <ul>{listItems}</ul>
    ```
    https://ko.legacy.reactjs.org/docs/lists-and-keys.html
