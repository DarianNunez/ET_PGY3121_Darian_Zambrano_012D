function ConfirmarEnvio(form)
{
enviar = window.confirm('¿Desea confirmar el envio del formulario?');
(enviar)?form.submit():'return false';
}

function contarPalabras(form)

{
texto = form.mensaje.value
texto = texto.split(" ")
form.cantidad.value=texto.length
}
