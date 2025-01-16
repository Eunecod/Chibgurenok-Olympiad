<script>
  import { GetFileServer } from '@/util/filehandler.js';

  export default {
    props: {
      data: {
        type: Object, 
        required: true, 
        default: () => ({
          id:       0,
          type:     '',
          score:    0,
          issue:    '',
          image:    '',
          options:  []
        }),
      },
    },
    data() {
      return {
        reply: {
          id:     this.data.id,
          answer: [],
        },
        single_answer:    [],
        multiple_answer:  [],
        text_answer:      [],
        detailed_answer:  [],
      };
    },
    methods: {
      GetFileServer,
      RecordAnswer(answer) {
        this.reply.answer = answer;
        this.$emit('answer-submitted', this.reply);
      }
    }
  }
</script>

<template>
  <div id="Question">

    <div class="column">
      <div class="box">
        <div class="field is-flex is-justify-content-space-between">
          <span class="has-text-weight-bold"> Вопрос: №{{ this.data.id + 1 }} </span>
          <span class="tag has-text-weight-bold is-primary is-normal">балл: {{ this.data.score }}</span>
        </div>


        <figure v-if="data.image" class="image field is-3by2">
          <img :src="GetFileServer(data.image)"/>
        </figure>

        <div class="field">
          <div class="has-text-weight-light"> {{ this.data.issue }} </div>
        </div>

        <div v-if="data.options" class="field" v-for="option in data.options">

          <label v-if="data.type == 'single'">
            <input v-model="single_answer" type="radio" :name="option" :value="option.id" @change="RecordAnswer(single_answer)"/> {{ option.text }}
          </label>

          <label v-if="data.type == 'multiple'">
            <input v-model="multiple_answer" class="checkbox" type="checkbox" :value="option.id" @change="RecordAnswer(multiple_answer)"/> {{ option.text }}
          </label>

        </div>

        <div class="field">
          <label v-if="data.type == 'text'">
            <input v-model="text_answer" class="input" type="text" placeholder="Ответ" @change="RecordAnswer(text_answer)"/>
          </label>

          <label v-if="data.type == 'detailed'">
            <textarea v-model="detailed_answer" class="textarea" type="text" placeholder="Развернутый ответ"  @change="RecordAnswer(detailed_answer)"/>
          </label>
        </div>

 
      </div>
    </div>
    
  </div>
</template>
