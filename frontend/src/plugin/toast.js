import { createApp } from 'vue';
import Toast from '@/components/Service/Toast.vue';

const ToastPlugin = {
  install(app) {
    const _toast = (message, options = {}) => {
      const constructor = createApp(Toast, {
        message:  message,
        type:     options.type,
        duration: options.duration,
      });

      const instance = constructor.mount(document.createElement('div'));
      document.body.appendChild(instance.$el);

      setTimeout(() => {
        document.body.removeChild(instance.$el); 
      }, options.duration + 500); // 0.5 second ~ transition: all 0.5s ease;
    };

    app.config.globalProperties.$push_toast = _toast;
  }
};

export default ToastPlugin;
