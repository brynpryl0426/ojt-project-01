$(function () {

    // Custom autocomplete instance.
    $.widget( "app.autocomplete", $.ui.autocomplete, {
          
      // Which class get's applied to matched text in the menu items.
      options: {
          highlightClass: "ui-state-highlight"
      },
      
      _renderItem: function( ul, item ) {
  
          // Replace the matched text with a custom span. This
          // span uses the class found in the "highlightClass" option.
          var re = new RegExp( "(" + this.term + ")", "gi" ),
              cls = this.options.highlightClass,
              template = "<span class='" + cls + "'>$1</span>",
              label = item.label.replace( re, template ),
              $li = $( "<li/>" ).appendTo( ul );
          
          // Create and return the custom menu item content.
          $( "<a/>" ).attr( "href", "#" )
                     .html( label )
                     .appendTo( $li );
          
          return $li;
          
      }
      
  });
  
    $("#violatorsearch").autocomplete({
      source: "/traffic-violations-management-monitoring/search-violator/",
      minLength: 2,
      highlightClass:"bold-text"
    });
  });
  