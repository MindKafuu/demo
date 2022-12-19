// Calendar Buddhist
$(document).ready(function () {
    $("[data-provide='datepicker']").datepicker({
        format: 'dd/mm/yyyy',
        language: 'th-th',
        thaiyear: true,
        autoclose: true,
        updateViewDate : true,
    });
});

// Button Floating
(function($) {
  $(function() {
      $('.fixed-action-btn').floatingActionButton();
    $('.fixed-action-btn.horizontal').floatingActionButton({
      direction: 'left'
    });
    $('.fixed-action-btn.click-to-toggle').floatingActionButton({
      direction: 'left',
      hoverEnabled: false
    });
    $('.fixed-action-btn.toolbar').floatingActionButton({
      toolbarEnabled: true
    });
  });
})(jQuery);

// Initialize
$(function () {
    $.initialize('[data-inputmask-alias="numeric"]', function () {
        var elem = $(this);
        if (elem.attr('id').toLowerCase().indexOf("__prefix__") >= 0) {
            return;
        }
        elem.inputmask("numeric", {
            radixPoint: ".",
            groupSeparator: ",",
            digits: 2,
            digitsOptional: false,
            autoGroup: true,
            autoUnmask: true,
            removeMaskOnSubmit: true
        });
    });
    $.initialize('[data-inputmask-alias="currency"]', function () {
        var elem = $(this);
        if (elem.attr('id').toLowerCase().indexOf("__prefix__") >= 0) {
            return;
        }
        elem.inputmask('currency', {
            prefix: '',
            radixPoint: ".",
            groupSeparator: ",",
            digits: 2,
            digitsOptional: false,
            autoGroup: true,
            autoUnmask: true,
            removeMaskOnSubmit: true
        });
    });
    $.initialize('[data-inputmask-alias="integer"]', function () {
        var elem = $(this);
        if (elem.attr('id').toLowerCase().indexOf("__prefix__") >= 0) {
            return;
        }
        elem.inputmask("integer", {
            radixPoint: ".",
            groupSeparator: ",",
            digits: 0,
            digitsOptional: false,
            autoGroup: true,
            autoUnmask: true,
            removeMaskOnSubmit: true
        });
    });

    $.initialize('input[data-provide="datepicker"]', function() {
        var elem = $(this);
        var id = elem.attr('id');
        var getDefaultValue = document.getElementById(id).value; // DD/MM/YYYY hh:mm:ss
        var split = getDefaultValue.split(' '); // [0]DD/MM/YYYY, [1]hh:mm:ss
        var date = split[0]; // DD/MM/YYYY
        var splitDate = date.split('/'); // [0]DD, [1]MM, [2]YYYY
        var yearDefault = splitDate[2]; // YYYY
        var toDay = new Date();
        var yearToDay = toDay.getFullYear()+543;

        //Check year of DefaultValue, if B.E. convert to A.D.
        if (yearDefault > yearToDay - 400) {
            date = splitDate[0] + '/' + splitDate[1] + '/' + (parseInt(splitDate[2]) - 543);
        }

        //Calendar B.E.
        if (elem.attr('id').toLowerCase().indexOf("__prefix__") >= 0) {
            return;
        }
        elem.datepicker();
        if ((elem.val().length)) {
            elem.datepicker('update', date);
        }
        else {
            elem.datepicker('clearDates');
        }
        if (elem.prop('readonly')) {
            elem.datepicker('destroy');
            elem.removeAttr('data-provide');
        }

        //set Value
        var setValue = document.getElementById(id).value;
        document.getElementById(elem.attr('id')).setAttribute('value', setValue);
    });
    $.initialize('select[readonly]', function() {
        var elem = $(this);
        if (elem.attr('id').toLowerCase().indexOf("__prefix__") >= 0) {
            return;
        }
        if (elem.attr('data-autocomplete-light-function')) {
            elem.select2('destroy');
        }
        var $input = $('<input>').attr({
            'type': 'text',
            'id': 'replace-' + elem.attr('id'),
            'name': 'replace-' + elem.attr('name'),
            'class': elem.attr('class'),
            'value': ((elem.find('option:selected').text() == '---------') ? '' : elem.find('option:selected').text())
        }).prop('readonly', true);
        var $hidden = $('<input>').attr({
            'type': 'hidden',
            'id': elem.attr('id'),
            'name': elem.attr('name'),
            'value': elem.val()
        });
        elem.replaceWith($input);
        $input.after($hidden);
    });
    $.initialize(':checkbox[readonly]', function() {
        var $parent = $(this).parent();
        var elem = $(this);
        var $checkbox = elem.clone().attr({
            'id': 'replace-' + elem.attr('id'),
            'name': 'replace-' + elem.attr('name')
        })
        .prop('disabled', true)
        .prop('readonly', false);
        var $hidden = $('<input>').attr({
            'type': 'hidden',
            'id': elem.attr('id'),
            'name': elem.attr('name'),
            'value': elem.val()
        });
        elem.replaceWith($checkbox);
        $parent.after($hidden);
    });
});

/*$(function () {

    var initialized = [];

    function initialize(element) {
        if (typeof element === 'undefined' || typeof element === 'number') {
            element = this;
        }

        if (initialized.indexOf(element) >= 0) {
            return;
        }

        $(element).trigger('formInitialize');
        initialized.push(element);
    }

    $(document).ready(function() {
        $('input,select').each(initialize);
    });

    $(document).bind('DOMNodeInserted', function(e) {
        $(e.target).find('input,select').each(initialize);
    });

});

$(function () {

    $(document).on('formInitialize', 'input,select', function() {

        var element = $(this);

        // initialize date picker
        if (element.attr('data-provide') == 'datepicker') {
            if (element.val() != '' && element.val() != 'null') {
                element.datepicker('update', element.val());
            } else {
                element.val('');
            }
        }

        if (element.attr('readonly')) {
            if (element.attr('data-provide') == 'datepicker') {
                element.datepicker('destroy');
                element.removeAttr('data-provide');
            }
            if (element.attr('type') == 'checkbox' || element.prop('tagName') == 'SELECT') {
                element.prop('disabled', true);
            }
        }
    });

});
*/

// disabled key enter when work with form
$(function () {
    $('div.main form').on('keyup keypress', function(e) {
        var keyCode = e.keyCode || e.which;
        if (keyCode === 13 && $(this).attr('id').indexOf('_findlist') == -1) {
            e.preventDefault();
            return false;
        }
    });
});

// formsets tools
function resetFormset(table) {
    var $table = $(table);
    if ($table.length) {
        $table.find('tbody > tr').each(function() {
            if ($(this).css('display') === 'none') {return true;}
            if ($(this).hasClass('formset-custom-template')) {return true;}
            if ($(this).find('.add-row').length) {return true;}
            $(this).find('.delete-row').trigger('click');
        });
    }
}
function loadFormset(table, values) {
    //console.log(table, values);
}
function insertFormset(table, values, prefix) {
    var $table = $(table);
    var $total = $('#id_' + prefix + '-TOTAL_FORMS');
    var index;
    if ($table.length && values.length && $total.length) {
        $table.find('.add-row').trigger('click');
        index = (parseInt($total.val())-1);
        var elem_id, elem;
        for (var i=0; i<values.length; i++) {
            elem_id = 'id_' + prefix + '-' + index + '-' + values[i].name;
            elem = $table.find('#' + elem_id);
            if (elem) {
                elem.val(values[i].value);
                if (values[i].hasOwnProperty('trigger')) {
                    elem.trigger(values[i].trigger);
                }
            }
        }
    }
    return index;
}
function updateFormset(table, data, index) {
    //console.log(table);
}
function deleteFormset(table, data, index) {
    //console.log(table);
}

// set inputmask number
function maskCurrency(elem) {
    var $elem = $(elem);
    if ($elem.length && !$elem.hasOwnProperty('inputmaskAlias')) {
        $elem.inputmask("numeric", {
            radixPoint: ".",
            groupSeparator: ",",
            digits: 2,
            digitsOptional: false,
            autoGroup: true,
            autoUnmask: true,
            removeMaskOnSubmit: true
        });
    }
}

// set text curreny
function toCurrency(val) {
    var output = '';
    if (val) {
        val = parseFloat(val);
        if (val) {
            output = val.toFixed(2).replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
        }
    }
    return output
}

function isDecimal(val) {
    var decimal=  /^-?[0-9]\d*(\.\d+)?$/ ;
    return val.match(decimal);
}

// Disable View_Source
 window.onload = function() {
    // document.addEventListener("contextmenu", function(e){
    //   e.preventDefault();
    // }, false);
    document.addEventListener("keydown", function(e) {
    //document.onkeydown = function(e) {
      // "I" key
      if (e.ctrlKey && e.shiftKey && e.keyCode == 73) {
        disabledEvent(e);
      }
      // "J" key
      if (e.ctrlKey && e.shiftKey && e.keyCode == 74) {
        disabledEvent(e);
      }
      // "S" key + macOS
      if (e.keyCode == 83 && (navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey)) {
        disabledEvent(e);
      }
      // "U" key
      if (e.ctrlKey && e.keyCode == 85) {
        disabledEvent(e);
      }
      // "F12" key
      if (event.keyCode == 123) {
        disabledEvent(e);
      }
    }, false);
    function disabledEvent(e){
      if (e.stopPropagation){
        e.stopPropagation();
      } else if (window.event){
        window.event.cancelBubble = true;
      }
      e.preventDefault();
      return false;
    }
  };

// Encode_Data
var k = '301';
var jsEncode = {
    encode: function (s) {
        var enc = "";
        for (var i = 0; i < s.length; i++) {
            // create block
            var a = s.charCodeAt(i);
            // bitwise XOR
            var b = a ^ k;
            enc = enc + String.fromCharCode(b);
        }
        return enc;
    }
};

// test
function disableSelection(e){
    if(typeof e.onselectstart!="undefined")e.onselectstart=function(){return false};
    else if(typeof e.style.MozUserSelect!="undefined")e.style.MozUserSelect="none";
        else e.onmousedown=function(){return false};
        e.style.cursor="default"
}
window.onload=function(){
    disableSelection(document.body)
};