import React, { Component } from "react";

class Counter extends Component {
  state = {
    count: 0,
    imageUrl: "https://picsum.photos/200",
  };

  styles = {
    fontSize: 10,
    fontWeight: "bold",
  };

  render() {
    return (
      <React.Fragment>
        <img src={this.state.imageUrl} alt="" />

        <span style={this.styles} className={this.getBadgeClasses()}>
          {this.formatCount()}
        </span>
        <button className="btn btn-secondary btm-sm">Increment</button>
      </React.Fragment>
    );
  }

  getBadgeClasses() {
    let classes = "badge m-2 badge-";
    if (this.state.count == 0) {
      classes += "warning";
    } else {
      classes += "primary";
    }
    return classes;
  }

  formatCount() {
    const { count } = this.state;
    if (count == 0) {
      return "Zero";
    }
    return count;
  }
}

export default Counter;
