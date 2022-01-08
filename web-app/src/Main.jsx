import React from "react";
import './Main.scss';


class Main extends React.Component {
    state = {
    
    }

    render() {
        return (
            <div className="container">
                <header>
                    <div className="header-menu">
                        <p>This is the main menu</p>
                        <button>Log In</button>
                    </div>
                </header>
                <main>
                    <div className="main-menu">
                        <li className="list-menu">
                            <button className="menu-btn">Сделать отчет</button>
                            <button className="menu-btn">Архивировать карточки</button>
                            <button className="menu-btn">Отправить документ в архив</button>
                            <button className="menu-btn">Очистить документ</button>
                        </li>
                    </div>
                </main>
            </div>
        )
    }
}

export { Main }