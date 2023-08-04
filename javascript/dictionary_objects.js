var x = [{
    "name": "ravi",
    "age": 23
}, {
    "name": "sahil",
    "age": 21
}, {
    "name": "shiv",
    "age": 22
}
]

try{
    var myValue = x.filter((i)=>(a.name == "shiv"))

    console.log(myValue[0].age)
}catch(error){
    console.log("My err is : " + error)
}finally{
    console.log("the code is executed")
}


