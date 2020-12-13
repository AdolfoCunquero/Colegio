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
            {"data":"jo_id_jornada"},
            {"data":"jo_descripcion"},
            {"data":"jo_id_jornada"},
        ],
        columnDefs:[{
            targets:[-1],
            class:"text-center",
            orderable:false,
            render:function(data, type, row){
                var buttons = '<a href="/jornada/update/'+row.jo_id_jornada+'/"  class="btn btn-warning btn-xs btn-xs btn-flat">Edit</a> '
                buttons += '<a href="/jornada/delete/'+row.jo_id_jornada+'/" class="btn btn-danger btn-xs btn-flat">Delete</a>'
                return buttons;
            }
        }],
        initComplete:function(settings, json){
        }
    })
})