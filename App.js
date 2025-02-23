import React, { useState } from 'react';
import './App.css';

function App() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  const handleInputChange = (event) => {
    setQuestion(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!question.toLowerCase().startsWith("what if")) {
      setResponse("I can only answer 'What If' questions. Try something fun, like 'What if cats ruled the world?' 😼");
      return;
    }

    try {
      const res = await fetch('http://localhost:8000/what-if', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_input: question }),
      });

      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      setResponse(`Oops! My circuits got tangled! Error: ${error.message} 🤖💥`);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>What If Machine</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={question}
            onChange={handleInputChange}
            placeholder="Ask a 'What If' question..."
          />
          <button type="submit">Ask</button>
        </form>
        {response && <p className="response">{response}</p>}
      </header>
    </div>
  );
}

export default App;