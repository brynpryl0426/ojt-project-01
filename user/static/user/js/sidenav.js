function url_activator(target_pattern){
    var path = '.navigator a[href^="'+target_pattern+'' + location.pathname.split(target_pattern)[1] + '"]';
    $(path).addClass('active');
    $(path).parents('.collapsible-body').css("display", "block");
    $(path).parents('.collapsible-body').prev().addClass('active');
}