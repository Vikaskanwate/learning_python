import { useState } from "react";
import API from "../api";

export default function Register({ goLogin }) {
  const [form, setForm] = useState({ name: "", email: "", password: "" });

  const handleRegister = async () => {
    try {
      await API.post("/auth/register", form);
      alert("Registered!");
      goLogin();
    } catch {
      alert("Register failed");
    }
  };

  return (
    <div className="flex flex-col items-center mt-20">
      <h1 className="text-2xl mb-4">Register</h1>

      <input placeholder="Name" className="border p-2 mb-2"
        onChange={(e) => setForm({ ...form, name: e.target.value })} />

      <input placeholder="Email" className="border p-2 mb-2"
        onChange={(e) => setForm({ ...form, email: e.target.value })} />

      <input type="password" placeholder="Password" className="border p-2 mb-2"
        onChange={(e) => setForm({ ...form, password: e.target.value })} />

      <button onClick={handleRegister} className="bg-green-500 text-white px-4 py-2">
        Register
      </button>
    </div>
  );
}