import React from "react";


class Form extends React.Component {
    state = {
        login: null,
        password: null
    };

    handleChange = (event) => {
        this.setState({ [event.target.name]: event.target.value });
        this.setState({ [event.target.password]: event.target.value });
    }

    render() {
        return (
            <div>
                <input type="text"
                    name="login"
                    placeholder="Логин"
                    value={this.state.login}
                    onChange={this.handleChange} />
                <input type="password"
                    name="password"
                    placeholder="Пароль"
                    value={this.state.password}
                    onChange={this.handleChange} />
            </div>
        )
    }
}

export {Form}