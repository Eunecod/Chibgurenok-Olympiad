<script>
  import _axios from '@/util/axioshandler.js';
  import { inject } from 'vue';

  import Toast      from '@/components/Service/Toast.vue';
  import Validate   from '@/components/Service/Validate.vue'; 

  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    setup() {
      const session = inject('session');
      return {
        session,
      };
    },
    components: {
      Toast, Validate
    },
    methods: {
      Login() {
        let data = {
          username: this.username,
          password: this.password
        };
        const URL = '/login';
        if (this.$refs.validate.Validate()) {
          _axios.post(URL, new URLSearchParams(data)).then(response => {
            this.session.SetAuthorized(response.data.autorized, response.data.grand);
            this.$router.push({ name: 'Profile' });   
          }).catch(error => {
            this.$push_toast('Неверный логин или пароль.', { type: 'danger', duration: 5000 });
          });
        }
        else {
          this.$push_toast('Не все поля заполнены.', { type: 'danger', duration: 5000 });
        }
      }
    }
  };
</script>

<template>
  <div id="Login">

    <section class="section">

      <div class="container is-flex is-align-items-center is-justify-content-center">

        <div class="column is-one-third">
          <div class="box">

            <div class="title is-4 has-text-centered"> Форма авторизации </div>

            <Validate ref="validate">       
              <form>
                <div class="field">
                  <p class="control has-icons-left">
                    <input v-model="username" class="input" autocomplete="username" type="text" placeholder="Логин" />
                    <span class="icon is-small is-left">
                      <i class="fa-solid fa-user"></i>
                    </span>
                  </p>
                </div>

                <div class="field">
                  <p class="control has-icons-left">
                    <input v-model="password" class="input" type="password" autocomplete="current-password" placeholder="Пароль" />
                    <span class="icon is-small is-left">
                      <i class="fa-solid fa-key"></i>
                    </span>
                  </p>
                </div>

                <div class="buttons is-centered">
                  <button type="button" class="button is-primary" @click="Login()">Войти</button>
                </div>
              </form>
            </Validate>


          </div>
        </div>

      </div>

    </section>
  </div>
</template>


<style>
</style>
