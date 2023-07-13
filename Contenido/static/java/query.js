$(function(){
    $("#formulario").validate({

        rules:{
            nombre:{
                required:true,
                minlength: 3
            },
            rut:{
                required:true,
                number: true
            },
            fono:{
                required:true,
                number:true,
                minlength: 9
            },
            email:{
                required:true,
                email:true
            },
            consulta:{
                required:true
            },
        },//rules
        messages:{
            nombre:{
                required:'Ingrese nombre de usuario',
                minlength:'Caracteres insuficientes (3)'
            },
            rut:{
                required:'Ingrese su rut',
                minlength:'Digitos insuficientes(9)'
            },
            fono:{
                required:'Ingrese número de teléfono',
                minlength:'Digitos insuficientes (10)'
            },
            email:{
                required:'Ingrese correo electrónico',
                email:'Formato de correo no válido'
            },
            consulta:{
                required: 'Se debe hacer la consulta',
            }
        },
    })
});
