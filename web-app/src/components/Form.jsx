import React from "react";
import '../styles/Form.scss';
import axios from 'axios';
import qs from 'qs';


class Form extends React.Component {
    state = {
        username: '',
        password: ''
    };

    handleChange = (event) => {
        this.setState({ [event.target.name]: event.target.value });
        this.setState({ [event.target.name]: event.target.value });
    }

    login = () => {
        axios({
            method: "POST",
            headers: { 'content-type': 'application/x-www-form-urlencoded' },
            url: 'http://localhost:8000/login',
            data: qs.stringify({
                'username': this.state.username,
                'password': this.state.password
            })
        }).then(function (response) {
            console.log(response);
        }).catch(function (error) {
            console.log(error);
        })
    }

    render() {
        return (
            <div className="form">
                <input type="text"
                    className="form-input input1"
                    name="username"
                    placeholder="Логин"
                    value={this.state.username}
                    onChange={this.handleChange} />
                <input type="password"
                    className="form-input input2"
                    name="password"
                    placeholder="Пароль"
                    value={this.state.password}
                    onChange={this.handleChange} />
                <button
                    className="form-button"
                    onClick={this.login}>Submit
                </button>
            </div>
        )
    }
}

export {Form}