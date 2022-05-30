$("#formulario_ct").validate({
    rules:{
        nombre_contacto:{
            required: true,
            minlength: 4,
            maxlength: 30
        },
        email_contacto:{
            required: true,
            email: true
        },
        telefono_contacto:{
            required: true,
            minlength: 9,
            maxlength: 9
        },
        mensaje_contacto:{
            required: true,
            minlength: 5,
            maxlength: 200
        }
    }
})





$("#btn_contacto").click(function(){
    if($("#formulario_ct").valid() == false){
        return;
    }
    let nombre_contacto = $("#nombre_contacto").val()
    let email_contacto = $("#email_contacto").val()
    let telefono_contacto = $("#telefono_contacto").val()
    let mensaje_contacto = $("#mensaje_contacto").val()
    let avisos_contacto = $("#avisos_contactos").is("checked")
})








$("#formulario_contacto").validate({
    rules:{
        email:{
            required: true,
            email:true
        },
        password:{
             required: true,
             minlength: 4,
             maxlength: 14
        }
    }
})

$("#btn").click(function(){
    if( $("#formulario_contacto").valid()==false){
        return;
    }
  let email = $("#email").val()
  let password = $("#password").val()
})


