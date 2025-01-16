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
          options:  [],

          answer:   [],
          point:    0
        }),
      },
    },
    methods: {
      GetFileServer,
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
          <img :src="GetFileServer(data.image)" />
        </figure>

        <div class="field">
          <div class="has-text-weight-light"> {{ this.data.issue }} </div>
        </div>

        <div v-if="data.options" class="field" v-for="option in data.options">

          <label v-if="data.type == 'single'">
            <input v-model="data.answer" type="radio" :name="option" :value="option.id"/> {{ option.text }}
          </label>

          <label v-if="data.type == 'multiple'">
            <input v-model="data.answer" class="checkbox" type="checkbox" :value="option.id"/> {{ option.text }}
          </label>

        </div>

        <div v-if="data.type == 'text' || data.type == 'detailed'" class="field box">
          <div class="has-text-weight-light"> {{ this.data.answer }} </div>
        </div>


        <div class="field is-flex is-align-items-center is-justify-content-space-between">
          <p class="is-vcentered"> Кол-во баллов: </p>
          <input v-model="data.point" class="input" type="number" min="0" :max="data.score" style="width: 20%;"/>
        </div>

      </div>
    </div>

  </div>
</template>
