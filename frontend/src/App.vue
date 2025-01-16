<script>
  import Navbar from '@/components/Navbar.vue';
  import Admin  from '@/components/Admin.vue';
  import Footer from '@/components/Footer.vue';

  import { Session } from '@/storage/session.js';
  import { provide } from 'vue';

  export default {
    setup() {
      const session = Session();
      provide('session', session);

      return {
        session,
      };
    },
    mounted() {
    },
    components: {
      Admin,
      Navbar, Footer
    }
  };
</script>

<template>
  <div id="app" class="app">
    <Navbar :autorized="session.GetAuthorized()"/>
    <Admin  :administrator="session.IsAdministrator()"/>
    <router-view/>
    <Footer/>
  </div>
</template>

<style>
  .app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    padding-top: 4rem;
    padding-bottom: 7rem;
  }
</style>
