<script>
  export default {
    props: {
      show: {
        type: Boolean,
        default: false,
        required: true
      },
      header: {
        type: String,
        default: "",
        required: true
      },
      action: {
        type: Function,
        default: () => { console.log("Action is not stick modal."); },
        required: false
      },
      type: {
        type: String,
        default: "",
        required: false
      },
      clear: {
        type: Function,
        required: false
      }
    },
    methods: {
      Close() {
        this.$emit('update:show', false);
        if(this.clear) {
          this.clear();
        }
      },
      Apply() {
        this.action();
        this.Close();
      }
    }
  }
</script>

<template>
  <div id="Modal">

    <transition name="fade" appear>
      <div v-if="show" class="modal is-active">
        <div class="modal-background" @click="Close()"></div>
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title"> {{ this.header }} </p>
            <button class="delete is-hidden-mobile" @click="Close()"></button>
          </header>
          <section class="modal-card-body">

            <slot name="modal-content"></slot>

          </section>
          <footer v-if="type == 'modal'" class="modal-card-foot buttons is-right">
            <button class="button is-success" @click="Apply()">Создать</button>
            <button class="button" @click="Close()">Закрыть</button>
          </footer>

          <footer v-if="type == ''" class="modal-card-foot buttons is-right">
            <button class="button is-success" @click="Apply()">Принять</button>
            <button class="button" @click="Close()">Отмена</button>
          </footer>
        </div>
      </div>
    </transition>

  </div>
</template>

<style>
  .modal {
      transition: opacity 0.3s ease;
  }
  
  .modal.fade-enter-from, .modal.fade-leave-to {
     opacity: 0;
  }
  
  .modal.fade-enter-to, .modal.fade-leave-from {
    opacity: 1;
  }

  @media screen and (max-width: 768px) {
    .modal {
      --bulma-radius-large: 0.0rem;
    }

    .modal-card {
      height: 100vh;
      --bulma-modal-card-spacing: -0.5rem;
    }
  }
</style>
