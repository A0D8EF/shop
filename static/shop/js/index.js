window.addEventListener("load", function (){
    let today   = new Date();
    let year    = String(today.getFullYear());
    let month   = ("0" + String(today.getMonth() + 1)).slice(-2);
    let day     = ("0" + String(today.getDate())).slice(-2);

    let date    = year + "-" + month + "-" + day;
    let config_date = {
        locale: "ja",
        dateFormat: "Y-m-d",
        // defaultDate: date
    }
    flatpickr(".date", config_date);
    flatpickr(".date", config_date);

    $("#search").on("click", function(){ url_replace_sendform(this); });
    $("#search_release").on("click", function(){ url_replace_sendform(this); });
});

function url_replace_sendform(elem){

    let form_elem   = $(elem).parent("form");
    let data        = new FormData( $(form_elem).get(0) );

    // 現在のクエリストリングを取得
    param   = new URLSearchParams(window.location.search);
    console.log(param.toString());

    for (let d of data){
        param.set(d[0], d[1]);
    }
    console.log(param.toString());

    window.location.href = "?" + param.toString();
}