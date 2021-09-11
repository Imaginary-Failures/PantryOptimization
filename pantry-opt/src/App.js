import logo from "./logo.svg";
import "./App.css";
import "./index.css";
import Home from "./Home";
import PantryOptions from "./PantryOptions";
import {
  Route,
  Link,
  Switch,
  BrowserRouter as Router,
  BrowserRouter,
  Redirect,
} from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import NavBar from "./components/NavBar";
import Counters from "./components/counters";
import React, { Component } from "react";
import { useState } from "react";
import Header from "./components/header";
import Tasks from "./components/Tasks";
import Pantries from "./components/Pantries";
import AddTask from "./components/AddTask";
import AddPantry from "./components/AddPantry";
import HeaderPantry from "./components/headerPantry";
import Calculations from "./components/page/calculations";

// function App() {
//   return (
//     <div className="App">
//       <NavBar />
//       <Route exact path="/Home" component={Home} />
//       <Route exact path="/PantryOptions" component={PantryOptions} />
//     </div>
//   );
// }
const App = () => {
  const [showAddTask, setShowAddTask] = useState(false);
  const [showPantryAdd, setShowPantryAdd] = useState(true);
  const [tasks, setTasks] = useState([]);
  //Pantry object
  const [pantries, setPantries] = useState([]);
  const [pantryInput, setPantryInput] = useState(true);

  //Add Pantry
  const addPantry = (pantry) => {
    const id = Math.floor(Math.random() * 10000 + 1);
    const newPantry = { id, ...pantry };
    setPantries([...pantries, newPantry]);
  };

  //add task
  const addTask = (task) => {
    const id = Math.floor(Math.random() * 10000 + 1);
    const newTask = { id, ...task };
    setTasks([...tasks, newTask]);
  };

  //Delete task

  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !== id));
  };

  //Delete Pantry

  const deletePantry = (id) => {
    setPantries(pantries.filter((pantry) => pantry.id !== id));
  };

  //Toggle reminder

  const toggleReminder = (id) => {
    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, reminder: !task.reminder } : task
      )
    );
  };

  const navStyle = {
    background: "black",
  };

  return (
    <div>
      <NavBar style={navStyle} />
      {pantries.length === 1 ? (
        ""
      ) : (
        <div className="containerPantry">
          <HeaderPantry
            onAdd={() =>
              setShowPantryAdd(!showPantryAdd && pantries.length <= 1)
            }
            showAdd={showPantryAdd}
          />

          {showPantryAdd ? (
            <AddPantry onAdd={addPantry} pantries={pantries} />
          ) : (
            ""
          )}
          {pantries.length > 0 ? (
            <Pantries
              pantries={pantries}
              onDelete={deletePantry}
              onToggle={toggleReminder}
            />
          ) : (
            ""
          )}
        </div>
      )}
      {pantries.length === 1 ? (
        <div className="containerShelf">
          <Header
            onAdd={() => setShowAddTask(!showAddTask)}
            showAdd={showAddTask}
            hide={() => setPantryInput(false)}
          />

          {showAddTask ? (
            <AddTask
              showAddTask={showAddTask}
              onAdd={addTask}
              pantries={pantries}
              home={Home}
              pantryOptions={PantryOptions}
            />
          ) : (
            ""
          )}
          {tasks.length > 0 ? (
            <Tasks
              pantries={pantries}
              tasks={tasks}
              onDelete={deleteTask}
              onToggle={toggleReminder}
            />
          ) : (
            "No Tasks Available"
          )}
        </div>
      ) : (
        ""
      )}
      <BrowserRouter>
        <Route path="/" component={PantryOptions} />
      </BrowserRouter>
    </div>
  );
};

export default App;
