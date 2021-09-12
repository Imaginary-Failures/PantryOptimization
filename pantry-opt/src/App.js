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
import { Button, ProgressBar } from "react-bootstrap";
import Counters from "./components/counters";
import React, { Component, useEffect } from "react";
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
import ReactProgressMeter from "react-progress-meter";
import { propTypes } from "react-bootstrap/esm/Image";
import { useFrame, Canvas } from "@react-three/fiber";
import { OrbitControls, Stars } from "@react-three/drei";
// import { Physics, useBox } from "@react-three/cannon";

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

  function Box() {
    return (
      <mesh position={[0, 0, 0]}>
        <boxBufferGeometry attach="geometry" args={[4, 4, 4]} />
        <meshLambertMaterial attach="material" color="hotpink" />
      </mesh>
    );
  }

  function Sphere() {
    return (
      <mesh position={[0, 100, 0]}>
        <sphereBufferGeometry attach="geometry" />
        <meshLambertMaterial attach="material" color="lightblue" />
      </mesh>
    );
  }

  const [progress, setProgress] = useState(0);

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
      <ProgressBar now={progress} animated striped variant="success" />
      {pantries.length === 1 ? (
        ""
      ) : (
        <div className="containerPantry">
          <Canvas className="box">
            <OrbitControls />
            <ambientLight intensity={0.5} />
            <spotLight position={[10, 15, 10]} angle={0.5} />
            <Box />
            <Stars />
          </Canvas>
          <HeaderPantry
            onAdd={() =>
              setShowPantryAdd(!showPantryAdd && pantries.length <= 1)
            }
            showAdd={showPantryAdd}
          />

          {pantries.length > 0 ? (
            <Pantries
              pantries={pantries}
              onDelete={deletePantry}
              onToggle={toggleReminder}
            />
          ) : (
            ""
          )}
          {showPantryAdd ? (
            <AddPantry onAdd={addPantry} pantries={pantries} />
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
            <Button variant="primary" size="lg" active>
              Calculate
            </Button>
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
