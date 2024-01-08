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
