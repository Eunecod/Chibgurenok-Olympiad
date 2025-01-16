<script>
  import _axios from '@/util/axioshandler.js';
  import Answer from '@/components/Admin/Answer.vue';

  export default {
    props: ['id'],
    data() {
      return {
        quiz_body:  [],
        reply_body: [],

        answer_body: []
      };
    },
    mounted() {
      this.InitReply();
    },
    components: {
      Answer
    },
    computed: {
      GetFinalScore() {
        let final_score = 0;
        this.answer_body.forEach(question => {
          final_score += question.point ? question.point : 0;
        });
        return final_score;
      },
      ConstructAnswer() {
        this.answer_body = this.quiz_body.map(quiz => {
          const reply = this.reply_body.find(r => r.id === quiz.id);

          return {
            id:       quiz.id,
            type:     quiz.type,
            score:    quiz.score,
            issue:    quiz.issue,
            image:    quiz.image,
            options:  quiz.options,
            answer:   reply ? reply.answer : [],
            point:    reply.point,
          };
        });
        return this.answer_body;
      },
    },
    methods: {
      InitReply() {
        const URL = '/admin/get/reply/' + this.id;
        _axios.get(URL).then(response => {
          this.quiz_body = response.data.quiz_body;
          this.reply_body = response.data.reply_body;
        }).catch(error => {
          console.error(error);
        });
      },
      UpdateReply() {
        const URL = '/admin/update/reply/' + this.id;
        const reply_body = this.answer_body.map(item => {
          return {
            id: item.id,
            answer: item.answer,
            point: item.point,
          };
        });

        let data = {
          assessed: this.GetFinalScore,
          reply_body: reply_body
        };
        _axios.post(URL, data).then(response => {
          this.$router.push({ name: 'ResultAdmin' }); 
        }).catch(error => {
          console.error(error);
        });
      }
    }
  }
</script>

<template>
  <div id="ReplyAdmin">

    <section class="section">
      <div class="container">

        <p class="field"> <span class="icon"> <i class="fa-solid fa-star"></i> </span> <strong> Кол-во баллов: {{GetFinalScore}}/100 </strong> </p>

        <div class="container">
          <div class="column is-half is-offset-one-quarter">


            <div v-for="(question, index) in ConstructAnswer" :key="index">
              <Answer :data="question"></Answer>
            </div>

            <div class="buttons is-half is-right">
              <button class="button is-warning" @click="UpdateReply()">Сохранить</button>
            </div>


          </div>
        </div>


      </div>
    </section>

  </div>
</template>
