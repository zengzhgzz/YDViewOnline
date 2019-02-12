(function($) {
    $(document).on('formset:added', function(event, $row, formsetName) {
        if (formsetName == 'author_set') {
            // Do something
            alert("哈哈哈哈哈");
        }
    });

    $(document).on('formset:removed', function(event, $row, formsetName) {
        // Row removed
    });
})(django.jQuery);