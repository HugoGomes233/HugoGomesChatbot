import React, { useState , useEffect} from "react";
import Chat from "./Chat";
import "./FloatingButton.css";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
/**
 * FloatingButton component renders a floating chat button.
 * When clicked, it toggles the chat window.
 * Adapts layout for mobile and desktop screens.
 */
function FloatingButton() {
  const [openChat, setOpenChat] = useState(false);
  const [isBotOnline, setIsBotOnline] = useState(false); // Bot online status
  const[initialMessages, setInitialMessages] = useState([])
  // Determine if the device is mobile based on viewport width
  const isMobile = window.innerWidth <= 768;

  
  // -----------------------------
  // Check bot status
  // -----------------------------
  useEffect(() => {
    const checkStatus = async () => {
      try {
        console.log(`${BACKEND_URL}/status`)
        // Send GET request to check if bot is online
        const res = await fetch(`${BACKEND_URL}/status`, {
          method: "GET",
          headers: { "Content-Type": "application/json" },
        });

        //Check response status
        if (!res.ok) throw new Error("Bot is offline");
        // If online, update state and show welcome message
        setIsBotOnline(true)
        setInitialMessages([{ sender: "bot", text: "Hello! How can I assist you today?" }]);
      } catch (err) {
        setInitialMessages([{ sender: "bot", text: "I am offline! Please contact administrator" }]);        
      }
    };
 // Initial status check on component mount
    checkStatus();
  }, []);

  return (
    <div>
      {/* Floating chat button */}
      <button
        className={`floating-btn ${isMobile ? "mobile" : "desktop"}`}
        onClick={() => setOpenChat(!openChat)}
      >
        🤖
      </button>

      {/* Conditionally render chat window */}
      {openChat && (
        <div className={`chat-window ${isMobile ? "mobile" : "desktop"}`}>
          {/* Pass onClose callback to allow Chat to close itself */}
          <Chat initialMessages={initialMessages} isBotOnline={isBotOnline } onClose={() => setOpenChat(false)} />
        </div>
      )}
    </div>
  );
}

export default FloatingButton;
