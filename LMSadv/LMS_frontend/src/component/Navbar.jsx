 function Navbar({ onLogout }) {
    return (
      <div className="flex justify-between p-4 bg-gray-800 text-white">
        <h1>LMS</h1>
        <button onClick={onLogout} className="bg-red-500 px-3 py-1">
          Logout
        </button>
      </div>
    );
  }
export default Navbar