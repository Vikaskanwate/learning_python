 function BookCard({ book, onIssue, onReturn }) {
    return (
      <div className="border p-3 mb-2">
        <h2 className="font-bold">{book.title}</h2>
        <p>{book.author}</p>
        <p>Available: {book.available_copies}</p>
  
        <button onClick={() => onIssue(book._id)}
          className="bg-blue-500 text-white px-2 py-1 mr-2">
          Issue
        </button>
  
        <button onClick={() => onReturn(book._id)}
          className="bg-green-500 text-white px-2 py-1">
          Return
        </button>
      </div>
    );
  }


  export default BookCard