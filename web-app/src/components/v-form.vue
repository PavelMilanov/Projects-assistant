<template>
    <div class="Form">
        <a href="#" class="btn-exit">X
        </a>
        <input
            v-model.lazy="form.username" 
            type="text"
            class="form-input input1"
            placeholder="Логин"
            />
        <input 
            v-model.lazy="form.password"
            type="password"
            class="form-input input2"
            placeholder="Пароль"
            />
        <button
            class="btn-sub"
            @click="login()"
        >Submit
        </button>
    </div>
</template>

<script>

export default {
    data() {
        return {
            form: {
                username: null,
                password: null
            }
        }
    },

    methods: {
        login () {
            this.$store.dispatch("LOGIN", this.form)
        },

        clear_input() {
            this.form.username = null
            this.form.password = null
        }
    }
}
</script>

<style lang="less">

.Form {
    visibility: visible;
    position: absolute;
    left: 25%;
    top: 25%;
    width: 20em;
    height: 15em;
    border: 1px solid black;
    display : grid;
    justify-items: center;
    padding-top: 3em;
    z-index: 2;
    
    .form-input {
        height: 30%;
        width: 85%;
    }

    .btn-sub {
        height: 40%;
        width: 60%;
    }

    .btn-exit {
        position: absolute;
        left: 90%;
        top: 1%;
        color: black;
        text-decoration: none;
    }

}


</style>
