<script>
  export default {
    props: {
      administrator: {
        type: Boolean,
        required: true,
      },
    },
    data() {
      return {
        count_not_read: 0,
      };
    },
    computed: {
      GetCountNotRead() {
        return this.count_not_read;
      }
    },
    methods: {

    }
  }
</script>

<template>
  <div v-if="administrator" id="Admin">

    <div class="box">
      <div>

        <div class="field has-text-weight-medium">Панель администратора</div>

        <nav class="level">

          <router-link to="/admin/olympiad" class="is-fullwidth">
            <button class="button is-fullwidth">
              <span class="icon is-small">
                <i class="fa-solid fa-graduation-cap"></i>
              </span>
              <span> Создание олимпиады </span>
            </button>
          </router-link>

          <router-link to="/admin/result" class="is-fullwidth">
            <button class="button is-fullwidth">
              <span class="icon is-small">
                <i class="fa-solid fa-book"></i>
              </span>
              <span> Результаты олимпиад </span>
            </button>
          </router-link>

          <router-link to="/admin/signup/administrator" class="is-fullwidth">
            <button class="button is-fullwidth">
              <span class="icon is-small">
                <i class="fa-solid fa-user"></i>
              </span>
              <span> Добавить администратора </span>
            </button>
          </router-link>

          <router-link to="/admin/mail" class="notification-container is-fullwidth">
            <button class="button is-fullwidth">
              <span class="icon is-small">
                <i class="fa-solid fa-comments"></i>
              </span>
              <span> Сообщение </span>
            </button>
            <span v-if="GetCountNotRead > 0" class="tag is-warning notification-badge has-text-black has-text-weight-bold"> {{GetCountNotRead}} </span>
          </router-link>

        </nav>

      </div>
    </div>

  </div>
</template>

<style>
  .is-fullwidth {
    width: 100%
  }

  .notification-container {
    position: relative;
    display: inline-block;
  }

  .notification-badge {
    position: absolute; 
    top: -5px; 
    right: -10px;
    z-index: 1; 
  }
</style>
