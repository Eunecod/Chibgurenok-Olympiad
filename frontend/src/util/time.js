export function FormatDate(date) {
  const date_string = date.toString();

  const year  = date_string.slice(0, 4);
  const month = date_string.slice(4, 6);
  const day   = date_string.slice(6, 8);

  return `${day}.${month}.${year}`;
}

export function DateNow() {
  const date = new Date();

  const day   = String(date.getDate()).padStart(2, '0');
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const year = date.getFullYear();

  return `${year}-${month}-${day}`
}

export function FormatDatestamp(date) {
  return parseInt(date.replace(/-/g, ''), 10);
}
