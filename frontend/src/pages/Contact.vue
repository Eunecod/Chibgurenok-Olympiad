<script>
  import Toast from '@/components/Service/Toast.vue';

  export default {
    components: {
      Toast
    },
    methods: {
      Submit() {
        this.$push_toast('Ваш ответ записан и отправлен нам.', { type: 'success', duration: 5000 });
      }
    }
  }
</script>

<template>

  <div id="Contact">
    <section class="section">
      <div class="container">

        <h1 class="title">Контакты</h1>

        <div class="columns">
          <div class="column is-half is-flex">

            <div class="card is-flex-grow-1">
              <div class="card-image">
                <figure class="image is-4by3">
                  <img src="@/assets/logo_BGU.png" style="object-fit: cover;" alt="Placeholder image" />
                </figure>
              </div>
              <div class="card-content">
                <div class="media">
                  <div class="media-content">
                    <p class="title is-4">Читинский институт БГУ</p>
                    <p class="subtitle is-6">Организатор ЧИБГУрёнка</p>
                  </div>
                </div>

                <div class="content has-text-justified">
                  Эта олимпиада — отличная возможность продемонстрировать свои знания и раскрыть творческий потенциал. Не бойтесь ставить перед собой высокие цели и стремиться к их достижению
                </div>
              </div>
            </div>


          </div>

          <div class="column is-half is-flex">
            <div class="box is-flex-grow-1">

              <div class="is-flex is-flex-direction-column" style="height: 100%;">
                <h2 class="subtitle has-text-centered">Форма обратной связи</h2>

                <div class="is-fullwidth is-flex is-justify-content-center">
                  
                    <figure class="image is-128x128">
                      <img style="max-height: 100%" src="@/assets/logo_paper.png" alt="logo-chibgurenok" />
                    </figure>
             
                </div>

                <div class="field">
                  <label class="label">Имя</label>
                  <div class="control">
                    <input type="text" class="input" placeholder="Ваше имя" required />
                  </div>
                </div>

                <div class="field">
                  <label class="label">Email</label>
                  <div class="control">
                    <input type="email" class="input" placeholder="Ваш email" required />
                  </div>
                </div>

                <div class="field">
                  <label class="label">Сообщение</label>
                  <div class="control">
                    <textarea class="textarea" placeholder="Ваше сообщение" required></textarea>
                  </div>
                </div>

                <div class="buttons is-right mt-auto">
                  <button class="button is-link" @click="Submit()">Отправить</button>
                </div>
              </div>

            </div>
          </div>

        </div>

        <div class="box">
          <h2 class="subtitle has-text-centered">Нас можно найти здесь</h2>

          <div class="columns">
            <div class="column has-text-centered">
              <strong>Адрес:</strong>
              <p>ул. Анохина, д.56, г. Чита</p>
            </div>
            <div class="column has-text-centered">
              <strong>Телефон:</strong>
              <p>(3022) 32-34-21</p>
            </div>
            <div class="column has-text-centered">
              <strong>Email:</strong>
              <p>abit@bgu-chita.ru</p>
            </div>
          </div>
          
          <div style="position:relative;overflow:hidden;">
            <a href="https://yandex.ru/maps/68/chita/search/%D1%87%D0%B8%D1%82%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B8%D0%BD%D1%81%D1%82%D0%B8%D1%82%D1%83%D1%82%20%D0%B1%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">читинский институт байкальский государственный университет в Чите</a>
            <a href="https://yandex.ru/maps/68/chita/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:14px;">Чита</a>
            <iframe src="https://yandex.ru/map-widget/v1/?display-text=%D1%87%D0%B8%D1%82%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B8%D0%BD%D1%81%D1%82%D0%B8%D1%82%D1%83%D1%82%20%D0%B1%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82&ll=113.506827%2C52.029055&mode=search&sctx=ZAAAAAgBEAAaKAoSCXcQO1PoulRAEZuvko%2Fdg0tAEhIJqHNFKSFY3j8R3PEmv0UnxT8iBgABAgMEBSgKOABAvKcNSAFqAnJ1nQHNzMw9oAEAqAEAvQFRVUFzwgELsbu7sATo3aTdtgSCAnDRh9C40YLQuNC90YHQutC40Lkg0LjQvdGB0YLQuNGC0YPRgiDQsdCw0LnQutCw0LvRjNGB0LrQuNC5INCz0L7RgdGD0LTQsNGA0YHRgtCy0LXQvdC90YvQuSDRg9C90LjQstC10YDRgdC40YLQtdGCigIAkgIAmgIMZGVza3RvcC1tYXBz&sll=113.506827%2C52.029055&sspn=0.007408%2C0.002773&text=%D1%87%D0%B8%D1%82%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B8%D0%BD%D1%81%D1%82%D0%B8%D1%82%D1%83%D1%82%20%D0%B1%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82&z=17" width="100%" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe>
          </div>
        </div>

      </div>
    </section>
  </div>

</template>

<style>

</style>
