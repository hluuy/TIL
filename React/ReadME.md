# Remind about React

- React.memo

React.memo는 고차 컴포넌트(Higher Order Component)입니다.  
컴포넌트가 동일한 props로 동일한 결과를 렌더링해낸다면, React.memo를 호출하고 결과를 메모이징(Memoizing)하도록 래핑하여 경우에 따라 성능 향상을 누릴 수 있습니다.  
 즉, React는 컴포넌트를 렌더링하지 않고 마지막으로 렌더링된 결과를 재사용합니다.

```
const MyComponent = React.memo(function MyComponent(props) {
/* props를 사용하여 렌더링 */
});
```

https://ko.reactjs.org/docs/react-api.html#reactmemo
