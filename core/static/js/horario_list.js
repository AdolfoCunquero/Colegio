$(function(){
    $("#data").DataTable({
        responsive:true,
        autoWidth:false,
        destroy:true,
        deferRender:true,
        ajax:{
            url:window.location.pathname,
            type:"POST",
            data:{
                "action":"searchdata",
                "csrfmiddlewaretoken":document.getElementsByName("csrfmiddlewaretoken")[0].value
            },
            dataSrc:""
        },
        columns:[
            {"data":"ho_ciclo"},
            {"data":"grado"},
            {"data":"curso"},
            {"data":"ho_usuario_catedratico"},
            {"data":"ho_hora_inicio"},
            {"data":"ho_hora_fin"},
            {"data":"ho_no_periodo"},
            {"data":"ho_no_periodo"}
        ],
        columnDefs:[{
            targets:[-1],
            class:"text-center",
            orderable:false,
            render:function(data, type, row){
                var buttons = '<a href="/horario/update/'+row.ho_id_grado_curso+'/"  class="btn btn-warning btn-xs btn-xs btn-flat">Edit</a> '
                buttons += '<a href="/horario/delete/'+row.ho_id_grado_curso+'/" class="btn btn-danger btn-xs btn-flat">Delete</a>'
                return buttons;
            }
        }],
        initComplete:function(settings, json){
        }
    })
})