import React from "react";
import { FaTimes } from "react-icons/fa";

const Pantry = ({ pantry, onDelete, onToggle }) => {
  return (
    <div
      className={`pantry ${pantry.reminder ? "reminder" : ""}`}
      // onDoubleClick={() => onToggle(task.id)}
    >
      <h3>
        <FaTimes
          onClick={() => onDelete(pantry.id)}
          style={{ color: "red", cursor: "pointer" }}
        />
      </h3>
      <p>
        Dimensions: {pantry.length}, {pantry.width}, {pantry.height}
      </p>
    </div>
  );
};

export default Pantry;
