const getAllcheckBox = document.querySelectorAll('.check')
const getHeaderSelect = document.querySelector('#select_box')
const getOptionBox = document.querySelector('#option_box')
// getAllcheckBox.forEach(element => {
//   console.log(element.checked) // print false because no checkbox is checked
//   if(element.checked == false){ // if element is not checked then they return false
//     element.checked = true // because no checkbox is checked, check them
//     console.log(element.checked) // at this time all the element is checked,it will return true.
//   }
// });

// Select all the box
const selectAllBox = () =>{
  getAllcheckBox.forEach(element => {
  console.log(element.checked) // print false because no checkbox is checked
  if(element.checked == false){ // if element is not checked then they return false
    element.checked = true // because no checkbox is checked, check them
    console.log(element.checked) // at this time all the element is checked,it will return true.
  }
  
});
}

// DeSelect all the box
const deSelectAllBox = ()=>{
   getAllcheckBox.forEach(element => {
  console.log(element.checked) // print false because no checkbox is checked
  if(element.checked == true){ // if element is not checked then they return false
    element.checked = false // because no checkbox is checked, check them
    console.log(element.checked) // at this time all the element is checked,it will return true.
  }
  
});
}


// When the header checkbox is selected then call the functions
getHeaderSelect.addEventListener('change',()=>{
  if(getHeaderSelect.checked == true){
    selectAllBox()
    getOptionBox.classList.remove('d-none')
    getOptionBox.classList.add('d-block')
  }else{
    deSelectAllBox()
    getOptionBox.classList.remove('d-block')
    getOptionBox.classList.add('d-none')
  }
})
