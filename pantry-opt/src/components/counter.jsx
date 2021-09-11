import React, { Component } from "react";

class Counter extends Component {
  //   constructor() {
  //     super();
  //     this.handleIncrement = this.handleIncrement.bind(this);
  //   }

  styles = {
    fontSize: 10,
    fontWeight: "bold",
  };

  renderTags() {
    return (
      <ul>
        {this.state.tags.map((tag) => (
          <li key={tag}>{tag}</li>
        ))}
      </ul>
    );
  }

  render() {
    return (
      <React.Fragment>
        {this.props.children}
        <span style={this.styles} className={this.getBadgeClasses()}>
          {this.formatCount()}
        </span>

        <button
          onClick={() => this.props.onIncrement(this.props.counter)}
          className="btn btn-secondary btn-sm m-2"
        >
          Increment
        </button>

        <button
          onClick={() => this.props.onDecrement(this.props.counter)}
          className="btn btn-secondary btn-sm m-2"
        >
          Decrement
        </button>

        <button
          onClick={() => this.props.onDelete(this.props.counter.id)}
          className="btn btn-danger btn-sm m-2"
        >
          Delete
        </button>
      </React.Fragment>
    );
  }

  getBadgeClasses() {
    let classes = "badge m-2 badge-";
    const { value } = this.props.counter;
    if (value <= 0) {
      classes += "warning";
    } else if (value >= 10) {
      classes += "danger";
    } else {
      classes += "success";
    }
    return classes;
  }

  formatCount() {
    const { value } = this.props.counter;
    return value <= 0 ? 0 : value;
  }
}

export default Counter;
