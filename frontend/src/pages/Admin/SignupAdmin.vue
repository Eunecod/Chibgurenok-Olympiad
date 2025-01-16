<script>
  import _axios from '@/util/axioshandler.js';

  import Modal      from '@/components/Modal.vue';
  import Validate   from '@/components/Service/Validate.vue';

  export default {
    data() {
      return {
        login:    '',
        password: '',
        fullname: '',
      };
    },
    components: {
      Modal, Validate
    },
    methods: {
      Signup() {
        if (this.$refs.validate.Validate()) {
          const URL = '/admin/create/administrator';
          const data = {
            login:        this.login,
            password:     this.password,
            fullname:     this.fullname
          };          
          _axios.post(URL, data).then(response => {
              this.$router.push({ name: 'Main' });
              this.$push_toast('Администратор активирован.', { type: 'success', duration: 5000 });
          }).catch(error => {
              this.$push_toast('Отказанно в регистрации.', { type: 'danger', duration: 5000 });
          });          
        }
        else {
          this.$push_toast('Не все поля заполнены.', { type: 'danger', duration: 5000 });
        }
      },      
    }
  };
</script>

<template>
  <div id="SignupAdmin">

    <section class="section">

      <div class="container">
        <div class="column is-offset-one-fifth is-three-fifths">
          <div class="box">
            <div class="title is-4 has-text-centered"> Регистрации админа </div>

            <Validate ref="validate">            
              <div class="field">
                <div class="field">
                  <input v-model="login" class="input" type="text" placeholder="Логин" />
                </div>

                <div class="field">
                  <input v-model="password" class="input" type="password" placeholder="Пароль" />
                </div>

                <div class="field">
                  <input v-model="fullname" class="input" type="text" placeholder="ФИО" />
                </div>
              </div>                       

              <div class="buttons is-centered">
                <button class="button is-primary" @click="Signup()"> Зарегистрировать </button>
              </div>

            </Validate>

          </div>
        </div>
      </div>

    </section>
  </div>
</template>

<style>
</style>