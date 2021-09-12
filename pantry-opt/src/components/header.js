import React from "react";
import PropTypes from "prop-types";
// impt
import Button from "./Button";

//shortcut for const = rafce

const header = ({ title, onAdd, showAdd }) => {
  return (
    <header className="header">
      <h1>{title}</h1>
      <Button
        color={showAdd ? "red" : "green"}
        text={showAdd ? "Close" : "Add"}
        onClick={onAdd}
      />
    </header>
  );
};

header.defaultProps = {
  title: "Shelves",
};

header.propTypes = {
  title: PropTypes.string.isRequired,
};

export default header;
