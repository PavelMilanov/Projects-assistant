<template>
    <div class="Main" v-if="main_auth">
        <div class="main-header">
            <p>Блок управления</p>
        </div>
        <div>
            <div class="main-menu">
                <div class="status-bar">
                    <p>{{text_status}}</p>
                </div>
                <li class="list-menu">
                    <button
                        @click="generate_doc()" 
                        class="menu-btn">Сгенерировать документ
                    </button>
                    <button
                        @click="archive_cards()" 
                        class="menu-btn">Архивировать карточки
                    </button>
                    <button
                        @click="download_doc()" 
                        class="menu-btn">Загрузить на сервер
                    </button>
                    <button
                        @click="upload_doc()" 
                        class="menu-btn">Выгрузить в Google Drive
                    </button>
                    <button
                        @click="clear_doc()" 
                        class="menu-btn">Очистить документ
                    </button>
                </li>
            </div>
        </div>
    </div>
    <div v-else>
        Необходима авторизация
    </div>
</template>


<script>

export default {
    data() {
        return {
            token: this.$store.getters.GET_USER.token
        }
    },
    methods: {
        generate_doc() {
            this.$store.dispatch('GENERATE_DOCUMENT', this.token);
        },
        clear_doc() {
            this.$store.dispatch('CLEAR_DOCUMENT', this.token);
        },
        download_doc() {
            this.$store.dispatch('DOWNLOAD_DOCUMENT', this.token);
        },
        archive_cards() {
            this.$store.dispatch('ARCHIVE_CARDS', this.token);
        },
    },
    computed: {
        main_auth() {
            return this.$store.getters.GET_USER.is_authenticated
        },
        text_status() {
            return this.$store.getters.GET_INFO
        }
    }
}
</script>

<style lang="less">

.main-header {
    text-align: center;
}

.main-menu {
    min-height: 100vh;

    .list-menu {
        margin-top: 1em;
        margin-bottom: 1em;
        display: grid;
        gap: 1em;
        justify-items: center;

        .list-item {
            width: 10em;
            text-align: center;
        }

        .menu-btn {
            width: 11em;
            height: 3em;
        }
    }

    .status-bar {
        height: 4em;
        text-align: center;
    }
}

.list-btn {
    width: 100%;
}

</style>