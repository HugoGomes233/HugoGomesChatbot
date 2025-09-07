import CVViewer from "./components/Curriculum";
import FloatingButton from "./components/FloatingButton";

/**
 * Root application component.
 * Renders the floating chat button and the curriculum (CV) viewer.
 * The chat button overlays the CV viewer, allowing interactive assistance.
 */
function App() {
    return (
        <>
            {/* Floating chat assistant */}
            <FloatingButton />

            {/* Main CV content */}
            <CVViewer />
        </>
    );
}

export default App;
