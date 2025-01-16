<script>
  import _axios from '@/util/axioshandler.js';

  import CardView from '@/components/CardView.vue';

  export default {
    data() {
      return {
        olympiads: []
      };
    },
    components: {
      CardView
    },
    mounted() {
      this.GetOlympiad();
    },
    methods: {
      GetOlympiad() {
        const URL = '/get/olympiads';
        _axios.get(URL).then(response => {
          this.olympiads = response.data.olympiads;
        }).catch(error => {
          console.error(error);
        });
      },
    }
  }
</script>

<template>

  <div id="Olympiad">
    <section class="section">
      <div class="container">

        <h1 class="title"> Олимпиады </h1>

        <div class="columns is-multiline">
          <div class="column is-offset-one-fifth is-three-fifths" v-for="(olympiad, index) in olympiads" :key="index">
            <CardView :data="olympiad" />
          </div>
        </div>

      </div>
    </section>
  </div>

</template>
