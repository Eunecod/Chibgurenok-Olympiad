<script>
  import _axios from '@/util/axioshandler.js';
  import { DownloadCSV } from '@/util/CSV.js';

  export default {
    data() {
      return {
        results: [],
        disciplines: [],

        filter_subject: '',
        filter_level: '',
        filter_login: '',

        current_page: 1,
        items_page: 10,
      };
    },
    mounted() {
      this.InitFormFilter();
    },
    computed: {
      FilteredResults() {
        return this.results.filter(result => {
          const matches_login = this.filter_login ? result.login.toLowerCase().includes(this.filter_login.toLowerCase()) : true;
          return matches_login;
        });
      },
      PaginatedResults() {
        const start = (this.current_page - 1) * this.items_page;
        return this.FilteredResults.slice(start, start + this.items_page);
      },
      TotalPages() {
        return Math.ceil(this.FilteredResults.length / this.items_page);
      }
    },
    methods: {
      DownloadCSV,
      InitFormFilter() {
        const URL = '/get/disciplines';
        _axios.get(URL).then(response => {
          this.disciplines = response.data.disciplines;
        }).catch(error => {
          console.error(error);
        });
      },
      LoadResult() {
        const URL = '/admin/result';
        let params = {
          subject:  this.filter_subject,
          level:    this.filter_level
        };
        _axios.get(URL, { params }).then(response => {
          this.results = response.data.results.sort((rhs, lhs) => lhs.assessed - rhs.assessed);
        }).catch(error => {
          console.error(error);
        });
      },
      ChangePage(page) {
        if (page < 1 || page > this.TotalPages)
          return;

        this.current_page = page;
      },
      OpenReplyBody(reply_id) {
        this.$router.push({ name: 'ReplyAdmin', params: { id: reply_id } });  
      },
    }
  }
</script>

<template>

  <div id="ResultAdmin">
    <section class="section">
      <div class="container">

        <div class="columns">

          <div class="column">
            <div class="select is-fullwidth">
              <select v-model="filter_subject">

                <option class="is-hidden" disabled selected value=''> Выберите дисциплину </option>
                <option v-for="(discipline, index) in disciplines" :key="index" :value="discipline.subject"> {{ discipline.subject }} </option>

              </select>
            </div>
          </div>

          <div class="column">
            <div class="select is-fullwidth">
              <select v-model="filter_level">

                <option class="is-hidden" disabled selected value=''> Выберите категорию </option>
                <option v-for="(discipline, index) in disciplines" :key="index" :value="discipline.level"> {{ discipline.level }} </option>

              </select>
            </div>
          </div>

        </div>


        <div class="field">
          <p class="control has-icons-left">
            <input v-model="filter_login" class="input" placeholder="Поиск по пользователю" />
            <span class="icon is-small is-left">
              <i class="fa-solid fa-magnifying-glass"></i>
            </span>
          </p>
        </div>

        <div class="buttons is-right">
          <button class="button" @click="LoadResult()">Получить результаты</button>
          <button class="button" @click="DownloadCSV(results, 'Отчет', ['class', 'login', 'subject', 'level', 'assessed'])" :disabled="FilteredResults.length == 0">
            <span class="icon">
              <i class="fa-solid fa-file-csv"></i>
            </span>
            <span> Выгрузить отчет</span>
          </button>
        </div>

        <div class="table-container">
          <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
            <thead>
              <tr>
                <th>ID</th>
                <th>Класс</th>
                <th>Предмет</th>
                <th>Категория</th>
                <th>Пользователь</th>
                <th>Балл</th>
                <th>Ответы</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(result, index) in PaginatedResults">
                <td>{{index + 1}}</td>
                <td>{{result.class}}</td>
                <td>{{result.subject}}</td>
                <td>{{result.level}}</td>
                <td>{{result.login}}</td>
                <td>{{result.assessed}}/100</td>
                <td>
                  <button class="button is-fullwidth" @click="OpenReplyBody(result.id)">
                    Открыть
                  </button>
                </td>
              </tr>
            </tbody>
          </table>

        </div>
        <div v-if="FilteredResults.length == 0" class="content has-text-centered">
          <i class="fa-solid fa-magnifying-glass"></i> Нет результатов
        </div>

        <div class="level">

          <div class="level-right">
            <nav class="pagination" v-if="FilteredResults.length != 0">
              <ul class="pagination-list level-left">
                <li>
                  <button class="pagination-previous" @click="ChangePage(current_page - 1)">
                    <i class="fa-solid fa-angle-left"></i>
                  </button>
                  <button class="pagination-next" @click="ChangePage(current_page + 1)">
                    <i class="fa-solid fa-angle-right"></i>
                  </button>
                </li>
              </ul>
            </nav>
          </div>

          <div class="level-right">
            <strong> {{current_page}} / {{TotalPages}} страниц </strong>
          </div>

        </div>

      </div>
    </section>
  </div>

</template>
