import React from "react";
import PropTypes from "prop-types";
// impt
import Button from "./Button";

//shortcut for const = rafce

const headerItem = ({ title, onAdd, showAdd }) => {
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

headerItem.defaultProps = {
  title: "Items",
};

headerItem.propTypes = {
  title: PropTypes.string.isRequired,
};

export default headerItem;
