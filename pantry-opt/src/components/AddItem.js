import React from "react";
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const AddItem = ({ showAddItem, onAdd, items, home, pantryOptions }) => {
  const [text, setText] = useState("");
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
        <label>Item</label>
        <input
          type="text"
          placeholder="Add item"
          value={text}
          onChange={(e) => setText(e.target.value)}
        ></input>
      </div>
      <div className="form-control">
        <label>Length</label>
        <input
          min="0"
          step=".01"
          type="number"
          placeholder="Length"
          value={length}
          onChange={(e) => setLength(e.target.value)}
        ></input>
      </div>
      <div className="form-control">
        <label>Width</label>
        <input
          min="0"
          step=".01"
          type="number"
          placeholder="Width"
          value={width}
          onChange={(e) => setWidth(e.target.value)}
        ></input>
      </div>
      <div className="form-control">
        <label>Height</label>
        <input
          min="0"
          step=".01"
          type="number"
          placeholder="Height"
          value={height}
          onChange={(e) => setHeight(e.target.value)}
        ></input>
      </div>
      <input
        style={buttonStyles}
        type="submit"
        value="Add item"
        className="btn btn-block"
      ></input>
    </form>
  );
};

export default AddItem;
