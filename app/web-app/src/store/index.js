import { createStore } from 'vuex'
import axios from 'axios';
import qs from 'qs';


export default createStore({
  state: {
    info: null,
    user: {
      is_authenticated: false,
      token: '',
    }
  },
  getters: {
    GET_USER: state => state.user
    ,
    GET_INFO: state => state.info
    ,
  },
  mutations: {
    SET_USER_IS_AUTH: (state, data) => {
      state.user.token = data
      state.user.is_authenticated = true
    },
    SET_INFO: (state, data) => {
      state.info = data
    },
    SET_INFO_DEFAULT: state => {
      state.info = null
    }
  },
  actions: {
    LOGIN: async (context, data) => {
      await axios({
            method: 'POST',
            headers: { 'content-type': 'application/x-www-form-urlencoded' },
            url: 'http://0.0.0.0/api/login',
            data: qs.stringify({
                'username': data.username,
                'password': data.password
            })
      }).then(response => {
          context.commit('SET_USER_IS_AUTH', response.data);
        }).catch( error => {
            console.log(error);
        })
    },
    GENERATE_DOCUMENT: async (context, data) => {
      await axios({
        method: 'GET',
        headers: { 'Authorization': `Bearer ${data}`},
        url: 'http://0.0.0.0/api/generate'
      }).then(response => {
        context.commit('SET_INFO', response.data)
      }).catch(error => {
        console.log(error)
      })
    },
    CLEAR_DOCUMENT: async (context, data) => {
      await axios({
        method: 'GET',
        headers: { 'Authorization': `Bearer ${data}` },
        url: 'http://0.0.0.0/api/clear'
      }).then(response => {
        context.commit('SET_INFO', response.data)
      }).catch(error => {
        console.log(error)
      })
    },
    DOWNLOAD_DOCUMENT: async (context, data) => {
      await axios({
        method: 'GET',
        headers: { 'Authorization': `Bearer ${data}` },
        url: 'http://0.0.0.0/api/download'
      }).then(response => {
        context.commit('SET_INFO', response.data)
      }).catch(error => {
        console.log(error)
      })
    },
    UPLOAD_DOCUMENT: async (context, data) => {
      await axios({
        method: 'POST',
        headers: { 'Authorization': `Bearer ${data}` },
        url: 'http://0.0.0.0/api/upload'
      }).then(response => {
        context.commit('SET_INFO', response.data)
      }).catch(error => {
        console.log(error)
      })
    },
    ARCHIVE_CARDS: async (context, data) => {
      await axios({
        method: 'POST',
        headers: { 'Authorization': `Bearer ${data}` },
        url: 'http://0.0.0.0/api/archive'
      }).then(response => {
        context.commit('SET_INFO', response.data)
      }).catch(error => {
        console.log(error)
      })
    },
  },
})
