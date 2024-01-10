import { useState, useEffect } from "react";

function Hello() {
    // function byeFn() {
    //     console.log("bye :(");
    // }
    // function hiFn() {
    //     console.log("hello :)");
    //     return byeFn;
    // }
    // useEffect(hiFn, []);
    useEffect(() => {
        console.log("hi :)");
        return function () {
            console.log("bye :(");
        };
    }, []);
    return <h1>Hello</h1>;
}

function App() {
    const [showing, setShowing] = useState(false);
    const onClick = () => setShowing((prev) => !prev);
    return (
        <div>
            <button onClick={onClick}>{showing ? "Hide" : "Show"}</button>
            {showing ? <Hello /> : null}
        </div>
    );
}

export default App;
