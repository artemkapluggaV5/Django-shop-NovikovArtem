document.addEventListener('DOMContentLoaded', function() {
    console.log("TinyMCE Init Script Loaded");

    tinymce.init({
        selector: 'textarea',
        height: 400,
        language: 'ru',
        plugins: [
            'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview',
            'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
            'insertdatetime', 'media', 'table', 'help', 'wordcount'
        ],
        toolbar: 'undo redo | blocks | bold italic backcolor | ' +
                 'alignleft aligncenter alignright alignjustify | ' +
                 'bullist numlist outdent indent | removeformat | help',
        branding: false,
        promotion: false,
        setup: function (editor) {
            editor.on('change', function () {
                editor.save();
            });
        }
    });
});