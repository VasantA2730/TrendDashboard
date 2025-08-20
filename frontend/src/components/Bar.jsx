import React from "react";
import "./Bar.css";

function Bar({ height, scaledPixels, text }) {
  console.log(height + "px");

  const pixelHeight = height * scaledPixels;

  return (
    <div
      className="item"
      style={{
        height: pixelHeight + "px",
      }}
    >
      {text}
      <div className="tooltip-text"> {height} </div>
    </div>
  );
}

export default Bar;
