import React from "react";
import { useState } from "react";
import {
  Link,
  BrowserRouter as Router,
  Route,
  Redirect,
  Switch,
  useHistory,
} from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

const AddTask = ({ showAddTask, onAdd, pantries, home, pantryOptions }) => {
  const [text, setText] = useState("");
  const [day, setDay] = useState("");
  const [reminder, setReminder] = useState(false);
  const [length, setLength] = useState();
  const [width, setWidth] = useState();
  const [height, setHeight] = useState();

  const onSubmit = (e) => {
    e.preventDefault();

    if (!text || length <= 0 || width <= 0 || height <= 0) {
      alert("Please add a pantry or enter valid dimensions");
      return;
    }

    onAdd({ text, length, width, height });

    setText("");
    setLength("");
    setHeight("");
    setWidth("");
  };

  const buttonStyles = {
    backgroundColor: "rgb(40, 41, 38)",
    background: "rgb(40, 41, 38)",
    color: "white",
    textAlign: "center",
    padding: "8px",
    fontSize: "small",
  };

  const calculate = () => {};

  return (
    <form className="add-form" onSubmit={onSubmit}>
      <div className="form-control">
        <label>Shelf</label>
        <input
          type="text"
          placeholder="Add shelf"
          value={text}
          onChange={(e) => setText(e.target.value)}
        ></input>
      </div>
      <div className="form-control">
        <label>Length</label>
        <input
          type="number"
          placeholder="Length"
          value={length}
          onChange={(e) => setLength(e.target.value)}
        ></input>
      </div>
      <div className="form-control">
        <label>Width</label>
        <input
          type="number"
          placeholder="Width"
          value={width}
          onChange={(e) => setWidth(e.target.value)}
        ></input>
      </div>
      <div className="form-control">
        <label>Height</label>
        <input
          type="number"
          placeholder="Height"
          value={height}
          onChange={(e) => setHeight(e.target.value)}
        ></input>
      </div>
      <input
        style={buttonStyles}
        type="submit"
        value="Add shelves"
        className="btn btn-block"
      ></input>

      <button
        style={buttonStyles}
        onClick={calculate}
        value="Calculate"
        className="btn btn-block"
      >
        Calculate
      </button>
    </form>
  );
};

export default AddTask;
