$(document).ready(function()
{

    //Datepicker show, more info in https://jqueryui.com/datepicker/
    $( "#id_update_date" ).datepicker({
                changeMonth: true,
                changeYear: true,
                yearRange: '1900:+nn',
                dateFormat: 'yy-mm-dd',
                maxDate: "+0D",
               });

});
