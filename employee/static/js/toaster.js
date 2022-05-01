var toastElList = [].slice.call(document.querySelectorAll('.toast'))
var option = {
    animation: true,
    delay:5000
} 
var toastList = toastElList.map(function (toastEl) {
  return new bootstrap.Toast(toastEl, option)
})

function showToastMsg(){
    for (var i = 0; i<toastList.length; i++){
        toastList[i].show()
    }
}
showToastMsg()
