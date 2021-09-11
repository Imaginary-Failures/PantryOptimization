import React from "react";
import Pantry from "./Pantry";

const Pantries = ({ pantries, onDelete, onToggle }) => {
  return (
    <React.Fragment>
      {pantries.map((pantry) => (
        <Pantry
          key={pantry.id}
          pantry={pantry}
          onDelete={onDelete}
          onToggle={onToggle}
        />
      ))}
    </React.Fragment>
  );
};

export default Pantries;
