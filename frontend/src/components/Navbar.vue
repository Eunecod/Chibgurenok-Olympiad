<script>
  import _axios from '@/util/axioshandler.js';
  import { inject } from 'vue';

  export default {
    props: {
      autorized: {
        type: Boolean,
        required: true,
      },
    },
    data() {
      return {
        is_active: false,
      };
    },
    setup() {
      const session = inject('session');
      return {
        session
      };
    },
    methods: {
      ToggleMenu() {
        this.is_active = !this.is_active;
      },
      Logout() {
        const URL = '/logout';
        _axios.get(URL).then(response => {
          this.session.SetAuthorized(false);
          this.$router.push({ name: 'Main' });   
        }).catch(error => {
          console.error(error);
        });
        this.ToggleMenu();
      }
    }
  }
</script>

<template>
  <div id="Navbar">
    
    <nav class="navbar has-shadow is-fixed-top" role="navigation">
    
      <div class="navbar-brand">
        <router-link to="/">
          <a class="navbar-item">
            <figure class="image is-64x64 is-hidden-mobile">
              <img style="max-height: 100%" src="@/assets/logo.png" alt="logo-chibgurenok" />
            </figure>
            <div class="mx-2">
              <strong class="title">ЧИБГУРЁНОК</strong>
              <p class="title is-6 has-text-weight-light">Региональный конкурс</p>
            </div>
          </a>
        </router-link>
        <a role="button" :class="{'navbar-burger': true, 'is-active': is_active}" @click="ToggleMenu" aria-label="menu" aria-expanded="false">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>


      <div :class="{'navbar-menu': true, 'is-active': is_active}">
      
        <div class="navbar-start" @click="ToggleMenu()">
          <router-link to="/olympiad" class="navbar-item">
            <a class="navbar-item"> Олимпиады </a>
          </router-link>
          <router-link to="/rules" class="navbar-item">
            <a class="navbar-item"> Правила </a>
          </router-link>
          <router-link to="/result" class="navbar-item">
            <a class="navbar-item"> Итоги </a>
          </router-link>
          <router-link to="/contact" class="navbar-item">
            <a class="navbar-item"> Контакты </a>
          </router-link>
        </div>
      
        <div class="navbar-end">
          <div class="navbar-item">
            <div v-if="autorized" class="columns is-mobile">
              <div class="column">
                <router-link to="/profile">
                  <button class="button is-link is-fullwidth" @click="ToggleMenu()">Профиль</button>
                </router-link>
              </div>
              <div class="column">
                <button class="button is-link is-fullwidth" @click="Logout()">Выйти</button>
              </div>
            </div>
            <div v-else class="columns is-mobile">
              <div class="column">
                <router-link to="/signup">
                  <button class="button is-link is-fullwidth" @click="ToggleMenu()">Регистрация</button>
                </router-link>
              </div>
              <div class="column">
                <router-link to="/login">
                  <button class="button is-link is-fullwidth" @click="ToggleMenu()">Войти</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>

      
    </nav>
  </div>
</template>

<style>

</style>
