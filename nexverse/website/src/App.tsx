import { HelmetProvider } from 'react-helmet-async';
import AppNavigation from './navigation/Navigation';
import { useEffect } from 'react';
import { animationCreate } from "./utils/utils";

function App() {

  useEffect(() => {
    // animation
    const timer = setTimeout(() => {
      animationCreate();
    }, 100);

    return () => clearTimeout(timer);
  }, []);

  return (
    <>
      <HelmetProvider>
        <AppNavigation />
      </HelmetProvider>
    </>
  );
}

export default App;
