console.log('Hey there')





//get all stars

const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four  = document.getElementById('fourth')
const five = document.getElementById('fifth')

// console.log(one)

const arr = [one,two,three,four,five]


const handleSelect = (Selection)=>{
    switch(Selection){
        case 'first':{
            one.classList.add('selected')
            two.classList.remove('selected')
            three.classList.remove('selected')
            four.classList.remove('selected')
            five.classList.remove('selected')
        } 
    }
}
arr.forEach(item => item.addEventListener('mouseover',(event)=>{
    console.log(event.target)
}))


arr.forEach(item=> item.addEventListener('mouseover',(event)=>{
   handleSelect(event.target.id)
}))


// (event)