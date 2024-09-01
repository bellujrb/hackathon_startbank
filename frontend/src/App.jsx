import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import HomePage from "./Screens/HomePage";
import "./index.scss";
import centerpriceReceiverForm from "./Screens/BlocoPage1";

const App = () => {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/bloco1" element={<centerpriceReceiverForm />} /> {/* Rota para Bloco1 */}
                </Routes>
            </div>
        </Router>
    );
};

export default App;
