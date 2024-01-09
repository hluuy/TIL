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
    https://velog.io/@jellyjw/React-useMemo%EC%99%80-useEffect-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0
