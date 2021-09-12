import React from "react";
import { useState } from "react";

const AddPantry = ({ onAdd, pantries }) => {
  const [length, setLength] = useState();
  const [width, setWidth] = useState();
  const [height, setHeight] = useState();

  const onSubmit = (e) => {
    e.preventDefault();

    if (
      //Check for invalid inputs
      isNaN(length) ||
      isNaN(width) ||
      isNaN(height) ||
      length <= 0 ||
      width <= 0 ||
      height <= 0
    ) {
      alert("Please add a pantry or enter valid dimensions");
      return;
    }

    onAdd({ length, width, height });

    setLength();
    setHeight();
    setWidth();
  };

  const showSubmit = () => {
    return (
      <input
        type="submit"
        value="Submit pantry"
        className="btn btn-block"
      ></input>
    );
  };

  const buttonStyles = {
    backgroundColor: "rgb(40, 41, 38)",
    background: "rgb(40, 41, 38)",
    color: "white",
    textAlign: "center",
    padding: "8px",
    fontSize: "small",
  };

  return (
    <form className="add-form" onSubmit={onSubmit}>
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
      {pantries.length <= 0 ? (
        <input
          style={buttonStyles}
          type="submit"
          value="Submit pantry"
          className="btn btn-block"
        ></input>
      ) : (
        ""
      )}
    </form>
  );
};

export default AddPantry;
