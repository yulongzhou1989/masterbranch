var btns = document.querySelectorAll('.page_btn');
var paginationWrapper = document.querySelector('.pagination-wrapper');
var bigDotContainer = document.querySelector('.big-dot-container');
var littleDot = document.querySelector('.little-dot');

for(var i = 0; i < btns.length; i++) {
  btns[i].addEventListener('click', pageBtnClick);
}

function pageBtnClick() {
  if(this.classList.contains('btn--prev')) {
    paginationWrapper.classList.add('transition-prev');

  } else {
    paginationWrapper.classList.add('transition-next');
  }

  var timeout = setTimeout(cleanClasses, 500);
}

function cleanClasses() {
  if(paginationWrapper.classList.contains('transition-next')) {
    paginationWrapper.classList.remove('transition-next')
  } else if(paginationWrapper.classList.contains('transition-prev')) {
    paginationWrapper.classList.remove('transition-prev')
  }
}

var pagination_stack = [];
if (pagination_stack.length == 0) {
  pagination_stack.push({'id': $('#lek_id').val(), 'title': $('#lek_title').val()});
}
