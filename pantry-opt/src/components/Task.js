import React from "react";
import { FaTimes } from "react-icons/fa";

const Task = ({ task, onDelete, onToggle }) => {
  return (
    <div
      className={`task ${task.reminder ? "reminder" : ""}`}
      // onDoubleClick={() => onToggle(task.id)}
    >
      <h3>
        {task.text}{" "}
        <FaTimes
          onClick={() => onDelete(task.id)}
          style={{ color: "red", cursor: "pointer" }}
        />
      </h3>
      <p>
        {task.length} in. &times; {task.width} in. &times; {task.height} in.
      </p>
    </div>
  );
};

export default Task;
