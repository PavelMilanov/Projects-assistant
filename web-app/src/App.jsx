import { Main } from './components/Main';
import { Asside } from './components/Asside';


function App() {
  return (
    <div className="App">
      <header>
        <p>header</p>
        <button>Log In</button>
      </header>
      <main>
        <Asside />
        <Main />
      </main>
    </div>
  );
}

export default App;
