import React, { Component } from "react";
import Counter from "./counter";
class Counters extends Component {
  render() {
    const { onReset, counters, onDelete, onIncrement, onDecrement } =
      this.props;

    return (
      <div>
        <button onClick={onReset} className="btn btn-primary btn-sm m-2">
          Reset
        </button>
        {counters.map((counter) => (
          <Counter
            key={counter.id}
            onDelete={onDelete}
            onIncrement={onIncrement}
            onDecrement={onDecrement}
            // value={counter.value}
            // id={counter.id}
            //All can be encapsulated by storing the object itself
            counter={counter}
          >
            <h4>Counter #{counter.id}</h4>
          </Counter>
        ))}
      </div>
    );
  }
}

export default Counters;
