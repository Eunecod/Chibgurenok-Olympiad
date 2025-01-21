<script>
  import { GetUniqueName } from '@/util/filehandler.js';


  export default {
    props: {
      data: {
        type: Object,
        required: true,
        default: () => ({
          id:       0,
          score:    0,
          issue:    '',
          type:     '',
          image:    {
            name:   '',
            source: '',
            file:   null,
          },
          options: [],
          correct: [],
        }),
      },
    },
    data() {
      return {
        single_correct:    [],
        multiple_correct:  [],
        text_correct:      [],
        detailed_correct:  [],
      };
    },
    methods: {
      DelQuestion() {
        this.$emit('delete-submitted', this.data.id);
        this.RecalcScore();
      },
      AddOption() {
        this.data.options.push({
          id:       this.data.options.length,
          text:     '',
        });
      },
      LoadImage(event) {
        const file = event.target.files[0];
        if (file) {
          const reader = new FileReader();
          const buffer_file = new File([file], GetUniqueName(file.name), { type: file.type });
          reader.onload = (e) => {
            this.data.image.name    = buffer_file.name;
            this.data.image.source  = e.target.result;
            this.data.image.file    = buffer_file;
          };
          reader.readAsDataURL(file);
          event.target.value = '';
        }
      },
      RemoveImage() {
        this.data.image.name    = '';
        this.data.image.source  = '';
        this.data.image.file    = null;
      },
      DelOption(id) {
        this.data.options = this.data.options.filter(option => option.id !== id);
        this.data.options.forEach((option, index) => {
          option.id = index;
        });
      },
      ResetOptions() {
        this.data.options = [];
      },
      SetCorrect(correct) {
        this.data.correct = correct;
        correct = [];
      },
      RecalcScore() {
        this.$emit('recalc-submitted');
      }
    }
  }
</script>

<template>
  <div id="Blank">

    <div class="box">

      <div class="level is-mobile">
        <strong>ID: {{ this.data.id }} </strong>
        <div class="buttons is-right" @click="DelQuestion()"> <button class="button is-danger icon"> <i class="fa-solid fa-trash"></i> </button> </div>
      </div>

      <div class="file is-fullwidth">
        <label class="file-label">
          <input class="file-input" type="file" name="resume" @change="(event) => LoadImage(event)"/>
          <span class="file-cta">
            <span class="file-icon"> <i class="fas fa-upload"></i> </span>
            <span class="file-label"> Загрузить файл </span>
          </span>
          <span class="file-name"> {{ this.data.image.source ? this.data.image.name : 'Файл не выбран'}} </span>
        </label>
      </div>

      <div v-if="data.image.source" class="block">
        <figure class="field image is-16by9">
          <img :src="data.image.source" />
          <div class="buttons is-right">
            <button class="delete is-medium m-2" @click="RemoveImage()"></button>
          </div>
        </figure>
      </div>

      <div class="field">
        <textarea v-model="data.issue" class="textarea" type="text" placeholder="Вопрос" />
      </div>

      <div class="columns is-mobile">

        <div class="column">

          <div class="field">
            <div class="select is-fullwidth">
              <select v-model="data.type" @change="ResetOptions()">

                <option value='' class="is-hidden" disabled selected> Выберите тип вопроса </option>
                <option value=single> Один ответ </option>
                <option value=multiple> Много ответов </option>
                <option value=text> Открытый ответ </option>
                <option value=detailed> Развернутый ответ </option>

              </select>
            </div>
          </div>

        </div>

        <div class="column">
          <div class="field">
            <input v-model="data.score" class="input" type="number" min="0" max="100" placeholder="Оценка за вопрос" @change="RecalcScore()"/>
          </div>
        </div>

      </div>

      <div class="field" v-for="(option, index) in data.options" :key="index">

        <div v-if="data.type == 'single'" :name="data.id" class="field level is-mobile">
          <input v-model="single_correct" type="radio" :value="option.id" @change="SetCorrect(single_correct)" />
          <input v-model="option.text" class="input" placeholder="Ответ" />

          <button class="button" @click="DelOption(option.id)"> <span> <i class="fa-solid fa-xmark"></i> </span> </button>
        </div>

        <div v-if="data.type == 'multiple'" :name="data.id" class="field level is-mobile">
          <input v-model="multiple_correct" class="checkbox" type="checkbox" :value="option.id" @change="SetCorrect(multiple_correct)" />
          <input v-model="option.text" class="input" placeholder="Ответ" />

          <button class="button" @click="DelOption(option.id)"> <span> <i class="fa-solid fa-xmark"></i> </span> </button>
        </div>

        <div v-if="data.type == 'text'" :name="data.id" class="field level is-mobile">
          <input v-model="text_correct[index]" class="input" type="text" placeholder="Ответ" @change="SetCorrect(text_correct)"/>

          <button class="button" @click="DelOption(option.id)"> <span> <i class="fa-solid fa-xmark"></i> </span> </button>
        </div>

      </div>

      <div v-if="data.type == 'detailed'" :name="data.id" class="field level is-mobile">
        Развернутый ответ по данному вопросу.
      </div>

      <div v-if="data.type != '' && data.type != 'detailed'" class="field">
        <button class="button is-fullwidth" @click="AddOption()"> <span> <i class="fa-solid fa-plus"></i> </span> </button>
      </div>

    </div>

  </div>
</template>
