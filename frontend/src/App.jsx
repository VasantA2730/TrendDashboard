// import { useState } from "react";
// import reactLogo from "./assets/react.svg";
// import viteLogo from "/vite.svg";
// import "./App.css";
import { BarChart } from "@mui/x-charts/BarChart";
import Bar from "./components/Bar.jsx";
import Chart from "./components/Chart.jsx";
import { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState(null);
  const [isLoading, setLoading] = useState(true);

  // async function getData() {
  //   const response = await fetch("/api/data");
  //   setData(await response.json());
  //   setLoading(false);
  //   // console.log(data);
  // }

  useEffect(() => {
    async function getData() {
      const response = await fetch("/api/data");
      setData(await response.json());
      setLoading(false);
      // console.log(data);
    }
    getData();
  }, []);

  console.log(data);
  // const pixelPerCount = 300 / Math.max(...Object.values(data));

  if (isLoading) {
    return "Loading";
  } else {
    return (
      // <div>
      //   {Object.entries(data).map((h, i) => (
      //     <Bar height={h[1]} scaledPixels={pixelPerCount} text={h[0]} />
      //   ))}
      // </div>
      <Chart data={data} />
    );
  }
}

export default App;
