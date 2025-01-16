import _axios from '@/util/axioshandler.js';
import { GenerateUUID } from '@/util/UUIDService';


const STORAGE_PREFIX = "/storage/file/";

export function GetFileServer(filename) {
  const path = STORAGE_PREFIX + filename;
  return path;
}

export function GetUniqueName(original_name) {
  const extension = original_name.split('.').pop();
  const UUID = GenerateUUID();
  return `${UUID}.${extension}`;
}

export function UploadFile(file) {
  const data = new FormData();

  file.forEach((blob) => {
    data.append("File", blob);
  });

  const URL = '/admin/upload/file'
  _axios.post(URL, data, { headers: { 'Content-Type': 'multipart/form-data' } }).then(response => {
  }).catch(error => {
    console.error(error);
  });
}
