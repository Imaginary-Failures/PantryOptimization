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
import { Button } from "react-bootstrap";
import Counters from "./components/counters";
import React, { Component } from "react";
import { useState } from "react";
import Header from "./components/header";
import HeaderItem from "./components/headerItem";
import Tasks from "./components/Tasks";
import Pantries from "./components/Pantries";
import AddTask from "./components/AddTask";
import AddPantry from "./components/AddPantry";
import HeaderPantry from "./components/headerPantry";
import Calculations from "./components/page/calculations";
import AddItem from "./components/AddItem";
import Items from "./components/Items";
import { motion, useAnimation } from "framer-motion";
import { Transition } from "react-transition-group";
import Particles from "react-particles-js";

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
  const [items, setItems] = useState([]);
  const [showAddItem, setShowAddItem] = useState(false);

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

  //add Item
  const addItem = (item) => {
    const id = Math.floor(Math.random() * 10000 + 1);
    const newItem = { id, ...item };
    setItems([...items, newItem]);
  };

  //Delete task

  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !== id));
  };

  //Delete Pantry

  const deletePantry = (id) => {
    setPantries(pantries.filter((pantry) => pantry.id !== id));
  };

  //Delete item

  const deleteItem = (id) => {
    setItems(items.filter((item) => item.id !== id));
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

  //Method to calculate
  const calculate = () => {};

  return (
    <div className="App">
      <div className="particles"></div>
      <NavBar style={navStyle} />
      <Particles
        params={{
          particles: {
            number: {
              value: 50,
            },
            size: {
              value: 3,
            },
          },
          interactivity: {
            events: {
              onhover: {
                enable: true,
                mode: "repulse",
              },
            },
          },
        }}
      />
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
        <div>
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
              "No Shelves Available"
            )}
          </div>

          <div className="containerItems">
            <HeaderItem
              onAdd={() => setShowAddItem(!showAddItem)}
              showAdd={showAddItem}
              hide={() => setPantryInput(false)}
            />

            {showAddItem ? (
              <AddItem
                showAddItem={showAddItem}
                onAdd={addItem}
                pantries={pantries}
              />
            ) : (
              ""
            )}
            {items.length > 0 ? (
              <Items
                pantries={pantries}
                items={items}
                onDelete={deleteItem}
                onToggle={toggleReminder}
              />
            ) : (
              "No Items Available"
            )}
          </div>

          {items.length > 0 && tasks.length > 0 ? (
            <form method="GET" action="parse">
              <input hidden name="pantries" value={JSON.stringify(pantries)}></input>
              <input hidden name="items" value={JSON.stringify(items)}></input>
              <Button type="submit" calculate={calculate} variant="primary" size="lg" active>
                Calculate
              </Button>
            </form>
          ) : (
            ""
          )}
        </div>
      ) : (
        ""
      )}


      <Particles
        params={{
          particles: {
            number: {
              value: 50,
            },
            size: {
              value: 3,
            },
          },
          interactivity: {
            events: {
              onhover: {
                enable: true,
                mode: "repulse",
              },
            },
          },
        }}
      />
      <BrowserRouter>
        <Route path="/" component={PantryOptions} />
      </BrowserRouter>
    </div>
  );
};

export default App;
