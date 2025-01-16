import { defineStore } from 'pinia';


export const Session = defineStore('session', {
  state: () => ({
    administrator:  false,
    authorized:     false,
  }),
  actions: {
    SetAuthorized(state, grand = false) {
      this.administrator = grand;
      this.authorized = state;
    },
    GetAuthorized() {
      return this.authorized;
    },
    IsAdministrator() {
      return this.administrator;
    }
  },
  persist: true,
  storage: window.sessionStorage,
});
