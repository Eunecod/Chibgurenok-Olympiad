import { saveAs } from 'file-saver';

export function DownloadCSV(data, filename, fields = []) {
  if (fields.length != 0) {
    data = data.map(item => {
      const new_item = {};
      fields.forEach(field => {
        if (field in item) {
          new_item[field] = item[field];
        }
      });
      return new_item;
    });
  }

  const header = Array.isArray(data) ? Object.keys(data[0]).join(",") + "\n" : Object.keys(data).join(",") + "\n";
  const row = Array.isArray(data) ? data.map(obj => Object.values(obj).join(",")).join("\n") : Object.values(data).join(",");

  let csvData = '';
  csvData = header + row;

  const blob = new Blob([csvData], { type: 'text/csv;charset=utf-8;' });
  const filename_extension = filename + '.csv';

  saveAs(blob, filename_extension);
}

export function ReadFieldCSV(file, key) {
  return new Promise((resolve) => {
    const reader = new FileReader();
    reader.onload = (event) => {
      const csv_content = event.target.result;
      const lines = csv_content.split(/\r\n|\n/);

      const headers = lines[0].split(',');
      const index = headers.indexOf(key);
      if (index === -1) {
        return;
      }
      const field = [];
      for (let i = 1; i < lines.length; i++) {
        if (lines[i] === '') {
          continue;
        }
        const row = lines[i].split(',');
        if (row.length > index) {
          field.push(row[index]);
        }
      }
      resolve(field);
    };

    reader.readAsText(file);
  });
}

export function ReadCSV(file) {
  return new Promise((resolve) => {
    const reader = new FileReader();
    reader.onload = (event) => {
      const csv_content = event.target.result;
      const lines = csv_content.split(/\r\n|\n/);
      const headers = lines[0].split(',');

      const field = [];
      for (let i = 1; i < lines.length; i++) {
        if (lines[i] === '') {
          continue;
        }

        const row = lines[i].split(',');
        const obj = {};

        headers.forEach((header, index) => {
          obj[header.trim()] = row[index] ? row[index].trim() : ''; 
        });
        field.push(obj);
      }

      resolve(field);
    };

    reader.readAsText(file);
  });
}