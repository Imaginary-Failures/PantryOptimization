import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import { Nav, Navbar, NavDropdown, Container } from "react-bootstrap";
import React, { Component } from "react";

function NavBar() {
  return (
    <Navbar bg="dark" variant="dark">
      <Container>
        <Navbar.Brand href="#home">Pantry Optimization</Navbar.Brand>
        <Nav className="me-auto">
          <Nav.Link href="http://localhost:3000/#home">Home</Nav.Link>
          <Nav.Link href="#features">Features</Nav.Link>
          <Nav.Link href="#pricing">About</Nav.Link>
        </Nav>
      </Container>
    </Navbar>
  );
}

export default NavBar;

// <ul>
//   <li>
//     <Link to="/Home">Home</Link>
//   </li>
//   <li>
//     <Link to="/PantryOptions">Pantry Options</Link>
//   </li>
// </ul>
