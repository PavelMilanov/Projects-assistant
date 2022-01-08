import React from "react";
import '../styles/Main.scss'


class Main extends React.Component {
    state = {
    
    }

    render() {
        return (
            <div className="Main">
                <div>
                    <p>This is the main menu</p>
                </div>
                <div>
                    <div className="main-menu">
                        <li className="list-menu">
                            <button className="menu-btn">Сделать отчет</button>
                            <button className="menu-btn">Архивировать карточки</button>
                            <button className="menu-btn">Отправить документ в архив</button>
                            <button className="menu-btn">Очистить документ</button>
                        </li>
                    </div>
                </div>
            </div>
        )
    }
}

export { Main }