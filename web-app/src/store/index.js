import { createStore } from 'vuex'
import axios from 'axios';
import qs from 'qs';


export default createStore({
  state: {

    user: {
      is_authenticated: false,
      token: '',
    }
  },
  getters: {
    GET_USER: state => {
      return state.user
    },
  },
  mutations: {
    SET_USER_TOKEN: (state, data) => {
      state.user.token = data
    }
  },
  actions: {
    LOGIN: async (context, data) => {
      await axios({
            method: "POST",
            headers: { 'content-type': 'application/x-www-form-urlencoded' },
            url: 'http://localhost:8000/login',
            data: qs.stringify({
                'username': data.username,
                'password': data.password
            })
        }).then( (response) => {
          console.log(response);
          context.commit('SET_USER_TOKEN', response.data);
        }).catch( (error) => {
            console.log(error);
        })
    }
  }
})
