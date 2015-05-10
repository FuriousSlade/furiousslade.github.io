$(function(){
    var d_top=$('#d-top');
    document.onscroll=function(){
        var scrTop=(document.body.scrollTop||document.documentElement.scrollTop);
        if(scrTop>500){
            d_top.show();
        }else{
            d_top.hide();
            }

    $('#d-top-a').click(function(){
    $("html,body").animate({scrollTop: 0},500);

    this.blur();
    return false;
});
}});