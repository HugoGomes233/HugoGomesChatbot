import React, { useState } from "react";
import Chat from "./Chat";
import "./FloatingButton.css";

/**
 * FloatingButton component renders a floating chat button.
 * When clicked, it toggles the chat window.
 * Adapts layout for mobile and desktop screens.
 */
function FloatingButton() {
  const [openChat, setOpenChat] = useState(false);

  // Determine if the device is mobile based on viewport width
  const isMobile = window.innerWidth <= 768;

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
          <Chat onClose={() => setOpenChat(false)} />
        </div>
      )}
    </div>
  );
}

export default FloatingButton;
