import React from "react";
import './Main.scss';


class Main extends React.Component {
    state = {
    
    }

    render() {
        return (
            <div>
                <header>
                    This is the main menu</header>
                <main>
                    <div className="menu">
                        <li className="menu-list">
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