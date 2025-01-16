<script>
  export default {
    props: {
      answer: {
        type: Boolean,
        required: false
      },
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
      type: {
        type: String,
        default: "",
        required: true
      }
    },
    data() {
      return {
        answer_messagebox: false
      };
    },
    methods: {
      Close() {
        this.$emit('update:show', false);        
        this.$emit('update:answer', this.answer_messagebox);

        this.$emit('callback-submitted');
      },
      Answer(choice) {
        switch (choice) {
          case 'OK':
            this.answer_messagebox = true;
            break;
          case 'Cancel':
            this.answer_messagebox = false;
            break;
        };
        this.Close();
      }
    }
  }
</script>

<template>
  <div id="MessageBox">

    <transition name="fade" appear>
      <div v-if="show" class="modal is-active">
        <div class="modal-background"></div>

        <div class="modal-card">
          <section class="modal-card-body box">

            <div class="field">
              <p class="title is-5"> {{ this.header }} </p>
            </div>


            <slot name="messagebox-content">
            </slot>

            <div v-if="type == 'question'" class="buttons is-right">
              <button class="button is-success" @click="Answer('OK')">Подтвердить</button>
              <button class="button is-danger" @click="Answer('Cancel')">Отмена</button>
            </div>

            <div v-if="type == 'info'" class="buttons is-right">
              <button class="button" @click="Answer('OK')">Принять</button>
            </div>

          </section>
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
