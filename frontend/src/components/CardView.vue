<script>
  import _axios from '@/util/axioshandler.js';
  import { GetFileServer }   from '@/util/filehandler.js';
  import { FormatDate } from '@/util/time.js';

  import Modal from '@/components/Modal.vue';

  export default {
    props: {
      data: {
        discipline: {
          subject:  '',
          level:    ''
        },
        passage_time: 0,
        access_date:  0,
        title:        '',
        describe:     '',
        path_preview: '',
        document:     ''
      }
    },
    methods: {
      GetFileServer,
      FormatDate,
      DownloadDocument() {
        const URL = '/download/file/' + this.data.document;
        _axios.get(URL, { responseType: 'blob' }).then(response => {
          const blob = response.data;
          const object_URL = window.URL.createObjectURL(blob);
          const new_filename = this.data.title; 

          const link = document.createElement('a');
          link.href = object_URL;
          link.download = new_filename; 

          document.body.appendChild(link);
          link.click(); 
          document.body.removeChild(link); 

          window.URL.revokeObjectURL(object_URL);
        }).catch(error => {
          this.$push_toast('Файл не может быть скачен.', { type: 'danger', duration: 5000 });
        });
        
      }
    }
  }
</script>

<template>

  <div id="CardView" class="field">

    <div class="box">

      <div class="field">
        <span class="has-text-left has-text-weight-light"> <strong>Дисциплина:</strong> "{{this.data.discipline.subject}}" на базе {{this.data.discipline.level}} кл.</span>
      </div>

      <div class="columns">

        <div class="column">
          <figure class="image is-3by2">
            <img :src="GetFileServer(this.data.path_preview)" />
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
          <button class="button is-primary is-fullwidth" @click="DownloadDocument()">Получить положение</button>
        </div>

      </div>

    </div>
  </div>
</template>

