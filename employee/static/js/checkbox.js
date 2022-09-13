const getAllcheckBox = document.querySelectorAll('.check')
const getHeaderSelect = document.querySelector('#select_box')
const getOptionBox = document.querySelector('#option_box')


// Select all the box
const selectAllBox = () =>{
  getAllcheckBox.forEach(element => {
  console.log(element.checked) // print false because no checkbox is checked
  if(element.checked == false){ // if element is not checked then they return false
    element.checked = true // because no checkbox is checked, check them
    console.log(element.checked.length) // at this time all the element is checked,it will return true.
  }
  
});
}

// DeSelect all the box
const deSelectAllBox = ()=>{
   getAllcheckBox.forEach(element => {
  if(element.checked == true){ // if element is not checked then they return false
    element.checked = false // because no checkbox is checked, check them
  }
  
});
}


// When the header checkbox is selected then call the functions
getHeaderSelect.addEventListener('change',()=>{
  if(getHeaderSelect.checked == true){
    selectAllBox()
  }
  else{
    deSelectAllBox()
  }
})


console.log(getAllcheckBox.checked) // this is the logic to apply
