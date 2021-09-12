import React from "react";
import { FaTimes } from "react-icons/fa";

const Item = ({ item, onDelete, onToggle }) => {
  return (
    <div
      className="task"
      // className={`item ${item.reminder ? "reminder" : ""}`}
      // onDoubleClick={() => onToggle(task.id)}
    >
      <h3>
        {item.text}{" "}
        <FaTimes
          onClick={() => onDelete(item.id)}
          style={{ color: "red", cursor: "pointer" }}
        />
      </h3>
      <p>
        {item.length} in. &times; {item.width} in. &times; {item.height} in.
      </p>
    </div>
  );
};

export default Item;
