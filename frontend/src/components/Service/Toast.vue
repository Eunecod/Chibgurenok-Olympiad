<script>
  export default {
    props: {
      message: String,
      type: {
        type: String,
        default: 'info'
      },
      duration: {
        type: Number,
        default: 10000
      }
    },
    data() {
      return {
        visible: true
      };
    },
    mounted() {
      setTimeout(() => {
        this.Close();
      }, this.duration);
    },
    computed: {
      GetType() {
        return `is-${this.type}`;
      }
    },
    methods: {
      Close() {
        this.visible = false;        
      },
    },
  };
</script>

<template>

    <div id="Toast">
      <transition name="slide" appear>
      <div v-if="visible" :class="{'toast': true, 'message': true, [GetType]: true}" @click="Close()">

        <div class="field message-body">

          {{ this.message }}

        </div>

      </div>
      </transition>
    </div>

</template>

<style>
  .toast {
    position: fixed;
    z-index: 100;
    right: 0px;
    top: 10%;
  }

  .slide-enter-active, .slide-leave-active {
    transition: all 0.5s ease;
  }

  .slide-enter-from, .slide-leave-to {
    opacity: 0;
    transform: translateX(100%);
  }

  .slide-enter-to, .slide-leave-from {
    opacity: 1;
    transform: translateX(0);
  }
</style>
