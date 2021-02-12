
var a=1,b=2;//1
var res=a+b;
console.log (res);

var a=1; //2
var res=a*4;
console.log (res);

var a=3,b=2; c=4;//3
var res=(a+b+c)/3;
console.log (res);

function fun_1(){//4
console.log (7);
}
fun_1 ();

function fun_2(a){//5
console.log (a%5);
}
fun_2 (7);

function fun_3(a,b){//6
console.log ("a:"+a,"b:"+b);
}
fun_3 (7,4);

var a=[5, 8,4,6,7];
function fun_4(a){//7
if (a. indexOf(8)!=-1|| a. indexOf(4)!=-1) {
console.log ("true");
}else{
console.log ("false")
}
}
fun_4 (a);

var a=[6, 7,4];//8
var b=[2, 6,8,9];
function fun_5(a,b){
var res=a[1]/b[0]
console.log (res);
}
fun_5(a, b);

/*var a = "Good night"; //9
   var x = a.replace(/" "/gi, 'privet');
    console.log(x);*/


//Number_13
//function  fn_6(a){
   // a=int(input("¬ведите число"))
//}





$(document).ready(function(){
    $("#my_button").click(function (e){
        alert("Button 1")
    })
    $(".my_button_2").click(function (e){
        alert("Button 2")
    })
});

$(document).ready(function(){
    $("#button1").click(function (e){
        x=$("#input1").val()
        if(x.length<4){
            alert ("Not value log in")
            e.preventDefault()
        }

    })
});

$(document).ready(function(){
    $("#button1").click(function (e){
        k=$("#password_1").val()
        if(k.length<2){
            alert ("Not value password")
            e.preventDefault()
        }

    })
});

$(document).ready(function(){
    $("#button2").click(function (e){
        s=$("#input2").val()
        if(s.length<4){
            alert ("Not value log in")
            e.preventDefault()
        }

    })
});



$(document).ready(function(){
    $("#button2").click(function (e){
        f=$("#password_2").val()
        if(f.length<2){
            alert ("Not value password")
            e.preventDefault()
        }

    })

    $("#my_button_3").click(function (e) {
        $.post("ajax_path",
            {},
            function (response) {
                alert(response.message)
            }
        );
    })


$("#input2").blur(function(){
    $.post("cheak_login",
    {
           "login":$("#input2").val()
    },
   function(response){
        if(response.exist == 1){
            alert("User is exist")
        }
       }
   );
 })

});


/*$("#button2").click(function (e) {
        $.post("ajax_path_reg",
            {window.location.pathname = '/ajax_path_reg"'},
            function (response) {
                alert(response.message)
            }
        );
    })*/




