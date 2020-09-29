// sanity check
// console.log('Everything is linked and working!!');

var button = document.getElementsByClassName('actualButton')[0];

button.addEventListener('mouseover', function() {
  console.log('hello from mr. button!');
  button.style.background = 'blue';
});

button.addEventListener('mouseout', function() {
  console.log('goodbye!');
  button.style.background = 'red';
});
