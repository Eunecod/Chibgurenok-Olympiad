import axios          from 'axios';


const _axios = axios.create({
  withCredentials:  true,
  baseURL:          '/api', 
});

_axios.interceptors.response.use(
  response => {
    return response; 
  },
  error => {
    return Promise.reject(error);
  }
);

export default _axios;
