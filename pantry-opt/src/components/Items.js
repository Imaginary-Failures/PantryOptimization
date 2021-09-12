import React from "react";
import Item from "./Item";

const Items = ({ items, tasks, onDelete, onToggle }) => {
  return (
    <React.Fragment>
      {items.map((item) => (
        <Item
          key={item.id}
          item={item}
          onDelete={onDelete}
          onToggle={onToggle}
        />
      ))}
    </React.Fragment>
  );
};

export default Items;
