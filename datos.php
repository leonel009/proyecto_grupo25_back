<?php
//conctamos con el servidor
$conectar=@mysql_connect('localhost','root','');
//verificamos la conexion
if(!$conectar){
    echo"No se pudo conectar con el servidor";
    }else{
        $base=mysql_select_db('prueba');
        if(!$base){
            echo"No se encontro la Base de Datos";
        }
    }
//recuperar las variables 
$nombre=$_POST['nombre'];
$correo=$_POST['correo'];
$mensaje=$_POST['mensaje'];
//hacemos la secuencia de sql
$sql="INSERT INTRO datos VALUES('$nombre', '$correo' , '$mensaje')";
//ejecutamos la secuencia de sql 
$ejecutar=mysql_query($sql);
//verificamos la ejecucion
if(!$ejecutar){
    echo"Hubo Algun Error";
    }else{
        echo"Datos Guardados Correctamente<br><a href='index.html'>Volver</a>;
    }
    ?>




?> 