<script>
  import _axios from '@/util/axioshandler.js';
  import { DownloadCSV, ReadFieldCSV, ReadCSV } from '@/util/CSV.js';
  import { FilterInRange } from '@/util/filter.js'

  import Modal      from '@/components/Modal.vue';
  import Validate   from '@/components/Service/Validate.vue';

  export default {
    data() {
      return {
        disciplines:  [],

        subscribers:  [],
        discipline:   null,

        school:     '',
        level:      '',
        fullname:   '',

        show:     false,
        approval: false,

        file:  null,
        mode:  {
          user: true,
          csv:  false
        }
      };
    },
    mounted() {
      this.InitSignup();
    },
    components: {
      Modal, Validate
    },
    methods: {
      DownloadCSV,
      ReadFieldCSV,
      ReadCSV,
      FilterInRange,
      InitSignup() {
        const URL = '/get/disciplines';
        _axios.get(URL).then(response => {
          this.disciplines = response.data.disciplines;
        }).catch(error => {
          console.error(error);
        });
      },
      Signup() {
        if (!this.approval) {
          this.$push_toast('Не принято согласие на обработку персональных данных.', { type: 'danger', duration: 5000 });
        }
        else if (this.subscribers.length == 0) {
          this.$push_toast('Не выбранно не одной дисциплины.', { type: 'danger', duration: 5000 });
        }
        else {
          this.mode.user ? this.SignToUser() : this.SignToCSV();
        }
      },
      SignToUser() {
        if (this.$refs.validate.Validate()) {
          const URL = '/signup';
          const data = {
            level:        this.level,
            school:       this.school,
            fullname:     this.fullname,
            subscribers:  this.subscribers
          };

          let filter_subscriber = true;
          this.subscribers.forEach(subscriber => {            
            if (!FilterInRange(this.level, subscriber.level)) {
              filter_subscriber = false;
            }
          });

          if (filter_subscriber) {
            _axios.post(URL, data).then(response => {
              this.DownloadCSV(response.data.signup_csv, 'Пользователи');
              this.$router.push({ name: 'Main' });
              this.$push_toast('Заявка поданна.', { type: 'success', duration: 5000 });
            }).catch(error => {
              this.$push_toast('Отказанно в регистрации.', { type: 'danger', duration: 5000 });
            });
          }
          else {
            this.$push_toast('Регистрируемые пользователи не соотвествуют выбранной категории дисциплин.', { type: 'danger', duration: 5000 });
          }
        }
        else {
          this.$push_toast('Не все поля заполнены.', { type: 'danger', duration: 5000 });
        }
      },
      async SignToCSV() {
        if (this.file && this.$refs.validate.Validate()) {
          const URL = '/signup/csv';

          let filter_subscriber = true;
          let filter_class = await ReadFieldCSV(this.file, "Класс");
          this.subscribers.forEach(subscriber => {
            filter_class.forEach(level => {
              if (!FilterInRange(level, subscriber.level)) {
                filter_subscriber = false;
              }
            });
          });
          let csv = await this.ReadCSV(this.file);

          if (filter_subscriber) {
            let data = {
              CSV: csv,
              subscribers: this.subscribers
            }
            _axios.post(URL, data, {
            }).then(response => {
              this.DownloadCSV(response.data.signup_csv, 'Пользователи');
              this.$router.push({ name: 'Main' });
              this.$push_toast('Заявка поданна.', { type: 'success', duration: 5000 });
            }).catch(error => {
              this.$push_toast('Отказанно в регистрации.', { type: 'danger', duration: 5000 });
            });
          }
          else {
            this.$push_toast('Регистрируемые пользователи не соотвествуют выбранной категории дисциплин.', { type: 'danger', duration: 5000 });
          }
        }
        else {
          this.$push_toast('Не все поля заполнены.', { type: 'danger', duration: 5000 });
        }
      },
      LoadCSV(event) {
        this.file = event.target.files[0];
      },
      DownloadTemplate() {
        const URL = "/download/file/csv-student";
        _axios.get(URL, { responseType: 'blob' }).then(response => {
          const blob = new Blob([response.data], { type: 'text/csv;charset=utf-8;' });
          saveAs(blob, 'Шаблон.csv');
        }).catch(error => {
          console.log(error);
          this.$push_toast('Ошибка при загрузки шаблона.', { type: 'danger', duration: 5000 });
        });
      },
      ToogleMode() {
        this.mode.user = !this.mode.user;
        this.mode.csv  = !this.mode.csv;

        this.subscribers = [];
        this.discipline = null;

        this.school = '';
        this.level = '';
        this.fullname = '';
        this.file = null;

        this.approval = false;
      },
      AddSubscribe() {
        if (!this.discipline) return;

        if (this.subscribers.some(subscriber => subscriber.id == this.discipline)) 
            return; 
      
        const select_discipline = this.disciplines.find(discipline => discipline.id === this.discipline);
        if (select_discipline)
          this.subscribers.push(select_discipline);
      
        this.discipline = null;
      },
      DelSubscribe(id) {
        this.subscribers = this.subscribers.filter(subscriber => subscriber.id !== id);
      },
      SetApproval() {
        this.approval = true;
      }
    }
  };
</script>

<template>
  <div id="Signup">

    <Modal :header="'Согласие на обработку персональных данных'" :show="show" @update:show="show = $event" :action="SetApproval">
      <template v-slot:modal-content>
        <div class="content has-text-justified">
          Прочитав этот документы вы даете свое согласие на обработку моих персональных данных в соответствии с настоящим согласием.
          1. Персональные данные, на обработку которых дается согласие:
          Фамилия, имя, отчество
          Дата рождения
          Контактный телефон
          Адрес электронной почты
          Учебное заведение
          Класс/курс
          2. Цели обработки персональных данных:
          Участие в олимпиаде [название олимпиады].
          Информирование о мероприятиях, связанных с олимпиадой.
          Обработка результатов участия в олимпиаде.
          Подготовка и выдача сертификатов и дипломов участникам.
          3. Сроки хранения персональных данных:
          Персональные данные будут храниться в течение [указать срок хранения] после завершения олимпиады.
          4. Права участника:
          Я осознаю, что имею право:
          Запрашивать информацию о своих персональных данных, которые обрабатываются.
          Требовать исправления или удаления своих персональных данных.
          Отозвать данное согласие в любое время.
          5. Передача персональных данных третьим лицам:
          Я даю согласие на передачу моих персональных данных третьим лицам только в целях, указанных в настоящем согласии.
          6. Подтверждение согласия:
          Настоящим я подтверждаю, что ознакомлен с условиями обработки моих персональных данных и даю согласие на их обработку.
          Прочитав этот документы вы даете свое согласие на обработку моих персональных данных в соответствии с настоящим согласием.
          1. Персональные данные, на обработку которых дается согласие:
          Фамилия, имя, отчество
          Дата рождения
          Контактный телефон
          Адрес электронной почты
          Учебное заведение
          Класс/курс
          2. Цели обработки персональных данных:
          Участие в олимпиаде [название олимпиады].
          Информирование о мероприятиях, связанных с олимпиадой.
          Обработка результатов участия в олимпиаде.
          Подготовка и выдача сертификатов и дипломов участникам.
          3. Сроки хранения персональных данных:
          Персональные данные будут храниться в течение [указать срок хранения] после завершения олимпиады.
          4. Права участника:
          Я осознаю, что имею право:
          Запрашивать информацию о своих персональных данных, которые обрабатываются.
          Требовать исправления или удаления своих персональных данных.
          Отозвать данное согласие в любое время.
          5. Передача персональных данных третьим лицам:
          Я даю согласие на передачу моих персональных данных третьим лицам только в целях, указанных в настоящем согласии.
          6. Подтверждение согласия:
          Настоящим я подтверждаю, что ознакомлен с условиями обработки моих персональных данных и даю согласие на их обработку.
        </div>
      </template>
    </Modal>

    <section class="section">

      <div class="container">
        <div class="column is-offset-one-fifth is-three-fifths">
          <div class="box">
            <div class="title is-4 has-text-centered"> Форма регистрации </div>

            <div class="buttons my-1 is-right">

              <button class="button is-ghost" @click="ToogleMode()">

                <div v-if="mode.user">
                  <span> Загрузить </span>
                  <span class="is-hidden-mobile"> пользователей из файла </span>
                  <span class="icon"> <i class="fa-solid fa-file-csv"></i> </span>
                </div>

                <div v-if="mode.csv">
                  <span> Зарегистрировать </span>
                  <span class="is-hidden-mobile"> пользователя </span>
                  <span class="icon"> <i class="fa-solid fa-user-plus"></i> </span>
                </div>

              </button>

            </div>

            <Validate ref="validate">
              <div v-if="mode.user" class="field">
                <div class="field">
                  <input v-model="school" class="input" type="text" placeholder="Школа" />
                </div>

                <div class="field">
                  <input v-model="level" class="input" type="text" placeholder="Класс" />
                </div>

                <div class="field">
                  <input v-model="fullname" class="input" type="text" placeholder="ФИО студента" />
                </div>
              </div>
              
              <div v-if="mode.csv" class="field">
                <div class="field">
                  <button class="button is-fullwidth" @click="DownloadTemplate()"> 
                    <span> 
                      <i class="fa-solid fa-download"></i> 
                      Скачать Шаблон CSV  
                    </span>
                  </button>
                </div>

                <div class="field file has-name is-fullwidth">
                  <label class="file-label">
                    <input class="file-input" type="file" name="resume" @change="LoadCSV" accept=".csv" />
                    <span class="file-cta">
                      <span class="file-icon"> <i class="fas fa-upload"></i> </span>
                      <span class="file-label"> Загрузить файл CSV </span>
                    </span>
                    <span class="file-name"> {{ file ? file.name : 'Файл не выбран' }} </span>
                  </label>
                </div>  
              </div>

              <div class="field">

                <div class="level is-mobile">
                  <div class="select is-fullwidth">
                    <select v-model="discipline">

                      <option class="is-hidden" disabled selected value="null">Выберите дисциплину</option>
                      <option v-for="(discipline, index) in disciplines" :key="index" :value="discipline.id"> "{{ discipline.subject }}" на базе {{ discipline.level }} кл. </option>

                    </select>
                  </div>

                  <button class="button" @click="AddSubscribe()"> <span> <i class="fa-solid fa-plus"></i> Выбрать </span> </button>

                </div>

              </div>

              <div v-if="subscribers.length" class="field">
                <strong>Выбранные дисциплины:</strong>
                <div v-for="subscriber in subscribers" class="level is-mobile">
                  <p> "{{ subscriber.subject }}" на базе {{ subscriber.level }} кл.</p>
                  <button @click="DelSubscribe(subscriber.id)"><i class="fa-solid fa-xmark"></i></button>
                </div>
              </div>

              <div class="field">
                <label class="checkbox"> <input v-model="approval" type="checkbox" class="checkbox"/> </label>
                <a class="is-ghost" @click="() => show = true"> Согласие на обработку персональных данных. </a>
              </div>

              <div class="buttons is-centered">
                <button class="button is-primary" @click="Signup()"> Подать заявку </button>
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