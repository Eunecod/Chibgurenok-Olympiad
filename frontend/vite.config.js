import { fileURLToPath, URL   } from 'node:url'
import { defineConfig         } from 'vite';
import { NodePackageImporter  } from 'sass-embedded';

import plugin from '@vitejs/plugin-vue';

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [plugin()],
    server: {
        port: 8000,
    },
    resolve: {
        alias: {
          '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    },
    css: {
    preprocessorOptions: {
      scss: {
        api: 'modern',
        importers: [new NodePackageImporter()],
      },
    },
  },
})
