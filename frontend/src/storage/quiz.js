import { defineStore } from 'pinia';


export const Reply = defineStore('reply', {
  state: () => ({
    stack: [],
  }),
  actions: {
    SaveReply(id, cache_reply = []) {
      const index = this.stack.findIndex(item => item.id === id);
      if (index !== -1) {
        this.stack[index].cache = cache_reply;
      } else {
        this.stack.push({ id: id, cache: cache_reply });
      }
    },
    GetCache(id) {
      const reply = this.stack.find(item => item.id === id);
      if (reply) {
        return reply.cache;
      }

      return [];
    },
    FreeCache(id) {
      const index = this.stack.findIndex(item => item.id === id);
      if (index !== -1) {
        this.stack.splice(index, 1);
      }
    }
  },
  persist: true,
  storage: window.sessionStorage,
});
