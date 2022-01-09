<template>
  <div class="App">
      <header>
        <p>header</p>
        <button>Log In</button>
      </header>
      <main>
        <vForm />
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
        
        }
    },
  components: {
    vMain,
    vAsside,
    vForm
  },

  methods: {

  }
}
</script>

<style lang="less" src="./main.less">

</style>
