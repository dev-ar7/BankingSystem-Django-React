import React from "react";
import App from './App';
import SignUp from "./Components/SignUp";
import { Route, Routes, BrowserRouter } from 'react-router-dom';


function Router() {
    return (
        <React.StrictMode>
            <BrowserRouter>
                <Routes>
                    <Route exact path="/" element={<App />} />
                    <Route exact path="/signup" element={<SignUp />} />
                </Routes>
            </BrowserRouter>
        </React.StrictMode>
    );
}


export default Router;