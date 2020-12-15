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
            
            {"data":"cu_nombre"},
            {"data":"cu_descripcion"},
            {"data":"cu_descripcion"}
        ],
        columnDefs:[{
            targets:[-1],
            class:"text-center",
            orderable:false,
            render:function(data, type, row){
                var buttons = '<a href="/curso/update/'+row.cu_id_curso+'/"  class="btn btn-warning btn-xs btn-xs btn-flat">Edit</a> '
                buttons += '<a href="/curso/delete/'+row.cu_id_curso+'/" class="btn btn-danger btn-xs btn-flat">Delete</a>'
                return buttons;
            }
        }],
        initComplete:function(settings, json){
        }
    })
})