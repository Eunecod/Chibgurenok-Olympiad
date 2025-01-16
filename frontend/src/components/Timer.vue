<script>
  export default {
    props: {
      expiration: {
        type:     Number,
        required: true,
      },
    },
    data() {
      return {
        remaining_time: this.expiration,
        timer:          null,
      };
    },
    mounted() {
      this.Start();
    },
    beforeUnmount() {
      this.Stop();
    },
    computed: {
      FormatTime() {
        const hours   = Math.floor(this.remaining_time / 3600);
        const minutes = Math.floor((this.remaining_time % 3600) / 60);
        const seconds = this.remaining_time % 60;

        if (hours <= 0 && minutes <= 0 && seconds <= 0)
          return '00:00:00';

        return `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
      },
    },
    methods: {
      Start() {
        if (this.timer)
          return;

        this.timer = setInterval(() => {
          if (this.remaining_time > 0) {
            this.remaining_time--;
          }
          else {
            this.$emit('stop-submitted');
            this.Stop();
          }
        }, 1000);
      },
      Stop() {
        clearInterval(this.timer);
        this.timer = null;
      }
    }
  }
</script>

<template>
  <div class="Timer">
    <div> {{ FormatTime }} </div>
  </div>
</template>
