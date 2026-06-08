import { useEffect, useState } from "react";
import API from "../api";
import Navbar from "../component/Navbar"
import AddBookForm from "../component/AddBookForm";
import BookCard from "../component/BookCard"
export default function Dashboard({ onLogout }) {
  const [books, setBooks] = useState([]);
  const [role, setRole] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchBooks = async () => {
    try {
      const res = await API.get("/books/");
      setBooks(res.data);
    } catch {
      alert("Failed to fetch books");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchBooks();

    const token = localStorage.getItem("token");
    if (token) {
      const payload = JSON.parse(atob(token.split(".")[1]));
      setRole(payload.role);
    }
  }, []);

  const issueBook = async (id) => {
    try {
      await API.post("/transactions/issue/", { book_id: id });
      alert("Book issued");
      fetchBooks();
    } catch (err) {
      alert(err.response?.data?.detail || "Issue failed");
    }
  };

  const returnBook = async (id) => {
    try {
      await API.post("/transactions/return/", { book_id: id });
      alert("Book returned ");
      fetchBooks();
    } catch (err) {
      alert(err.response?.data?.detail || "Return failed");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar onLogout={onLogout} role={role} />

      <div className="max-w-5xl mx-auto p-6">

        {/* Admin Section */}
        {role === "admin" && (
          <>
            <h2 className="text-xl font-semibold mb-3"> Add Book</h2>
            <AddBookForm refresh={fetchBooks} />
          </>
        )}

        {/* Books Section */}
        <h2 className="text-xl font-semibold mt-6 mb-3"> All Books</h2>

        {loading ? (
          <p className="text-center text-gray-500">Loading books...</p>
        ) : books.length === 0 ? (
          <p className="text-center text-gray-500 mt-6">
            No books available
          </p>
        ) : (
          books.map((b) => (
            <BookCard
              key={b._id}
              book={b}
              onIssue={issueBook}
              onReturn={returnBook}
            />
          ))
        )}
      </div>
    </div>
  );
}