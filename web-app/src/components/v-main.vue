<template>
    <div class="Main">
        <div>
            <p>This is the main menu</p>
        </div>
        <div>
            <div class="main-menu">
                <div class="status-bar">
                    <p>{{status_text ? status_text : ''}}</p>
                </div>
                <li class="list-menu">
                    <button
                        @click="generate_doc()" 
                        class="menu-btn">Сделать отчет
                    </button>
                    <button
                        @click="archive_cards()" 
                        class="menu-btn">Архивировать карточки
                    </button>
                    <button
                        @click="download_doc()" 
                        class="menu-btn">Отправить документ в архив
                    </button>
                    <button
                        @click="clear_doc()" 
                        class="menu-btn">Очистить документ
                    </button>
                </li>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            status_text: this.$store.getters.GET_INFO,
            token: this.$store.getters.GET_USER.token
        }
    },
    methods: {
        generate_doc() {
            this.$store.dispatch('GENERATE_DOCUMENT', this.token);
            let test = setTimeout(() => console.log(this.$store.getters.GET_INFO), 10)
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
    }
}
</script>

<style lang="less">
.main-menu {
    min-height: 100vh;

    .list-menu {
        margin-top: 0.5em;
        margin-bottom: 0.5em;
        display: grid;
        gap: 1em;
        justify-items: center;

        .list-item {
            width: 10em;
            text-align: center;
        }
    }

    .status-bar {
        text-align: center;
    }
}

.list-btn {
    width: 100%;
}

</style>