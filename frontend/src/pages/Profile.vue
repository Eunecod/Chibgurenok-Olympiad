<script>
  import _axios from '@/util/axioshandler.js';

  import Card from '@/components/Card.vue';

  export default {
    data() {
      return {
        username:   '',
        olympiads:  []
      };
    },
    components: {
      Card
    },
    mounted() {
      this.GetProfile();
    },
    methods: {
      GetProfile() {
        const URL = '/profile';
        _axios.get(URL).then(response => {
          this.username = response.data.payload.usr.fullname;
          this.olympiads = response.data.olympiads;
        }).catch(error => {
          console.error(error);
        });
      },
    }
  }
</script>

<template>
  <div id="Profile">
    <section class="section">

      <div class="container">

        <h1 class="title"> Профиль </h1>
        <h2 class="subtitle is-hidden-mobile"> Здравствуйте, {{ this.username }}! </h2>

        <div class="columns is-multiline">
          <div class="column is-offset-one-fifth is-three-fifths" v-for="(olympiad, index) in olympiads" :key="index">
            <Card :data="olympiad" />
          </div>
        </div>

      </div>

    </section>
  </div>
</template>
