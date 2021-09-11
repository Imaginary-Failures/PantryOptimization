import React from "react";
import PropTypes from "prop-types";
// impt
import Button from "./Button";

//shortcut for const = rafce

const headerPantry = ({ title, onAdd, showAdd }) => {
  return (
    <header className="header">
      <h1>{title}</h1>
    </header>
  );
};

headerPantry.defaultProps = {
  title: "Specify your pantry",
};

headerPantry.propTypes = {
  title: PropTypes.string.isRequired,
};

//css in js
const headingStyles = {
  color: "red",
  backgroundColor: "black",
};

export default headerPantry;
