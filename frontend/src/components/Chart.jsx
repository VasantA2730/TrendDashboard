import Bar from "./Bar.jsx";
import "./Chart.css";

function Chart({ data }) {
  const pixelPerCount = 500 / Math.max(...Object.values(data));

  return (
    <div className="container">
      {Object.entries(data).map((h, i) => (
        <Bar key={i} height={h[1]} scaledPixels={pixelPerCount} text={h[0]} />
      ))}
    </div>
  );
}

export default Chart;
