import { useState, useEffect } from "react";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";

function App() {
  const [token, setToken] = useState(null);
  const [page, setPage] = useState("login");

  useEffect(() => {
    const saved = localStorage.getItem("token");
    if (saved) setToken(saved);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    setToken(null);
    setPage("login");
  };

  if (!token) {
    return page === "login" ? (
      <Login setToken={setToken} goRegister={() => setPage("register")} />
    ) : (
      <Register goLogin={() => setPage("login")} />
    );
  }

  return <Dashboard onLogout={handleLogout} />;
}

export default App;