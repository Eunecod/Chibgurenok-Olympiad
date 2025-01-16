<script>
  import _axios from '@/util/axioshandler.js';

  import MessageBox from '@/components/MessageBox.vue';
  import Question from '@/components/Question.vue';
  import Timer from '@/components/Timer.vue';

  export default {
    props: ['id'],
    data() {
      return {
        timestamp:  0,
        quiz_body:  [],
        reply_body: [],

        messagebox_ask_show:  false,
        messagebox_info_show: false
      };
    },
    mounted() {
      this.InitQuiz();
    },
    components: {
      MessageBox,
      Question,
      Timer
    },
    methods: {
      InitQuiz() {
        const URL = '/quiz/' + this.id;
        _axios.get(URL).then(response => {
          this.quiz_body = response.data.quiz;
          this.timestamp = response.data.timestamp;
          this.ConstructReply();
        }).catch(error => {
          console.error(error);
        });
      },
      ConstructReply() {
        this.quiz_body.forEach((question, index) => {
          this.reply_body.push({ id: question.id, answer: null})
        });
      },
      RecordReply(question) {
        const index = this.reply_body.findIndex(reply => reply.id == question.id);
        if (index != -1)
          this.reply_body[index].answer = question.answer;
      },
      SubmitQuiz(answer) {
        answer && this.Submit();
      },
      Submit() {
        const URL = '/submit/quiz/' + this.id;
        let data = {
          reply_body: this.reply_body
        };
        _axios.post(URL, data).then(response => {
          this.$router.push({ name: 'Profile' });
        }).catch(error => {
          console.error(error);
        });
      }
    }
  }
</script>

<template>
  <div id="Quiz">

    <MessageBox :type="'question'" :header="'Завершить тестирование?'" :show="messagebox_ask_show" @update:show="messagebox_ask_show = $event" @update:answer="SubmitQuiz($event)">
      <template v-slot:messagebox-content>
        <div class="block">
          Вы точно хотите завершить тестирование? Ваши ответы будут записанны без возможности исправления.
        </div>
      </template>
    </MessageBox>

    <MessageBox :type="'info'" :header="'Время закончилось'" :show="messagebox_info_show" @update:show="messagebox_info_show = $event" @callback-submitted="Submit()">
      <template v-slot:messagebox-content>
        <div class="block">
          Время отведенное на тестирование закончилось. Ваши ответы сохраненны и отправленны.
        </div>
      </template>
    </MessageBox>

    <section class="section">
      <div class="container">

        <div class="is-flex is-align-items-center">
          <i class="fa-solid fa-clock"></i>
          <span class="ml-2">Оставшееся время:</span>
          <strong class="ml-1">
            <Timer v-if="this.timestamp" :expiration="this.timestamp" @stop-submitted="() => this.messagebox_info_show = true" />
          </strong>
        </div>

        <div class="container">
          <div class="column is-half is-offset-one-quarter">


            <div v-for="(question, index) in quiz_body" :key="index">
              <Question :data="question" @answer-submitted="RecordReply($event)"></Question>
            </div>

            <div class="buttons is-half is-right">
              <button class="button is-primary" @click="() => this.messagebox_ask_show = true">Завершить тестирование</button>
            </div>


          </div>
        </div>

      </div>
    </section>
  </div>
</template>
