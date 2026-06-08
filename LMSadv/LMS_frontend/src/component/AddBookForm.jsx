import { useState } from "react";
import API from "../api";

export default function AddBookForm({ refresh }) {
  const [form, setForm] = useState({
    title: "",
    author: "",
    total_copies: 1,
  });

  const handleAdd = async () => {
    await API.post("/books", form);
    refresh();
  };

  return (
    <div className="border p-3 mb-4">
      <h2>Add Book</h2>

      <input placeholder="Title" className="border p-1 mr-2"
        onChange={(e) => setForm({ ...form, title: e.target.value })} />

      <input placeholder="Author" className="border p-1 mr-2"
        onChange={(e) => setForm({ ...form, author: e.target.value })} />

      <input type="number" className="border p-1 mr-2"
        onChange={(e) => setForm({ ...form, total_copies: Number(e.target.value) })} />

      <button onClick={handleAdd} className="bg-purple-500 text-white px-3 py-1">
        Add
      </button>
    </div>
  );
}