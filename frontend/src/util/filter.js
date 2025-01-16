export function FilterInRange(number, range) {
  const _number = parseFloat(number);

  if (range.includes('-')) {
    const [start_range, end_range] = range.split('-');
    return _number >= parseFloat(start_range) && _number <= parseFloat(end_range);
  }
  else {
    return _number === parseFloat(range);
  }
}