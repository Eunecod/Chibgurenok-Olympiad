<script>
  import _axios from '@/util/axioshandler.js';

  import Modal from '@/components/Modal.vue';
  import Blank from '@/components/Admin/Blank.vue';
  import Toast from '@/components/Service/Toast.vue';

  import { UploadFile, GetUniqueName }  from '@/util/filehandler.js';
  import { DateNow, FormatDatestamp }   from '@/util/time.js';

  export default {
    data() {
      return {
        total_score:  0,
        disciplines:  [],

        olympiad: {
          title:    '',
          describe: '',
          image:    {
            name:   '',
            source: '',
            file:   null,
          },
          discipline:   0,
          passage_time: 0,
          access_date:  this.DateNow(),
          document:     {
            name: '',
            file: null
          }
        },

        questions: [],

        show_discipline: false,
        discipline: {
          subject:  '',
          level:    ''
        },
      };
    },
    mounted() {
      this.InitOlympiad();
    },
    components: {
      Modal, Blank, Toast
    },
    methods: {
      DateNow,
      InitOlympiad() {
        const URL = '/get/disciplines';
        _axios.get(URL).then(response => {
          this.disciplines = response.data.disciplines;
        }).catch(error => {
          console.error(error);
        });
      },
      AddDiscipline() {
        const URL = '/admin/create/discipline';
        if (true) {
          _axios.post(URL, this.discipline).then(response => {
            this.disciplines = response.data.disciplines;
          }).catch(error => {
            console.error(error);
          });
        }
        else {
          this.$push_toast('Не все поля заполнены.', { type: 'danger', duration: 5000 });
        }
      },
      ClearDiscipline() {
        this.discipline.subject = '';
        this.discipline.level   = '';
      },
      RecalcTotalScore() {
        this.total_score = 0;
        this.questions.forEach(question => {
          this.total_score += question.score;
        });
      },
      LoadImage(event) {
        const file = event.target.files[0];
        if (file) {
          const reader = new FileReader();
          const buffer_file = new File([file], GetUniqueName(file.name), { type: file.type });
          reader.onload = (e) => {
            this.olympiad.image.name    = buffer_file.name;
            this.olympiad.image.source  = e.target.result;
            this.olympiad.image.file    = buffer_file;
          };
          reader.readAsDataURL(file);
          event.target.value = '';
        }
      },
      RemoveImage() {
        this.olympiad.image.name    = '';
        this.olympiad.image.source  = '';
        this.olympiad.image.file    = null;
      },
      LoadDocument() {
        const file = event.target.files[0];
        if (file) {
          const reader = new FileReader();
          const buffer_file = new File([file], GetUniqueName(file.name), { type: file.type });
          reader.onload = (e) => {   
            this.olympiad.document.file = buffer_file;
            this.olympiad.document.name = buffer_file.name;
          };
          reader.readAsDataURL(file);
          event.target.value = '';
        }
      },
      RemoveDocument() {
        this.olympiad.document.name = '';
        this.olympiad.document.file = null;
      },
      AddQuestion() {
        this.questions.push({
          id:       this.questions.length,
          score:    0,
          issue:    '',
          type:     '',
          image:    {
            name:   '',
            source: '',
            file:   null,
          },
          options:  [],
          correct:  [],
        });
      },
      DelQuestion(id) {
        this.questions = this.questions.filter(question => question.id !== id);
        this.questions.forEach((question, index) => {
          question.id = index;
        });
      },
      CreateOlympiad() {
        const URL = '/admin/create/olympiad';
        if (true) {
          this.olympiad.access_date = FormatDatestamp(this.olympiad.access_date);

          let images = [ this.olympiad.image.file ]
          this.questions.forEach(question => {
            if (question.image.file != null)
              images.push(question.image.file);
          });
          UploadFile(images);

          let document = [ this.olympiad.document.file ]
          UploadFile(document);
        
          let data = {
            olympiad:   this.olympiad,
            questions:  this.questions,
          }
          _axios.post(URL, data).then(response => {
            this.$router.push({ name: 'Main' });  
          }).catch(error => {
            console.error("Не дошел ответ.");
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

  <div id="OlympiadAdmin">

    <Modal :type="'modal'" :header="'Создать новую дисциплину'" :show="show_discipline" @update:show="show_discipline = $event" :action="AddDiscipline" :clear="ClearDiscipline">
      <template v-slot:modal-content>
        <div class="field">
          <input v-model="discipline.subject" class="input" placeholder="Название предмета" />
        </div>
        <div class="field">
          <input v-model="discipline.level" class="input" placeholder="Возрастная группа (класс)" />
        </div>
      </template>
    </Modal>

    <section class="section">
      <div class="container">

        <p class="field"> <span class="icon"> <i class="fa-solid fa-star"></i> </span> <strong> Суммарное кол-во баллов: {{ total_score }}/100 </strong> </p>
        <p class="field"> <span class="icon"> <i class="fa-solid fa-circle-question"></i> </span> <strong> Суммарное кол-во вопросов: {{ questions.length }} </strong> </p>

        <div class="column is-half is-offset-one-quarter">

          <div class="box">

            <div class="title is-4 has-text-centered"> Форма создания теста </div>

            <div class="field">
              <input v-model="olympiad.title" class="input" placeholder="Название теста" />
            </div>

            <div class="file field is-fullwidth">
              <label class="file-label">
                <input class="file-input" type="file" name="resume" @change="(event) => LoadImage(event)" />
                <span class="file-cta">
                  <span class="file-icon"> <i class="fas fa-upload"></i> </span>
                  <span class="file-label"> Загрузить файл </span>
                </span>
                <span class="file-name"> {{ olympiad.image.source ? olympiad.image.name : 'Файл не выбран'}} </span>
              </label>
            </div>

            <div v-if="olympiad.image.source" class="block">
              <figure class="field image is-16by9">
                <img :src="olympiad.image.source" />
                <div class="buttons is-right">
                  <button class="delete is-medium m-2" @click="RemoveImage()"></button>
                </div>
              </figure>
            </div>

            <div class="field">
              <textarea v-model="olympiad.describe" class="textarea" type="text" placeholder="Описание олимпиады" />
            </div>

            <div class="columns field is-vcentered">

              <div class="column is-fullwidth">
                <label> Время тестирования: </label>
              </div>
              <div class="column is-fullwidth">
                <input v-model="olympiad.passage_time" class="input is-fullwidth" type="number" />
              </div>

            </div>

            <div class="columns field is-vcentered">

              <div class="column is-fullwidth">
                <label> Дата проведения: </label>
              </div>
              <div class="column is-fullwidth">
                <input v-model="olympiad.access_date" class="input is-fullwidth" type="date" />
              </div>

            </div>

            <div class="field">
              <div class="select is-fullwidth">
                <select v-model="olympiad.discipline">

                  <option class="is-hidden" disabled selected value=0> Выберите дисциплину </option>
                  <option v-for="(discipline, index) in disciplines" :key="index" :value="discipline.id"> "{{ discipline.subject }}" на базе {{ discipline.level }} </option>

                </select>
              </div>
            </div>

            <div class="buttons">
              <button class="button is-fullwidth" @click="() => show_discipline = true">
                <span class="icon"> <i class="fa-solid fa-pen"></i> </span>
                <span> Добавить новую дисциплину </span>
              </button>

              <div class="file field is-fullwidth">
                <label class="file-label">
                  <input class="file-input" type="file" name="resume" @change="(event) => LoadDocument(event)" />
                  <span class="file-cta">
                    <span class="file-icon"> <i class="fas fa-upload"></i> </span>
                    <span class="file-label"> Загрузить файл </span>
                  </span>
                  <span class="file-name"> {{ this.olympiad.document.file ? this.olympiad.document.name : 'Файл не выбран'}} </span>
                </label>
              </div>
            </div>

            <div v-if="this.olympiad.document.file" class="box">              
              <div class="level is-mobile">
                <i class="fa-solid fa-file fa-2x"></i>
                <button class="delete is-medium" @click="RemoveDocument()"></button>
              </div>
              <label>Прикрепленный документ:</label>
              <p>{{this.olympiad.document.name}}</p>
            </div>

          </div>

          <div class="field" v-for="(question, index) in questions" :key="index">

            <Blank :data="question" @delete-submitted="DelQuestion($event)" @recalc-submitted="RecalcTotalScore()"></Blank>

          </div>

          <div class="level is-half buttons is-centered">
            <div class="column">
              <button class="button is-primary is-fullwidth" @click="AddQuestion()"> Добавить вопрос </button>
            </div>
            <div v-if="questions.length" class="column">
              <button class="button is-warning is-fullwidth" @click="CreateOlympiad()"> Завершить создание </button>
            </div>
          </div>

        </div>


      </div>
    </section>

  </div>
</template>
