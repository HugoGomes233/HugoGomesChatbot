import React, { useState, useRef, useEffect } from "react";
import "./Chat.css";

// -----------------------------
// Avatar images for user and bot
// -----------------------------
const userAvatar = "/no-picture.png"; 
const botAvatar = "/personal_data_picture.jpg";

// -----------------------------
// Chat Component
// -----------------------------
function Chat({ onClose }) {
  // -----------------------------
  // State hooks
  // -----------------------------
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Hello! How can I assist you today?" }, // initial message
  ]);
  const [input, setInput] = useState("");       // Text input value
  const [loading, setLoading] = useState(false); // Loading state for async request
  const [isTyping, setIsTyping] = useState(false); // Typing indicator for bot

  // -----------------------------
  // Reference to the bottom of the chat
  // -----------------------------
  const chatEndRef = useRef(null);

  // -----------------------------
  // Auto-scroll effect
  // -----------------------------
  // Scrolls to the bottom whenever messages or typing status changes
  useEffect(() => {
    if (chatEndRef.current) {
      chatEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages, isTyping]);

  // -----------------------------
  // Handle sending message
  // -----------------------------
  const handleSend = async () => {
    if (!input) return; // Prevent sending empty messages

    // Add user message to state
    setMessages((prev) => [...prev, { sender: "user", text: input }]);
    setInput("");          // Clear input field
    setLoading(true);      // Show loading state
    setIsTyping(true);     // Show "Hugo is writing..." indicator

    try {
      // Send query to backend API
      const res = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: input }),
      });

      const data = await res.json();

      // Add bot response to state
      setMessages((prev) => [...prev, { sender: "bot", text: data.answer }]);
    } catch (err) {
      console.error(err);

      // Handle API errors gracefully
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "Error contacting backend." },
      ]);
    }

    setLoading(false);      // Reset loading state
    setIsTyping(false);     // Stop typing indicator
  };

  // -----------------------------
  // Handle Enter key press
  // -----------------------------
  // Allows sending message on Enter while Shift+Enter creates new line
  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  // -----------------------------
  // JSX structure
  // -----------------------------
  return (
    <div className="chat-container">
      {/* Top Bar */}
      <div className="chat-header">
        <img src={botAvatar} alt="bot" className="chat-avatar" />
        <span className="chat-name">Hugo Gomes</span>
        <span className="chat-status">● Online</span>
        {/* Close button */}
        <button className="chat-close-btn" onClick={onClose}>✖</button>
      </div>

      {/* Messages */}
      <div className="chat-messages">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`chat-message-row ${
              msg.sender === "user" ? "user" : "bot"
            }`}
          >
            {/* Avatar on the left for bot */}
            {msg.sender === "bot" && (
              <img src={botAvatar} alt="bot" className="chat-avatar" />
            )}

            {/* Message bubble */}
            <div
              className={`chat-bubble ${
                msg.sender === "user" ? "user" : "bot"
              }`}
            >
              {msg.text}
            </div>

            {/* Avatar on the right for user */}
            {msg.sender === "user" && (
              <img src={userAvatar} alt="user" className="chat-avatar" />
            )}
          </div>
        ))}

        {/* Dummy div to allow scrolling to bottom */}
        <div ref={chatEndRef}></div>

        {/* Typing indicator */}
        {isTyping && <div className="typing-indicator">Hugo is writing...</div>}
      </div>

      {/* Input Area */}
      <div className="chat-input-area">
        <textarea
          rows="2"
          placeholder="Type a message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyPress}
          className="chat-input"
        />
        <button
          onClick={handleSend}
          disabled={loading}
          className="chat-send-btn"
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default Chat;
