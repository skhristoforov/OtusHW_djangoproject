var checked_count = 0;
var MAX_CHECKED_COUNT = 3;


$(function () {
    $('.button-checkbox').each(function () {
        // Settings
        var $widget = $(this),
            $button = $widget.find('button'),
            $checkbox = $widget.find('input:checkbox'),
            color = $button.data('color')

        // Event Handlers
        $button.on('click', function () {
            if ($checkbox.prop('checked')) {
                checked_count -= 1;

                $checkbox.prop('checked', !$checkbox.is(':checked'));
                $checkbox.triggerHandler('change');
                updateDisplay();
            } else if (checked_count < MAX_CHECKED_COUNT) {
                checked_count += 1;
                $checkbox.prop('checked', !$checkbox.is(':checked'));
                $checkbox.triggerHandler('change');
                updateDisplay();
            }
        });

        $checkbox.on('change', function () {
            updateDisplay();
        });

        // Actions
        function updateDisplay() {
            var isChecked = $checkbox.is(':checked');

            // Set the button's state
            $button.data('state', (isChecked) ? "on" : "off");

            // Update the button's color
            if (isChecked) {
                $button
                    .css('background-color', '#00cc66')
                    .css('color', '#fafcfb')
                    .css('font-weight', 'bold');
            }
            else {
                $button
                    .css('background-color', '#8775a7')
                    .css('color', '#fafcfb')
                    .css('font-weight', 'bold');
            }
        }

        // Initialization
        function init() {
            updateDisplay();
        }

        init();
    });
});