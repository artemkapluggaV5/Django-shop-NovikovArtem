document.addEventListener('DOMContentLoaded', function () {

    tinymce.remove();

    tinymce.init({
        selector: '#id_description',
        height: 400,
        width: '100%',
        language: 'ru',

        plugins: ['lists'],

        toolbar: 'undo redo | bold italic | bullist numlist',

        menubar: false,
        statusbar: false,
        branding: false,


        valid_styles: {
            '*': ''
        },

        valid_elements: 'p,b,strong,i,em,ul,ol,li',

        forced_root_block: 'p',

        setup: function (editor) {
            editor.on('change', function () {
                editor.save();
            });
        }
    });
});