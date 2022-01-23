<template>
    <div class="Asside" v-if="asside_auth">
        <div>
            <p>This is the status bar</p>
        </div>
        <main>
            <div class="asside-menu">
                
            </div>
        </main>
    </div>
</template>

<script>

export default {
    data() {
        return {
            auth: this.$store.getters.GET_USER.is_authenticated
        }
    },
    methods: {

    },
    computed: {
        asside_auth() {
            return this.$store.getters.GET_USER.is_authenticated
        }
    }
}
</script>

<style lang="less">

</style>