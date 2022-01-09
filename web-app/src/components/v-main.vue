<template>
    <div class="Main">
        <div>
            <p>This is the main menu</p>
        </div>
        <div>
            <div class="main-menu">
                <li class="list-menu">
                    <button class="menu-btn">Сделать отчет</button>
                    <button class="menu-btn">Архивировать карточки</button>
                    <button class="menu-btn">Отправить документ в архив</button>
                    <button class="menu-btn">Очистить документ</button>
                </li>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            
        }
    },
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