<template>
  <div class="App">
      <header>
        <p class="header-name">Project Assistant v0.1.1</p>
        <button class="header-button"
          @click="openForm()"
          >Log In
        </button>
      </header>
      <main>
        <vForm 
        :status="status"
        @closeForm="closeForm()"/> 
        <vAsside />
        <vMain />
      </main>
    </div>
</template>

<script>
import vMain from '@/components/v-main.vue';
import vAsside from '@/components/v-asside.vue';
import vForm from '@/components/v-form.vue';


export default {
  name: 'App',
  data() {
        return {
          // для стиля компонента vForm
          status: 'hidden'
        }
    },
  components: {
    vMain,
    vAsside,
    vForm
  },
 
  methods: {
    openForm() {
      this.status = 'visible';
    },

    closeForm() {
      this.status = 'hidden';
    }

  },

}
</script>

<style lang="less" src="./main.less">

</style>
