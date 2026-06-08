import { useState } from "react";
import API from "../api";

export default function Login({ setToken, goRegister }) {
  const [form, setForm] = useState({ email: "", password: "" });

  const handleLogin = async () => {
    try {
      const res = await API.post("/auth/login", form);
      localStorage.setItem("token", res.data.access_token);
      setToken(res.data.access_token);
    } catch {
      alert("Login failed");
    }
  };

  return (
    // <div className="flex flex-col items-center mt-20">
    //   <h1 className="text-2xl mb-4">Login</h1>

    //   <input placeholder="Email" className="border p-2 mb-2"
    //     onChange={(e) => setForm({ ...form, email: e.target.value })} />

    //   <input type="password" placeholder="Password" className="border p-2 mb-2"
    //     onChange={(e) => setForm({ ...form, password: e.target.value })} />

    //   <button onClick={handleLogin} className="bg-blue-500 text-white px-4 py-2">
    //     Login
    //   </button>

    //   <p className="mt-3 cursor-pointer" onClick={goRegister}>
    //     Register instead
    //   </p>
    // </div>
    <div className="flex items-center justify-center  bg-[#00ADB5] h-screen">
      <div className="w-full max-w-xs h-">
        <form className="bg-[#EEEEEE] shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" for="username">
              Username
            </label>
            <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="email" placeholder="Username"
              onChange={(e) => setForm({ ...form, email: e.target.value })} />
          </div>
          <div className="mb-6">
            <label className="block text-gray-700 text-sm font-bold mb-2" for="password">
              Password
            </label>
            <input className="shadow appearance-none border  rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="password"
              onChange={(e) => setForm({ ...form, password: e.target.value })} />
            {/* <p className="text-red-500 text-xs italic">Please choose a password.</p> */}
          </div>
          <div className="flex items-center justify-between">
            <button className="bg-[#222831] hover:bg-[#393E46] text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button"
              onClick={handleLogin}>
              Sign In
            </button>
            <p className="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800 cursor-pointer"
              onClick={goRegister}>
              Register instead
            </p>
          </div>
        </form>
        {/* <p className="text-center text-gray-500 text-xs">
        &copy;2020 Acme Corp. All rights reserved.
      </p> */}
      </div>
    </div>

  );
}