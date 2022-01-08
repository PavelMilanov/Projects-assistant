import React from "react";
import '../styles/Asside.scss'


class Asside extends React.Component {
    state = {

    }

    render() {
        return (
            <div className="Asside">
                <div>
                    <p>This is the status bar</p>
                </div>
                <main>
                    <div className="asside-menu">
                        
                    </div>
                </main>
            </div>
        )
    }
}

export {Asside}