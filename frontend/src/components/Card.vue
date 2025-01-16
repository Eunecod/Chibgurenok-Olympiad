<script>
  import { GetFileServer }   from '@/util/filehandler.js';
  import { FormatDate } from '@/util/time.js';

  export default {
    props: {
      data: {
        discipline: {
          subject:  '',
          level:    ''
        },
        passage_time: 0,
        access_date:  0,
        quiz:         0,
        title:        '',
        describe:     '',
        path_preview: '',
        active:       false,
      }
    },
    methods: {
      GetFileServer,
      FormatDate,
      OpenQuiz(quiz, event) {
        this.$router.push({ name: 'Quiz', params: { id: this.data.quiz } });  
      }
    }
  }
</script>

<template>
  <div id="Card" class="field">
    <div class="box">

      <div class="field">
        <span class="has-text-left has-text-weight-light"> <strong>Дисциплина:</strong> "{{this.data.discipline.subject}}" на базе {{this.data.discipline.level}} кл.</span>
      </div>

      <div class="columns">

        <div class="column">
          <figure class="image is-3by2">
            <img :src="GetFileServer(this.data.path_preview)"/>
          </figure>
        </div>

        <div class="column">
          <strong class="has-text-weight-bold"> {{this.data.title}} </strong>
          <div class="has-text-justified has-text-weight-light"> {{this.data.describe}} </div>
        </div>

      </div>

      <div class="columns is-vcentered">

        <div class="column">
          <div>
            <strong class="has-text-weight-bold"> Начало:  </strong>
            <span class="has-text-weight-light"> {{FormatDate(this.data.access_date)}} </span>
          </div>
          <div>
            <strong class="has-text-weight-bold"> Время:  </strong>
            <span class="has-text-weight-light"> {{this.data.passage_time}} минут </span>
          </div>
        </div>

        <div class="column">
          <button v-if="data.active" :id="data.quiz" class="button is-primary is-fullwidth" @click="(event) => OpenQuiz(data.quiz, event)">Начать олимпиаду</button>
          <button v-else class="button is-primary is-fullwidth" disabled>Начать олимпиаду</button>
        </div>

      </div>

    </div>
  </div>
</template>

